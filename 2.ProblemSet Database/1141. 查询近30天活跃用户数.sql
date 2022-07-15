--请写SQL查询出截至 2019-07-27（包含2019-07-27），近 30 天的每日活跃用户数（当天只要有一条活动记录，即为活跃用户）。
--以 任意顺序 返回结果表。
--查询结果示例如下。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/user-activity-for-the-past-30-days-i

-- 2022-07-15
select activity_date as 'day', count(distinct user_id) active_users
from Activity
where activity_date between DATE_SUB('2019-07-27', interval 29 day )
 and DATE_SUB('2019-07-27', interval 0 day )
group by activity_date
order by activity_date;