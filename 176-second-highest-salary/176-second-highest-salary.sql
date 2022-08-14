# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from Employee
where Salary not in (select max(salary) from Employee )
