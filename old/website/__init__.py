from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
DB_Blog = "blogPosts.db"


def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Blog}'
    #db.init_app(app)

    from .views import views
    from .blog import blog
    #from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(blog,  url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    #create_database(app,DB_NAME)
    #create_database(app,DB_Blog)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app,DB):
    if not path.exists('website/' + DB):
        db.create_all(app=app)
        print('Created {} Database!'.format(DB))