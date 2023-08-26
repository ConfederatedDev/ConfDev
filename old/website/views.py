from flask import Blueprint, render_template, request, flash, jsonify, Response,current_app,url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import db
import json
import os
import smtplib
from email.message import EmailMessage
from PIL import Image
import base64
import io
from rembg import remove

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

views = Blueprint('views', __name__)

@views.route('/',methods=['GET'])
def home():

    return render_template("home.html", user=current_user)

@views.route('/projects',methods=['GET'])
def projects():

    return render_template("projects.html", user=current_user)

@views.route('/projects/removeBG',methods=['GET','POST'])
def removeBG():
    #print(current_app.config)
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template("removeBG.html", user=current_user)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template("removeBG.html", user=current_user)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            #file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join("imageHolder", filename))
            im = Image.open(file)
            output = remove(im)#.convert('RGB')
            data = io.BytesIO()
            output.save(data, "PNG")
            encoded_img_data = base64.b64encode(data.getvalue())
            #,linkBack=url_for('views.removeBG')
            return render_template("removedBG.html", user=current_user, img_data=encoded_img_data.decode('utf-8'))
    return render_template("removeBG.html", user=current_user)

@views.route('/projects/removedBG',methods=['GET','POST'])
def removedBG():

    return render_template("removeBG.html", user=current_user)

@views.route('/contact',methods=['GET','POST'])
def contact():
    
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        BC = float(request.form.get("BotCheck"))
        #print(BC)
        ##breakpoint()
        if(BC==20):
            
            
            subjectFull =   "Confederated.dev - Contact Form - "+subject
            
            msg = EmailMessage()
            msg['Subject'] = subjectFull
            msg['From'] = "contact@confederated.dev"
            msg['To'] = "admin@confederated.dev"
            msg.set_content(message)
            
            
            breakpoint()
            sendEmail = smtplib.SMTP('localhost')
            sendEmail.send_message(msg)
            sendEmail.quit()
            print("Email Sent")

        else:
            error_statement = "Bot Check Failed"



    return render_template("contact.html", user=current_user)

@views.route('/blog',methods=['GET'])
def blog():

    return render_template("blog.html", user=current_user)