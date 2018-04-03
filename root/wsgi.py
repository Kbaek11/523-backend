from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:522314@localhost/postgres'
db = SQLAlchemy(application)

# def main():
#     conn_string = "host='localhost' dbname='postgresql' user='postgres' password='522314'"
#     print ("Connecting to database\n")
#     conn = psycopg2.connect(conn_string)
#     cursor = conn.cursor()
#     print ("Connected!\n")

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     team = db.Column(db.String(120), unique=True)

@application.route('/')
def index():
    return render_template('index.html')
    #return 'Hello World!'

@application.route('/hello.html')
def hello():
    return render_template('hello.html')

# @application.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

if __name__ == "__main__":
    application.run(debug = True)
