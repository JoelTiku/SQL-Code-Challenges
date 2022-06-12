-- Find CS (major = ‘CS’) students (ssn, name, major, status) who received the
-- grade in at least one course according to transcript. Order the result by student ssn.
-- query 1
drop view query1 ;
create view query1 as
select distinct s.*
from student s
where s.major = 'CS' and 
	  s.ssn in (
         select distinct s.ssn
         from student s
         inner join transcript t on s.ssn = t.ssn
         where t.grade = 'A'
);


-- Find CS (major = ‘CS’) students (ssn, name, major, status) who received the
-- grade A in at least two courses according to transcripts. Order the result by
-- student ssn.
--  query 2
drop view query2 ;
create view query2 as
select distinct s.*
from student s
inner join transcript t on s.ssn = t.ssn
cross join transcript t1
where s.major = 'CS' and 
      t.grade = 'A' and t1.grade = 'A' and
			t1.ssn = t.ssn and s.ssn = t1.ssn and 
      t.cno != t1.cno;


-- Find CS (major = ‘CS’) students (ssn, name, major, status) who received the
-- grade A in all CS courses (dcode = ‘CS’) they have taken (according to transcripts), 
-- i.e., have not received a non-A grade in a CS course. Order the result by student ssn.
-- query 3
drop view query3 ;
create view query3 as
select distinct s.*
from student s
where s.major = 'CS' and 
s.ssn not in (
         select distinct s.ssn
         from student s
         left join transcript t on s.ssn = t.ssn
         where t.dcode = 'CS' and (t.grade is null or t.grade in ('B', 'C', 'D', 'F'))
);




-- Find employees that have the same name (duplicate values in employee name)
-- query 4
drop view query4 ;
create view query4 as
select employeeName
from employee
group by employeeName
having count(*) >= 2
order by employeeID




-- Return department name where average employee salary is greater than $80,000 
-- query 5
drop view query5 ;
create view query5 as
select departmentName, avg(e.salary)
from employee e
inner join department d
on e.departmentID = d.departmentID
group by d.departmentID
having avg(e.salary) > 80000
order by d.departmentID