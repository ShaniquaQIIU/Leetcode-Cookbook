-- 编写一个 SQL 查询，找出每个部门工资最高的员工。对于上述表，您的 SQL 查询应返回以下行（行的顺序无关紧要）。
-- Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。
-- Department 表包含公司所有部门的信息。

-- 2020-12-09
select d.`Name` as Department,  e.`Name` as Employee,  e.Salary as Salary
from
(
    select `Name`, Salary, DepartmentId
    from Employee  e1
    where Salary = ( select MAX(Salary) from Employee  e2 where e1.DepartmentId = e2.DepartmentId )
) e
join  Department d
on e.DepartmentId = d.Id;

-- 窗口函数，注意同排名的情况
select s.Department, s.Employee,  s.Salary
from
(
    select d.`Name` Department,
    e.`Name` as Employee,
    Salary,
    rank() over(partition by e.DEPARTMENTID order by e.Salary desc) rn
    from Employee  e
    join  Department d
    on e.DepartmentId = d.Id
) s
where s.rn = 1;