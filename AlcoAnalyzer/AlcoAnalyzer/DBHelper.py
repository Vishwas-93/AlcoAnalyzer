import sqlite3
from builtins import print
import pandas as pd



def createusertable():
    db = sqlite3.connect('alcoanalyzer.db')
    cursor = db.cursor()
    cursor.execute('create table if not exists alcoanalyzer (fname text, lname text, email text, password text, age integer, '
                   'sex text, medu integer, mjob integer, fjob integer, reason text, studytime integer, '
                   'schoolsup integer, goout integer, higher text, Dalc integer, Walc integer,famsup text, isLogged text)')
    db.commit()
    db.close()

def enteruser(fname, lname, email, pwd, age, sex, medu, mjob, fjob, reason, studytime, schoolsup, goout, higher, dalc, walc, famsup, isLogged):
    db = sqlite3.connect('alcoanalyzer.db')
    cursor = db.cursor()
    try:
        sql = "INSERT into alcoanalyzer VALUES"+"( '"+fname+"' , '"+lname+"' , '"+email+"' , '"+pwd+"' , '"+age+"' , '"+sex+"' , '"+medu+"' , '"+mjob+"' , '"+fjob+"' , '"+reason+"' , '" \
        +studytime + "' , '"+schoolsup+"' , '"+goout+"' , '"+higher+"' , '"+dalc+"' , '"+walc+"' , '"+famsup+"' , '"+isLogged+"' )"
        sql =sql.replace("@","_")
        print(sql)
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except Exception as e:
        print(str(e))
        db.close()
        return -1


def getcredentials(email_):
    db = sqlite3.connect('alcoanalyzer.db')
    cursor = db.cursor()

    try:
        sql = "SELECT email, password from alcoanalyzer where email = '"+email_+"'"
        print(sql)
        cur = cursor.execute(sql)
        row = cur.fetchone()
        print(row)
        db.close()
        return row
    except Exception as e:
        print(str(e))
        db.close()
        return -1

def setLoggedIn(email, val):
    db = sqlite3.connect('alcoanalyzer.db')
    cur = db.cursor()
    val = str(val)
    sql = "UPDATE alcoanalyzer SET isLogged = '"+val+"' where email = '"+email+"'"
    print(sql)
    cur.execute(sql)
    cur.execute('Select * from alcoanalyzer')
    rows = cur.fetchall()
    print(rows)
    db.close()




def getdetails(email):
    db = sqlite3.connect('alcoanalyzer.db')
    cursor = db.cursor()
    sql = "SELECT fname, lname, email, password, age, sex, medu, mjob, fjob, reason, studytime, schoolsup, goout, higher, Dalc, Walc, famsup from alcoanalyzer where email = '"+email+"'"
    cur = cursor.execute(sql)
    row = cur.fetchone()
    db.close()
    return row


def updateprofile(email_param, fname, lname, email_, pwd, age, sex, medu, mjob, fjob, reason, studytime, schoolsup, goout, higher, dalc, walc, famsup):
    db = sqlite3.connect('alcoanalyzer.db')
    cursor = db.cursor()
    sql = "UPDATE alcoanalyzer SET fname = '"+fname+"', lname = '"+lname+"', age = '"+age+"', sex = '"+sex+"', medu = '"+medu+"', mjob='"+mjob+"'," \
                                    "fjob = '"+fjob+"', reason = '"+reason+"', studytime = '"+studytime+"', schoolsup = '"+schoolsup+"', goout = '"+goout+"'," \
                                    " higher = '"+higher+"', dalc = '"+dalc+"', walc = '"+walc+"', famsup='"+famsup+"' WHERE email = '"+email_param+"'"
    cursor.execute(sql)
    db.commit()
    db.close()


def getalldetails(email):
    db = sqlite3.connect('alcoanalyzer.db')
    sql = "Select * from alcoanalyzer where email = '"+email+"'"
    print(sql);
    rows =pd.read_sql_query(sql, db)
    db.close()
    return rows
    # cur.execute(sql)
    # rows = cur.fetchone()
    # db.close()
    # return rows


def getdalcoclasscount(val):
    val = str(val)
    db = sqlite3.connect('alcoanalyzer.db')
    cur = db.cursor()
    sql = "Select count(*) as num from alcoanalyzer where dalc = '"+val+"'"
    print(sql)
    cur.execute(sql)
    dalc_count = cur.fetchone()
    db.close()
    return dalc_count


def getwalcoclasscount(val):
    val = str(val)
    db = sqlite3.connect('alcoanalyzer.db')
    cur = db.cursor()
    sql = "Select count(*) as num from alcoanalyzer where walc = '" + val + "'"
    cur.execute(sql)
    walc_count = cur.fetchone()
    db.close()
    return walc_count


def getpresentuseralcohol(email):
    db = sqlite3.connect('alcoanalyzer.db')
    cur = db.cursor()
    sql = "Select dalc, walc from alcoanalyzer where email = '"+email+"'"
    cur.execute(sql)
    alco_data = cur.fetchone()
    db.close()
    return alco_data

def getsuggestiondata(email):
    db = sqlite3.connect('alcoanalyzer.db')
    cur = db.cursor()
    sql = "select dalc, walc, studytime, schoolsup, goout from alcoanalyzer where email = '"+email+"'"
    cur.execute(sql)
    suggestionsdata = cur.fetchone()
    db.close()
    return suggestionsdata