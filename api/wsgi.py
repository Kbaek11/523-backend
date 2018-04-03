from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Student, StudentData
import psycopg2

#Initialize Flask, SQLAlchemy, Migrations
application = Flask(__name__)
db.init_app(application)
migrate = Migrate(application, db)

#TODO put this in config file
#specify user, pass, host, db name
application.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/DrugUse'

#Insert into Database
#addStudent = Student('bball')
# db.session.add(addStudent)
# db.session.commit()


def test():
    addStudent = Student('ballislife')
    db.session.add(addStudent)
    db.session.commit()


#TODO Rest API
#GET


#POST
class Index(Resource):
    def get(self):
        return {"message": "Hello, World!"}
        #return {userId: students[team]}


api.add_resource(Index, '/')


class Questions(Resource):
    def get(self):
        return {"message": "Hello, World!"}


api.add_resource(Questions, '/questions')

#Run App
if __name__ == "__main__":
    #TODO turn debug mode off for production
    application.run(debug=True)
    db.create_all()

#index is home page
#hello.html is next page they go to for questionnaire
#result.html
#for questionnaire its going to be 2 weeks data (14 days)
#and its going to have the same questioni --how many drinks did you drink that day (int value)?
