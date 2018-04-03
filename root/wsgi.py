from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:522314@localhost/postgres'
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:doberman@localhost/postgres'
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

@application.route('/')
def index():
    #return render_template('index.html')
    return 'Hello World!'

if __name__ == "__main__":
    application.run(debug = True)

# @application.route('/hello.html')
# def hello():
#     return render_template('hello.html')

# @application.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)
