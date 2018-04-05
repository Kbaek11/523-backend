from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Users, UserData
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

#TODO Rest API

#endpoint to create new user
# @application.route("/", methods=["POST"])
# def addUser():
#     if request.method == 'POST':
#         userId = request.form['userId']
#         team = request.form['team']
#         newUser = Users(userId, team)
#         db.session.add(newUser)
#         db.session.commit()

#    return 401
# @application.route('/test', methods=['GET', 'POST'])
# def test():
#     if request.method == 'GET':
#         return (
#             '<form action="/test" method="post"><input type="submit" value="Send" /></form>'
#         )

#     elif request.method == 'POST':
#         return "OK this is a post method"
#     else:
#         return ("ok")

# # endpoint to get user info by id
# @app.route("/<id>", methods=["GET"])
# def user_detail(id):
#     user = Users.query.get(id)
#     return .jsonify(user)


@application.route('/', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        userId = request.form['userId']
        team = request.form['team']
        newUser = Users(userId, team)
        db.session.add(newUser)
        db.session.commit()
    return jsonify(userId=request.form[userId], team=request.form[team])


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
