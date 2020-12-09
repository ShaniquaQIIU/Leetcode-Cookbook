-- 编写一个 SQL 查询，找出每个部门获得前三高工资的所有员工。例如，根据上述给定的表，查询结果应返回：
-- 2020-12-09 排名连续
select s.Department, s.Employee,  s.Salary
from
(
    select d.`Name` Department,
    e.`Name` as Employee,
    Salary,
    dense_rank() over(partition by e.DEPARTMENTID order by e.Salary desc) rn
    from Employee  e
    join  Department d
    on e.DepartmentId = d.Id
) s
where s.rn <= 3;