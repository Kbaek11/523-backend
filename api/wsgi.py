from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Users, Calendar, TrueFalse
import psycopg2
#TODO add dates next to calendar instead of using monday, tuesday etc. Add a date when the survey was taken on JSON 
#TODO ...and store on backend
#Initialize Flask, SQLAlchemy, Migrations
application = Flask(__name__)
db.init_app(application)
migrate = Migrate(application, db)

#TODO put this in config file
#specify user, pass, host, db name
application.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/DrugUse'

#TODO Rest API

# # endpoint to get user info by id
# @app.route("/<id>", methods=["GET"])
# def user_detail(id):
#     user = Users.query.get(id)
#     return .jsonify(user)

#TODO
@application.route('/', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        payload = request.json
        if not 'userId' in payload or not 'team' in payload:
            raise Exception('Missing "userId" or "team" in JSON')
        userId = payload['userId']
        team = payload['team']
        newUser = Users(userId, team)
        try:
            db.session.add(newUser)
            db.session.commit()
        except:
            raise Exception('Error when adding new user to the database')
    message = {"return": {"message": "Successfully added user"}}
    return jsonify(message), 200

@application.route('/questions', methods=['GET', 'POST'])


#Run Application
if __name__ == "__main__":
    #TODO turn debug mode off for production
    application.run(debug=True)
    db.create_all()
