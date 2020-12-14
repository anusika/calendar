import os
import sqlite3
from flask import Flask, request, render_template, url_for
from getAssignments import get_assignments,  updateAssignment, delete_assignmnent
from insertAssignments import reloadA, databaseFile, courses, insert_assignment, edit_assignment
from createTable import create_connection
import random
import datetime

app = Flask(__name__)

assignments = []

@app.route('/')
def hello_world():
    connection = create_connection(databaseFile)
    global assignments
    assignments = get_assignments(connection)
    connection.close()
    return render_template("index.html", data=assignments, courses = courses)

@app.route('/reload/', methods=['POST'])
def reload():
    connection = create_connection(databaseFile)
    reloadA(connection)
    global assignments
    assignments = get_assignments(connection)
    connection.close()
    return render_template("index.html", data=assignments, courses = courses)


@app.route('/toggle/', methods=['POST', "GET"])
def toggle():
    connection = create_connection(databaseFile)
    for names in request.form:
        assignment_code = names

    updateAssignment(connection, assignment_code, request.form[assignment_code])
    global assignments
    assignments = get_assignments(connection)
    connection.close()
    return render_template("index.html", data=assignments, courses = courses)

@app.route('/add/', methods=['POST', "GET"])
def addAssignment():
    data = request.form
    courseCode = data.get("courseCode")
    assignmentName = data.get("assignmentName")
    dueDate = data.get("dueDate")
    points = data.get("points")
    submitted = 0
    assignmentId = random.randint(1000,9999)

    dueDate= datetime.datetime.strptime(dueDate, "%Y-%m-%dT%H:%M")
    dueDate = dueDate.strftime('%Y-%m-%d %H:%M:00')

    for course in courses.keys():
        if courses[course] == int(courseCode):
            courseName = course

    connection = create_connection(databaseFile)

    insert_assignment(connection, [courseName, int(courseCode), assignmentName, int(assignmentId), dueDate, int(points), submitted])
    
    global assignments
    assignments = get_assignments(connection)

    connection.close()

    return render_template("index.html", data=assignments, courses = courses)    

@app.route('/delete/', methods=['POST', "GET"])
def delete():
    data = request.form
    assignmentCode = data.get("toDelete")

    connection = create_connection(databaseFile)
    delete_assignmnent(connection, assignmentCode)

    global assignments
    assignments = get_assignments(connection)

    connection.close()
    return render_template("index.html", data=assignments, courses = courses) 

@app.route('/edit/', methods=['POST', "GET"])
def edit():
    connection = create_connection(databaseFile)
    data = request.form

    courseCode = data.get("courseCode")
    assignmentName = data.get("assignmentName")
    dueDate = data.get("dueDate")
    points = data.get("points")
    submitted = data.get("submitStatus")
    assignmentId = data.get('assignmentId')
    try:
        dueDate= datetime.datetime.strptime(dueDate, "%Y-%m-%dT%H:%M:%S")
    except:
        dueDate= datetime.datetime.strptime(dueDate, "%Y-%m-%dT%H:%M")
    dueDate = dueDate.strftime('%Y-%m-%d %H:%M:00')


    for course in courses.keys():
        if courses[course] == int(courseCode):
            courseName = course

    edit_assignment(connection, [courseName, int(courseCode), assignmentName, int(assignmentId), dueDate, int(points), int(submitted)])
    
    global assignments
    assignments = get_assignments(connection)

    connection.close()
    return render_template("index.html", data=assignments, courses = courses) 