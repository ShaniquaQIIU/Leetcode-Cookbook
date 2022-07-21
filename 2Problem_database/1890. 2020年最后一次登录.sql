--编写一个 SQL 查询，该查询可以获取在 2020 年登录过的所有用户的本年度 最后一次 登录时间。结果集 不 包含 2020 年没有登录过的用户。
--返回的结果集可以按 任意顺序 排列。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/the-latest-login-in-2020

-- 2022-07-16
select user_id, max(time_stamp) last_stamp
from Logins
where year(time_stamp) = 2020
group by user_id;
