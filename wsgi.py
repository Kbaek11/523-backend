<<<<<<< HEAD
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:522314@localhost/postgres'
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2
>>>>>>> fe7f8a9926a842a4d270ab86ee9a8aeb0b2e1965

application = Flask(__name__)
#specify user, pass, host, db name
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/test'
db = SQLAlchemy(application) 
migrate = Migrate(application, db)

#Create tables
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(80), unique=False)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('students.id'))
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)

@application.route('/')
def index():
    #return render_template('index.html')
    return 'Hello World!'

if __name__ == "__main__":
    application.run(debug = True)
    db.create_all()



# @application.route('/hello.html')
# def hello():
#     return render_template('hello.html')

# @application.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)