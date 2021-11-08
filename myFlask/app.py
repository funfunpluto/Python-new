from flask import Flask, render_template, flash, request, redirect, url_for, session, logging
#did not use Flask-Bootstrap coz it is a little weird to use ;
#instead use BootstrapCDN
#https://www.youtube.com/watch?v=zRwy8gtgJ1A&t=0s&index=16&list=WL
#python3 app.py; open browser, run http://localhost:5000

from data import Articles
#import mysql.connector flask-mysqldb is not for python3
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

# config mysql & init db
#SQLALCHEMY_DATABASE_URI = "mysql://username:password@server/db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://hz028:hippo828@localhost/myflaskapp"
db = SQLAlchemy(app)


Articles = Articles()

@app.route('/')
def index():
    #return 'INDEX'
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id = id)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=8, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match'),
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validator():

        return render_template('register.html')
    return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
