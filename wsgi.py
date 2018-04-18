from flask import Flask, jsonify, request, abort  #pylint: disable=E0401
from models import db, Users, UserAnswers
from flask_migrate import Migrate  #pylint: disable=E0401
from dotenv import load_dotenv  #pylint: disable=E0401
from os.path import join, dirname
import os
import psycopg2  #pylint: disable=E0401

#Initialize Flask, SQLAlchemy, Migrate
application = Flask(__name__)
db.init_app(application)
migrate = Migrate(application, db)

#Load .env file
dotenvPath = join(dirname(__file__), '.env')
load_dotenv(dotenvPath)

#Connect to Database
try:
    DB_URL = os.environ.get('DATABASE_URL')
except:
    DB_URL = None

if not DB_URL:
    DB_URL = 'postgresql://postgres:password@localhost/DrugUse'
application.config['SQLALCHEMY_DATABASE_URI'] = DB_URL


#API Routes
@application.route('/', methods=['POST'])
def addUser():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        payload = request.json
        if 'userId' not in payload or 'team' not in payload:
            raise Exception('Missing "userId" or "team" in JSON')
        newUser = Users(payload['userId'], payload['team'])
        try:
            db.session.add(newUser)
            db.session.commit()
        except:
            raise Exception('Error when adding new user to the database')
        return jsonify({"return": {"message": "Successfully added user"}}), 200


@application.route('/', methods=['GET'])
def returnUserData():
    if request.method == 'GET':
        usersList = (Users.query.order_by(Users.userId).all())
        return jsonify([user.serialize() for user in usersList])


@application.route('/questions', methods=['POST'])
def addUserAnswers():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        payload = request.json
        if 'userId' not in payload:
            raise Exception('Missing "userId" in JSON')
        userAnswers = UserAnswers(
            payload['userId'], payload['day1a'], payload['day1b'], payload['day1c'], payload['day2a'],
            payload['day2b'], payload['day2c'], payload['day3a'], payload['day3b'], payload['day3c'],
            payload['day4a'], payload['day4b'], payload['day4c'], payload['day5a'], payload['day5b'],
            payload['day5c'], payload['day6a'], payload['day6b'], payload['day6c'], payload['day7a'],
            payload['day7b'], payload['day7c'], payload['day8a'], payload['day8b'], payload['day8c'],
            payload['day9a'], payload['day9b'], payload['day9c'], payload['day10a'], payload['day10b'],
            payload['day10c'], payload['day11a'], payload['day11b'], payload['day11c'], payload['day12a'],
            payload['day12b'], payload['day12c'], payload['day13a'], payload['day13b'], payload['day13c'],
            payload['day14a'], payload['day14b'], payload['day14c'], payload['q1'], payload['q2'], payload['q3'],
            payload['q4'], payload['q5'], payload['q6'], payload['q7'], payload['q8'], payload['q9'], payload['q10'])

        try:
            db.session.add(userAnswers)
            db.session.commit()
        except:
            raise Exception('Error when adding user answers to the database')
        return jsonify({
            "return": {
                "message": "Successfully added user answers"
            }
        }), 200

@application.route('/questions', methods=['GET'])
def returnUserAnswers():
    if request.method == 'GET':
        userAnswersList = (UserAnswers.query.order_by(Users.userId).all())
        return (jsonify([user.serialize() for user in userAnswersList]))

@application.route('/results', methods=['GET'])
def retrunResults():
    if request.method == 'GET':
        userAnswersList = (UserAnswers.query.order_by(Users.userId).all())
        return (jsonify([user.serialize() for user in userAnswersList]))


#Run Application
if __name__ == "__main__":
    #TODO turn debug mode off for production
    application.run(host='0.0.0.0', port=33507, debug=False)
    db.create_all()
