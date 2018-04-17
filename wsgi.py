from flask import Flask, jsonify, request, abort
from models import db, Users, UserAnswers
from flask_migrate import Migrate
from dotenv import load_dotenv
from os.path import join, dirname
import os
import psycopg2

#Initialize Flask, SQLAlchemy, Migrations
application = Flask(__name__)
db.init_app(application)
migrate = Migrate(application, db)

dotenvPath = join(dirname(__file__), '.env')
load_dotenv(dotenvPath)

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
        if not 'userId' in payload or not 'team' in payload:
            raise Exception('Missing "userId" or "team" in JSON')
        newUser = Users(payload['userId'], payload['team'])
        #allUsers = Users.query.all()
        #print(len(allUsers))
        try:
            db.session.add(newUser)
            db.session.commit()
        except:
            raise Exception('Error when adding new user to the database')
        return jsonify({"return": {"message": "Successfully added user"}}), 200


@application.route('/questions', methods=['POST'])
def addUserAnswers():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        j = request.json
        if not 'userId' in j:
            raise Exception('Missing "userId" in JSON')
        userAnswers = UserAnswers(
            j['userId'], j['day1a'], j['day1b'], j['day1c'], j['day2a'],
            j['day2b'], j['day2c'], j['day3a'], j['day3b'], j['day3c'],
            j['day4a'], j['day4b'], j['day4c'], j['day5a'], j['day5b'],
            j['day5c'], j['day6a'], j['day6b'], j['day6c'], j['day7a'],
            j['day7b'], j['day7c'], j['day8a'], j['day8b'], j['day8c'],
            j['day9a'], j['day9b'], j['day9c'], j['day10a'], j['day10b'],
            j['day10c'], j['day11a'], j['day11b'], j['day11c'], j['day12a'],
            j['day12b'], j['day12c'], j['day13a'], j['day13b'], j['day13c'],
            j['day14a'], j['day14b'], j['day14c'], j['q1'],j['q2'],j['q3'],j['q4'],j['q5'],j['q6'],j['q7'],j['q8'],j['q9'],j['q10'])

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


@application.route('/results', methods=['GET'])
def returnResults():
    if request.method == 'GET':
        print('')


#Run Application
if __name__ == "__main__":
    #TODO turn debug mode off for production
    application.run(host='0.0.0.0', port=33507)
    db.create_all()
