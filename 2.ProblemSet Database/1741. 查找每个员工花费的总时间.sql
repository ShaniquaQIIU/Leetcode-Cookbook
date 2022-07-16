--编写一个SQL查询以计算每位员工每天在办公室花费的总时间（以分钟为单位）。 请注意，在一天之内，同一员工是可以多次进入和离开办公室的。 在办公室里一次进出所花费的时间为out_time 减去 in_time。
--返回结果表单的顺序无要求。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/find-total-time-spent-by-each-employee

-- 2022-07-16
select event_day as 'day', emp_id, sum(out_time-in_time) total_time
from Employees
group by event_day, emp_id;