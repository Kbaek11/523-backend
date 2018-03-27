from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:522314@localhost/postgres'
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@application.route('/')
def main():
    return render_template('index.html')

@application.route('/hello.html')
def hello():
    return render_template('hello.html')

@application.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == "__main__":
    application.run(debug = True)
