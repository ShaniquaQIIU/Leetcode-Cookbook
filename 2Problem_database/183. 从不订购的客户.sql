-- 某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

-- join用多了第一反应
select `Name` as Customers
from Customers c
left join Orders o
on  c.Id = o.CustomerId
where o.Id is null;

-- 第二反应是 not exists
select `Name` as Customers
from Customers c
where not exists (select 1 from Orders o where c.Id = o.CustomerId);

-- 此题还是not in好
select `Name` as Customers
from Customers c
where c.Id not in (select distinct CustomerId from Orders o );