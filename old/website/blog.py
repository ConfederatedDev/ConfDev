from flask import Blueprint, render_template, request, flash, jsonify, Response
from flask_login import login_required, current_user
from . import db
import json


blog = Blueprint('blog', __name__)



@blog.route('/blog/HelloWorld',methods=['GET'])
def HelloWorld():
    
    return render_template("blog_HelloWorld.html", user=current_user)
