--写一条 SQL 语句，使得对于每一个 date_id 和 make_name，返回不同的 lead_id 以及不同的 partner_id 的数量。
--按 任意顺序 返回结果表。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/daily-leads-and-partners

-- 2022-07-16
select date_id, make_name,
    count(distinct lead_id) unique_leads, count(distinct partner_id) unique_partners
from DailySales
group by date_id, make_name;
