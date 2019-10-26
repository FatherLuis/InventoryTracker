

CREATE TABLE [Person] (
    [PersonID] INTEGER PRIMARY KEY AUTOINCREMENT,
    [FirstName] TEXT  NOT NULL ,
    [LastName] TEXT  NOT NULL 
);

CREATE TABLE [Phone] (
    [PhoneID] INTEGER  PRIMARY KEY AUTOINCREMENT,
    [PersonID] INTEGER  NOT NULL ,
    [PhoneType] TEXT  NOT NULL ,
    [PhoneNum] INTEGER  NOT NULL 
);

CREATE TABLE [Email] (
    [EmailID] INTEGER  PRIMARY KEY AUTOINCREMENT ,
    [PersonID] INTEGER  NOT NULL ,
    [EmailAddress] TEXT  NOT NULL
);

CREATE TABLE [Course] (
    [CourseID] INTEGER  PRIMARY KEY AUTOINCREMENT ,
    [CourseName] TEXT  NOT NULL 
);

CREATE TABLE [Professor] (
    [ProfessorID] INTEGER  PRIMARY KEY AUTOINCREMENT ,
    [PersonID] INTEGER  NOT NULL 
);

CREATE TABLE [Semester] (
    [SemesterID] INTEGER  PRIMARY KEY AUTOINCREMENT ,
    [SemesterName] TEXT  NOT NULL 
);

CREATE TABLE [Student] (
    [StudentID] INTEGER Primary Key NOT NULL,
    [PersonID] INTEGER  NOT NULL 
);

CREATE TABLE [Contract] (
	[ContractID] INTEGER PRIMARY KEY AUTOINCREMENT,
    [StudentID] INTEGER  NOT NULL,
    [CourseID] INTEGER  NOT NULL ,
    [SemesterID] INTEGER  NOT NULL ,
    [ProfessorID] INTEGER  NOT NULL ,
    [StartDate] TEXT  NOT NULL ,
    [EndDate] TEXT  NOT NULL ,
    [isActive] INTEGER  NOT NULL 
);


CREATE TABLE [Login] (
    [LoginID] INTEGER  PRIMARY KEY AUTOINCREMENT ,
    [Username] TEXT  NOT NULL ,
    [Password] TEXT  NOT NULL 
);
