-- 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
-- 例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

-- 2020-12-05 做题
-- Write your MySQL query statement below
select
IFNULL( (select Salary from Employee
    group by Salary
    order by Salary desc
    limit 1,1 ), null
) as SecondHighestSalary;

-- 这个效率更高
select max(Salary) as SecondHighestSalary
from Employee
where Salary < ( select max(Salary) from Employee);
