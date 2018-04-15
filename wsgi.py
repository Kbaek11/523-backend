from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Users, UserAnswers
from manage import migrate
import psycopg2
import os

#TODO add dates next to calendar instead of using monday, tuesday etc.
#if json field is empty from frontend such as user answering something
#make it so that there is a default value in json before posting

#Initialize Flask, SQLAlchemy, Migrations
application = Flask(__name__)
db.init_app(application)
migrate = Migrate(application, db)

DB_URL = os.environ['DATABASE_URL']
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
        userAnswers = UserAnswers()
        userAnswers.day1a = j['day1a']
        userAnswers.day1b = j['day1b']
        userAnswers.day1c = j['day1c']
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
    application.run()
    db.create_all()
