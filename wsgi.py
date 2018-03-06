from flask import Flask, render_template, request
application = Flask(__name__)

@application.route('/')
def hello():
    return render_template('hello.html')

@application.route('http://drug-education-project-kbaek11.cloudapps.unc.edu/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == "__main__":
    application.run(debug = True)