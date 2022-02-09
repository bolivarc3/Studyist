import sqlite3
from datetime import datetime,timedelta
import re
import os
import requests
import urllib.parse
from flask import redirect, render_template, request, session
from functools import wraps



def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def connectdb(db):
    #input is name of db
    connect = sqlite3.connect("databases/" + db)
    cursor = connect.cursor()
    list = [cursor,connect]
    #returns db information
    return list;



def grabclasses():
    #grabs all the classes and converts it to an array
    dbinfo = connectdb("classes.db")
    coursecursor = dbinfo[0]
    courseconnect = dbinfo[1]
    coursecursor.execute("SELECT name FROM classes");
    coursesdb = coursecursor.fetchall()
    courses = []
    #converts all data into an array
    for i in range(len(coursesdb)):
        data = coursesdb[i][0]
        courses.append(data)
    return courses;


def checkclass(course, courses):
    availible = False
    for i in range(len(courses)):
        if course == courses[i]:
            availible = True
    if availible != True:
        return False;

def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        print("Valid Email")
        return("valid")

    else:
        print("Invalid Email")
        return("invalid")


def time_difference(postedtime,posteddate):
    now = datetime.now()
    nowdate = now.strftime("%d/%m/%Y")
    print("hey")

    posteddate = datetime.strptime(posteddate,"%d/%m/%y")

    print(nowdate)
    print(posteddate)
    print((abs(now - posteddate).days))

