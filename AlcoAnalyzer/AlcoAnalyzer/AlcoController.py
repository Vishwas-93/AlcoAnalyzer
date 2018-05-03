from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import flask
import DBHelper as dbh
# import AlcoAnalyzer.Data_Preprocess as dp
import Classification as cl
import json
import TestModel as tmg1
import TestModel_G2 as tmg2
import TestModel_G3 as tmg3
import pandas as pd
import numpy as np

app = Flask(__name__)
applicationdata = []


@app.route('/')
def index():
    dbh.createusertable()
    return render_template("login.html")


@app.route('/signUp', methods=['POST', 'GET'])
def signup():
    if request.method =='POST':
        data = request.form
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        pwd = data['pwd']
        age = data['age']
        sex = data['sex']
        medu = data['medu']
        mjob = data['mjob']
        fjob = data['fjob']
        reason = data['reason']
        studytime = data['studytime']
        schoolsup = data['schoolsup']
        goout = data['goout']
        higher = data['higher']
        dalc = data['dalc']
        walc = data['walc']
        famsup = data['famsup']
        isLogged = '1'
        email_ = email.replace("@", "_")
        dbh.enteruser(fname, lname, email_, pwd, age, sex, medu, mjob, fjob, reason, studytime, schoolsup, goout, higher, dalc, walc, famsup, isLogged)
        applicationdata.append(email_)
        applicationdata.append(isLogged)
        print(applicationdata)
        return redirect(url_for('check'))
    else:
        return render_template('signup.html')


@app.route('/signin', methods=['GET'])
def signin():
    email = request.args.get('email')
    pwd = request.args.get('pwd')
    email_ = email.replace("@", "_")
    result = dbh.getcredentials(email_)
    try:
        if result[0] == email_:
            if result[1] == pwd:
                print('Welcome! You are logged in!')
                isLogged = '1'
                dbh.setLoggedIn(email_, isLogged)
                applicationdata.append(email_)
                applicationdata.append(isLogged)
                # print(applicationdata)
                return 'valid credentials'
            else:
                print('Invalid Password!')
                return 'invalid password'
        else:
            print('Invalid Email')
            return 'invalid email'
    except Exception as e:
        print(e)
        return 'something went wrong'
#


@app.route('/dashboard')
def check():
    return render_template('dashboard.html')
#


@app.route('/logout', methods=['GET'])
def logout():
    dbh.setLoggedIn(applicationdata[0], 0)
    del applicationdata[:]
    return 'logged out'


@app.route('/success')
def success():
   return 'Success'


@app.route('/getprofiledetails', methods=['GET'])
def getdetails():
    appdat = applicationdata[0]
    result = dbh.getdetails(applicationdata[0])
    print(result)
    json_res = json.dumps(result)
    return json_res


@app.route('/editprofile')
def getprofile():
    return render_template('editprofile.html')


@app.route('/updateprofile', methods=['POST'])
def updateprofile():
    email_param = applicationdata[0]
    try:
        if request.method =='POST':
            data = request.form
            fname = data['fname']
            lname = data['lname']
            email = data['email']
            pwd = data['pwd']
            age = data['age']
            sex = data['sex']
            medu = data['medu']
            mjob = data['mjob']
            fjob = data['fjob']
            reason = data['reason']
            studytime = data['studytime']
            schoolsup = data['schoolsup']
            goout = data['goout']
            higher = data['higher']
            dalc = data['dalc']
            walc = data['walc']
            famsup = data['famsup']
            email_ = email.replace("@", "_")
            dbh.updateprofile(email_param, fname, lname, email_, pwd, age, sex, medu, mjob, fjob, reason, studytime, schoolsup, goout, higher, dalc, walc, famsup)
        return 'updated'
    except Exception as e:
        print(e)
        return 'not updated'


@app.route('/getanalyzeddata', methods=['GET'])
def getanalyzeddata():
    email_ = applicationdata[0]
    rows = dbh.getalldetails(email_)
    rows = rows.drop(columns=['fname', 'lname', 'email', 'password', 'isLogged'])
    grade1 = tmg1.predictGradeOne(rows)
    # print(grade1)
    grade = grade1
    grade_final = {}
    grade_final['grade'] = np.ceil(grade)
    grade_json = json.dumps(grade_final)
    print(grade_json)
    return grade_json


@app.route('/getanalyzeddata2', methods=['GET'])
def getanalyzeddata2():
    email_ = applicationdata[0]
    data = request.args.get('exam1')
    exam1 = data
    rows = dbh.getalldetails(email_)
    rows.insert(loc=len(rows), column='g1', value=exam1)
    rows = rows.drop(columns=['fname', 'lname', 'email', 'password', 'isLogged'])
    grade2 = tmg2.predictGradeTwo(rows)
    grade = grade2
    grade_final = {}
    grade_final['grade'] = np.ceil(grade)
    grade_json = json.dumps(grade_final)
    return grade_json

