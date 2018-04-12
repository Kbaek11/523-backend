from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


#Database
class Users(db.Model):
    __tablename__ = 'users'
    #TODO Mabe I can make my userId be the primary key
    userId = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(80))

    def __init__(self, userId, team):
        self.userId = userId
        self.team = team


class UserAnswers(db.Model):
    __tablename__ = 'calendar'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    answeredDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    day1a = db.Column(db.String(80))
    day1b = db.Column(db.String(80))
    day1c = db.Column(db.String(80))
    day2a = db.Column(db.String(80))
    day2b = db.Column(db.String(80))
    day2c = db.Column(db.String(80))
    day3a = db.Column(db.String(80))
    day3b = db.Column(db.String(80))
    day3c = db.Column(db.String(80))
    day4a = db.Column(db.String(80))
    day4b = db.Column(db.String(80))
    day4c = db.Column(db.String(80))
    day5a = db.Column(db.String(80))
    day5b = db.Column(db.String(80))
    day5c = db.Column(db.String(80))
    day6a = db.Column(db.String(80))
    day6b = db.Column(db.String(80))
    day6c = db.Column(db.String(80))
    day7a = db.Column(db.String(80))
    day7b = db.Column(db.String(80))
    day7c = db.Column(db.String(80))
    day8a = db.Column(db.String(80))
    day8b = db.Column(db.String(80))
    day8c = db.Column(db.String(80))
    day9a = db.Column(db.String(80))
    day9b = db.Column(db.String(80))
    day9c = db.Column(db.String(80))
    day10a = db.Column(db.String(80))
    day10b = db.Column(db.String(80))
    day10c = db.Column(db.String(80))
    day11a = db.Column(db.String(80))
    day11b = db.Column(db.String(80))
    day11c = db.Column(db.String(80))
    day12a = db.Column(db.String(80))
    day12b = db.Column(db.String(80))
    day12c = db.Column(db.String(80))
    day13a = db.Column(db.String(80))
    day13b = db.Column(db.String(80))
    day13c = db.Column(db.String(80))
    day14a = db.Column(db.String(80))
    day14b = db.Column(db.String(80))
    day14c = db.Column(db.String(80))

    q1 = db.Column(db.Boolean)
    q2 = db.Column(db.Boolean)
    q3 = db.Column(db.Boolean)
    q4 = db.Column(db.Boolean)
    q5 = db.Column(db.Boolean)
    q6 = db.Column(db.Boolean)
    q7 = db.Column(db.Boolean)
    q8 = db.Column(db.Boolean)
    q9 = db.Column(db.Boolean)
    q10 = db.Column(db.Boolean)

    def __init__(self, userId, day1a, day1b, day1c, day2a, day2b, day2c, day3a,
                 day3b, day3c, day4a, day4b, day4c, day5a, day5b, day5c, day6a,
                 day6b, day6c, day7a, day7b, day7c, day8a, day8b, day8c, day9a,
                 day9b, day9c, day10a, day10b, day10c, day11a, day11b, day11c,
                 day12a, day12b, day12c, day13a, day13b, day13c, day14a,
                 day14b, day14c, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        self.userId = userId
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
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10


# class UserCalendarAnswers(db.Model):
#     __tablename__ = 'calendaranswers'
#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
#     calendarId = db.Column(db.Integer, db.ForeignKey('calendar.id'))
#     answer1 = db.Column(db.Integer)
#     answer2 = db.Column(db.Integer)
#     answer3 = db.Column(db.Integer)

#     def __init__(self, userId, calendarId, answer1, answer2, answer3):
#         self.userId = userId
#         self.calendarId = calendarId
#         self.answer1 = answer1
#         self.answer2 = answer2
#         self.answer3 = answer3

# class TrueFalse(db.Model):
#     __tablename__ = 'truefalse'
#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
#     q1 = db.Column(db.Boolean)
#     q2 = db.Column(db.Boolean)
#     q3 = db.Column(db.Boolean)
#     q4 = db.Column(db.Boolean)
#     q5 = db.Column(db.Boolean)
#     q6 = db.Column(db.Boolean)
#     q7 = db.Column(db.Boolean)
#     q8 = db.Column(db.Boolean)
#     q9 = db.Column(db.Boolean)
#     q10 = db.Column(db.Boolean)

#     def __init__(self, userId, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
#         self.userId = userId
#         self.q1 = q1
#         self.q2 = q2
#         self.q3 = q3
#         self.q4 = q4
#         self.q5 = q5
#         self.q6 = q6
#         self.q7 = q7
#         self.q8 = q8
#         self.q9 = q9
#         self.q10 = q10