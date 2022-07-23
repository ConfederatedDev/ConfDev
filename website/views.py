from flask import Blueprint, render_template, request, flash, jsonify, Response
from flask_login import login_required, current_user
from . import db
import json
import smtplib
from email.message import EmailMessage


views = Blueprint('views', __name__)

@views.route('/',methods=['GET'])
def home():

    return render_template("home.html", user=current_user)

@views.route('/projects',methods=['GET'])
def projects():

    return render_template("projects.html", user=current_user)

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