@app.route('/getanalyzeddata3', methods=['GET'])
def getanalyzeddata3():
    email_ = applicationdata[0]
    exam1 = request.args.get('exam1')
    exam2 = request.args.get('exam2')
    rows = dbh.getalldetails(email_)
    rows.insert(loc=len(rows), column='g1', value=exam1)
    rows.insert(loc=len(rows), column='g2', value=exam2)
    rows = rows.drop(columns=['fname', 'lname', 'email', 'password', 'isLogged'])
    grade3 = tmg3.predictGradeThree(rows)
    grade = grade3
    grade_final = {}
    grade_ceil = np.ceil(grade)
    grade_final['grade'] = 20 if grade_ceil>20 else grade_ceil
    grade_json = json.dumps(grade_final)
    return grade_json


@app.route('/getdalcodata', methods=['GET'])
def getdalcodata():
    dalccount = cl.getdalccount()
    dalccount_json = json.dumps(dalccount)
    return dalccount_json

@app.route('/getwalcdata', methods=['GET'])
def getwalcodata():
    walccount = cl.getwalccount()
    walc_data_json = json.dumps(walccount)
    print(walc_data_json)
    return walc_data_json
#
@app.route('/getuseralcodata', methods=['GET'])
def getuseralcodata():
    email_ = applicationdata[0]
    alco_data = dbh.getpresentuseralcohol(email_)
    user_alco_data = {}
    user_alco_data['user_dalc'] = alco_data[0]
    user_alco_data['user_walc'] = alco_data[1]
    user_alco_json = json.dumps(user_alco_data)
    print(user_alco_json)
    return user_alco_json

@app.route('/getalldata', methods=['GET'])
def getalldata():
    email = applicationdata[0]
    rows = dbh.getalldetails(email)
    print('--------------------')
    print(rows)
    return 'data1'

@app.route('/getsuggestions', methods=['GET'])
def getsuggestions():
    exam = request.args.get('exam')
    email = applicationdata[0]
    suggestiondata = dbh.getsuggestiondata(email)
    dalc = suggestiondata[0]
    walc = suggestiondata[1]
    studytime = suggestiondata[2]
    schoolsup = suggestiondata[3]
    goout = suggestiondata[4]
    suggetsions = []
    if int(exam) < 10:
        happy = "You are doing great!! You might still want to consider the following."
        suggetsions.append(happy)
        if dalc > 3:
            st1 = "Try to reduce your daily alcohol consumption"
            suggetsions.append(st1)
        if walc > 3:
            st2 = "Try to reduce your weekly alcohol consumption"
            suggetsions.append(st2)
        if studytime <= 2:
            st3 = "Increase you study time by quite a bit"
            suggetsions.append(st3)
        if schoolsup == "no":
            st4 = "Consider some tutoring in school"
            suggetsions.append(st4)
        if goout > 3:
            st5 = "Try not going out too much"
            suggetsions.append(st5)


    elif int(exam) < 15:
        happy = "You are doing great!! You might still want to consider the following."
        suggetsions.append(happy)
        if dalc > 3:
            st1 = "Try to reduce your daily alcohol consumption"
            suggetsions.append(st1)
        if walc > 3:
            st2 = "Try to reduce your weekly alcohol consumption"
            suggetsions.append(st2)
        if studytime <= 2:
            st3 = "Increase you study time by quite a bit"
            suggetsions.append(st3)
        if schoolsup == "no":
            st4 = "Consider some tutoring in school"
            suggetsions.append(st4)
        if goout > 3:
            st5 = "Try not going out too much"
            suggetsions.append(st5)

    else:
        happy = "You are doing great!! You might still want to consider the following."
        suggetsions.append(happy)
        if dalc > 3:
            st1 = "Try to reduce your daily alcohol consumption"
            suggetsions.append(st1)
        if walc > 3:
            st2 = "Try to reduce your weekly alcohol consumption"
            suggetsions.append(st2)
        if studytime <= 2:
            st3 = "Increase you study time by quite a bit"
            suggetsions.append(st3)
        if schoolsup == "no":
            st4 = "Consider some tutoring in school"
            suggetsions.append(st4)
        if goout > 3:
            st5 = "Try not going out too much"
            suggetsions.append(st5)
    suggestions = json.dumps(suggetsions)
    return suggestions


if __name__=="__main__":
    app.run()