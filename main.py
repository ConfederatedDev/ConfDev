from website import create_app

app = create_app()

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'imageHolder'
    app.run(debug=True)
    