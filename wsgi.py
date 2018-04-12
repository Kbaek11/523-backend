from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Users, UserAnswers
import psycopg2
#TODO add dates next to calendar instead of using monday, tuesday etc. 
# Add a date when the survey was taken on JSON 
#TODO ...and store on backend

#Initialize Flask, SQLAlchemy, Migrations
application = Flask(__name__)
db.init_app(application)
migrate = Migrate(application, db)

#TODO put this in config file
#specify user, pass, host, db name
application.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/DrugUse'

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
            
@application.route('/results', methods=['GET'])
def returnResults():
    if request.method == 'GET':
        
            

#Run Application
if __name__ == "__main__":
    #TODO turn debug mode off for production
    application.run(debug=True)
    db.create_all()
