-- 编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。
-- 2020-12-09
delete p1
from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id;

-- 注意删除和查询不直接使用同一张表，需嵌套查询一层
-- You can't specify target table for update in FROM clause
delete
from Person
where Id not in (
    select tmp.id
    from (select min(Id) id from Person p1 group by Email) tmp
) ;