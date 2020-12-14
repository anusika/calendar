from createTable import create_connection
from insertAssignments import databaseFile


def get_assignments(connection):
    cmdGet = "SELECT * FROM assignments ORDER BY submitted ASC, dueDate ASC NULLS LAST;"
    cur = connection.cursor()
    cur.execute(cmdGet)
    assignments = cur.fetchall()
    return assignments


def updateAssignment(connection, assignment, value):
    cmdUpdate = """
    UPDATE assignments
    SET submitted = ?
     WHERE assignmentId = ?"""
    cur = connection.cursor()

    if value == "1":
        value = "0"
    else:
        value = "1"

    cur.execute(cmdUpdate, [value, assignment])
    connection.commit()

    cmdGet = "SELECT * FROM assignments WHERE assignmentId = ?;"
    cur.execute(cmdGet, [assignment])


def delete_assignmnent(connection, assignmentId):

    cmdDelete = "DELETE FROM assignments WHERE assignmentId = ?;"
    cur = connection.cursor()
    cur.execute(cmdDelete, [assignmentId])
    connection.commit()