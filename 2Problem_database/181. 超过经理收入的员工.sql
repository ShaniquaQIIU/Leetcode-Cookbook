-- Employee 表包含所有员工，他们的经理也属于员工。每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。
-- 给定 Employee 表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。

select a.Name as Employee
from Employee a
where a.Salary > ( select  Salary
                   from Employee b
                   where a.ManagerId = b.Id  )

select a.Name as Employee
from Employee a ,Employee b
where a.ManagerId=b.Id AND a.Salary>b.Salary;