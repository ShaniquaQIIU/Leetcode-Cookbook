--写出 SQL 语句，对于每一个用户，返回该用户的关注者数量。
--按 user_id 的顺序返回结果表。

-- 2022-07-16
select user_id, count(follower_id) followers_count
from Followers
group by user_id
order by user_id;
