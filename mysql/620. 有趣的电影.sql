-- 编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级 rating 排列。
-- 2020-12-10
select  id , movie,description, rating
from cinema
where id%2 =1 and description != 'boring'
order by rating desc;

-- 用位运算 和 not 更快！
select  id , movie,description, rating
from cinema
where id&1 and not description = 'boring'
order by rating desc;