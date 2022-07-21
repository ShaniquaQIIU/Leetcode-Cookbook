--写一段 SQL , 报告每个用户的旅行距离。
--返回的结果表单，以 travelled_distance 降序排列 ，如果有两个或者更多的用户旅行了相同的距离, 那么再以 name 升序排列 。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/top-travellers

-- 2022-07-16
select name,
    if(travelled_distance is null, 0, travelled_distance) travelled_distance
from Users u
left join
    (  select user_id, sum(distance) travelled_distance
       from Rides
       group by user_id ) a
on u.id = a.user_id
order by travelled_distance desc, name asc;
