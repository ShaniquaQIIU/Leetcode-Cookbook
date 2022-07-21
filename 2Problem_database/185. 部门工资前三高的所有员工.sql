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

-- 2022-02-17 跟我一个部门，且比我工资高的至多两人
select d.Name as Department,e.Name as Employee,e.Salary as Salary
from Employee e
left join Department d
on e.DepartmentId = d.Id
where e.Id in
(
    select e1.Id
    from Employee e1
    left join Employee e2
    on e1.DepartmentId = e2.DepartmentId and e1.Salary < e2.Salary
    group by e1.Id
    having count(distinct e2.Salary) <= 2
);