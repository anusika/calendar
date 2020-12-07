import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    # connect to a sqlite3 database
    conn = None
    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn

createAssignmentsTableCmd = """CREATE TABLE assignments (
    courseName TEXT,
    courseId INT,
	assignmentName TEXT,
    assigmentId INT UNIQUE,
	dueDate TEXT,
	points INT,
    submitted INT
	
); """


def create_table(conn, createCmd):
    # create sqlit3 table 

    try:
        c = conn.cursor()
        c.execute(createCmd)
    except Error as e:
        print(e)


def main():
    connection = create_connection("assignments.db")

    if connection:
        create_table(connection, createAssignmentsTableCmd)
        connection.close()



if __name__ == '__main__':
    main()