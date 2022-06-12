create table student (
   ssn int,
   name varchar(50),
   major varchar(15),
   status varchar(15),
   primary key(ssn)
);


create table transcript (
   dcode varchar(15),
   cno int,
   ssn int,
   grade varchar(2),
   primary key(dcode, cno, ssn)
);



create table employee (
   employeeID varchar(2),
   employeeName varchar(20),
   departmentID varchar(20),
   salary int
);


create table department (
   departmentID varchar(20),
   departmentName varchar(50)
);