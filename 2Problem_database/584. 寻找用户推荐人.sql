-- 写一个查询语句，返回一个客户列表，列表中客户的推荐人的编号都 不是 2。
-- 2022-07-08
-- 注意：作比较的时候，NUll会被过滤掉，因此需要单独罗列出来
select `name`
from customer
where referee_id is null or referee_id != 2;