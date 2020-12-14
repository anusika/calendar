from createTable import create_connection
from insertAssignments import databaseFile
from getAssignments import get_assignments

def getTasks(connection, assignmentId):

    cmdCreate = "CREATE TABLE IF NOT EXISTS {} (taskName TEXT, taskStatus INT);".format("tasks" + str(assignmentId))
    cmdGet = "SELECT * from {}".format("tasks" + str(assignmentId))
    cur = connection.cursor()
    cur.execute(cmdCreate)
    cur.execute(cmdGet)
    tasks = cur.fetchall()
    connection.commit()
    return tasks
    

def main():
    connection = create_connection(databaseFile)
    assignments = get_assignments(connection)
    for assignment in assignments:
        tasks = getTasks(connection, assignment[3])
    connection.close()

if __name__ == '__main__':
    main()