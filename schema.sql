CREATE TABLE assignments (
    courseName TEXT,
    courseId INT,
	assignmentName TEXT,
    assigmentId INT UNIQUE,
	dueDate TEXT,
	points INT,
    submitted INT
	
);