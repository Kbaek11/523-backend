from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


#Database
class Users(db.Model):
    __tablename__ = 'users'
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

    # def __init__(self, userId, day1a, day1b, day1c, day2a, day2b, day2c, day3a,
    #              day3b, day3c, day4a, day4b, day4c, day5a, day5b, day5c, day6a,
    #              day6b, day6c, day7a, day7b, day7c, day8a, day8b, day8c, day9a,
    #              day9b, day9c, day10a, day10b, day10c, day11a, day11b, day11c,
    #              day12a, day12b, day12c, day13a, day13b, day13c, day14a,
    #              day14b, day14c, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    #     self.userId = userId
    #     self.day1a = day1a
    #     self.day1b = day1b
    #     self.day1c = day1c
    #     self.day2a = day2a
    #     self.day2b = day2b
    #     self.day2c = day2c
    #     self.day3a = day3a
    #     self.day3b = day3b
    #     self.day3c = day3c
    #     self.day4a = day4a
    #     self.day4b = day4b
    #     self.day4c = day4c
    #     self.day5a = day5a
    #     self.day5b = day5b
    #     self.day5c = day5c
    #     self.day6a = day6a
    #     self.day6b = day6b
    #     self.day6c = day6c
    #     self.day7a = day7a
    #     self.day7b = day7b
    #     self.day7c = day7c
    #     self.day8a = day8a
    #     self.day8b = day8b
    #     self.day8c = day8c
    #     self.day9a = day9a
    #     self.day9b = day9b
    #     self.day9c = day9c
    #     self.day10a = day10a
    #     self.day10b = day10b
    #     self.day10c = day10c
    #     self.day11a = day11a
    #     self.day11b = day11b
    #     self.day11c = day11c
    #     self.day12a = day12a
    #     self.day12b = day12b
    #     self.day12c = day12c
    #     self.day13a = day13a
    #     self.day13b = day13b
    #     self.day13c = day13c
    #     self.day14a = day14a
    #     self.day14b = day14b
    #     self.day14c = day14c


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