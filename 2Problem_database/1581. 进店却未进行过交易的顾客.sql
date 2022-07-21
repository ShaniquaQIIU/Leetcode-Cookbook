--有一些顾客可能光顾了购物中心但没有进行交易。请你编写一个 SQL 查询，来查找这些顾客的 ID ，以及他们只光顾不交易的次数。
--返回以 任何顺序 排序的结果表。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/customer-who-visited-but-did-not-make-any-transactions

-- 2022-07-15
select customer_id, count(1) count_no_trans
from Visits  v
left join Transactions t using(visit_id)
where t.visit_id is null
group by customer_id;

-- 慢
SELECT customer_id,COUNT(1) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (
                    SELECT visit_id
                    FROM Transactions
                    GROUP BY visit_id)
GROUP BY customer_id;