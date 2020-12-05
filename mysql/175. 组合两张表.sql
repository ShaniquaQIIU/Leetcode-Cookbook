-- 编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供person 的以下信息：
-- FirstName, LastName, City, State

-- 2020-12-05 做题
-- Write your MySQL query statement below
select FirstName, LastName, City, State
from Person p
left join Address a
on p.PersonId = a.PersonId;

SELECT FirstName, LastName, City, State
FROM Person p
LEFT JOIN Address USING(PersonId);