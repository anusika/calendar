import os
from canvasapi import Canvas
import datetime as dt
import pytz
from createTable import create_connection

databaseFile = os.path.abspath('db/assignments.db')
courses = {"2020 Fall - Engineering Co-op Assignments (2020W1)" : 68533, 
"CLST 105 003 2020W Greek and Roman Mythology" : 65390}

def create_canvas():
    TOKEN = os.environ.get('CANVAS_API_TOKEN')
    BASEURL = 'https://ubc.instructure.com'
    canvas = Canvas(BASEURL, TOKEN)

    return canvas

def insert_assignment(connection, assignment):
    
    cmdcheckExists = " SELECT * from assignments WHERE assignmentId = ?"

    cmdUpdate = "UPDATE assignments SET dueDate = ? WHERE assignmentId = ?"

    cmdInsert = """ INSERT INTO assignments(courseName, courseId, assignmentName, assignmentId, dueDate, points, submitted)
    VALUES(?, ?, ?, ?, ?, ?, ?)"""
    
    cur = connection.cursor()
    cur.execute(cmdcheckExists, [assignment[3]])
    assignments = cur.fetchall()

    if assignments:
        cur.execute(cmdUpdate, [assignment[4], assignment[3]] )
    else:
        cur.execute(cmdInsert, assignment)

    connection.commit()


def edit_assignment(connection, assignment):
    
    cmdReplace = """ REPLACE INTO assignments(courseName, courseId, assignmentName, assignmentId, dueDate, points, submitted)
    VALUES(?, ?, ?, ?, ?, ?, ?)"""
    
    cur = connection.cursor()
    cur.execute(cmdReplace, assignment)
    connection.commit()



def reloadA(connection):
    canvas = create_canvas()

    for courseId in courses.values():

        course = canvas.get_course(courseId)
        courseName = course.name
        assignments = course.get_assignments()


        for assignment in assignments:
            aid = int(assignment.id)
            due_at = assignment.due_at
            points = int(assignment.points_possible)
            name = assignment.name
            submitted = int(assignment.has_submitted_submissions)
            
            # convert UTC to PST
            if due_at:
                due = due_at[:-1]
                iso = (dt.datetime.fromisoformat(due).replace(tzinfo=pytz.UTC))
                time = iso.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:00')
                due_at = time
            insert_assignment(connection, (courseName, courseId, name, aid, due_at, points, submitted))
