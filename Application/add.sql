DELETE FROM [Semester];
DELETE FROM [Course];
DELETE FROM [Person];
DELETE FROM [Professor];


INSERT INTO [Semester] (SemesterName) VALUES ('Fall 2019');
INSERT INTO [Semester] (SemesterName) VALUES ('Spring 2020');

INSERT INTO [Course] (CourseName) VALUES ('Math 1314');
INSERT INTO [Course] (CourseName) VALUES ('Math 1332');
INSERT INTO [Course] (CourseName) VALUES ('Math 1342');


INSERT INTO [Person] (FirstName,LastName) VALUES ('Professor','One');
INSERT INTO [Professor] (PersonID) SELECT [PersonID] FROM [Person] WHERE [FirstName] = 'Professor' AND [LastName]='One';

INSERT INTO [Person] (FirstName,LastName) VALUES ('Professor','Two');
INSERT INTO [Professor] (PersonID) SELECT [PersonID] FROM [Person] WHERE [FirstName] = 'Professor' AND [LastName]='Two';

