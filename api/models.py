from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#Database
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, unique=True)
    team = db.Column(db.String(80), unique=False)

    def __init__(self, userId, team):
        self.userId = userId
        self.team = team


class UserData(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    day1 = db.Column(db.Integer)
    day2 = db.Column(db.Integer)
    day3 = db.Column(db.Integer)
    day4 = db.Column(db.Integer)
    day5 = db.Column(db.Integer)
    day6 = db.Column(db.Integer)
    day7 = db.Column(db.Integer)
    day8 = db.Column(db.Integer)
    day9 = db.Column(db.Integer)
    day10 = db.Column(db.Integer)
    day11 = db.Column(db.Integer)
    day12 = db.Column(db.Integer)
    day13 = db.Column(db.Integer)
    day14 = db.Column(db.Integer)

    def __init__(self, studentId, day1, day2, day3, day4, day5, day6, day7,
                 day8, day9, day10, day11, day12, day13, day14):
        self.studentId = studentId
        self.day1 = day1
        self.day2 = day2
        self.day3 = day3
        self.day4 = day4
        self.day5 = day5
        self.day6 = day6
        self.day7 = day7
        self.day8 = day8
        self.day9 = day9
        self.day10 = day10
        self.day11 = day11
        self.day12 = day12
        self.day13 = day13
        self.day14 = day14
