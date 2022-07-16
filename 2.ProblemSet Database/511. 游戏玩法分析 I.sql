--写一条 SQL 查询语句获取每位玩家 第一次登陆平台的日期。

-- 2022-07-16
select player_id, min(event_date) first_login
from Activity
group by player_id;