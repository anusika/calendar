CREATE TABLE assignments (
    courseName TEXT,
    courseId INT,
	assignmentName TEXT,
    assignmentId INT UNIQUE,
	dueDate TEXT,
	points INT,
    submitted INT
	
);