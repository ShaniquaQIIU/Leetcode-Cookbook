--编写一个 SQL 查询来查找每个日期、销售的不同产品的数量及其名称。
--每个日期的销售产品名称应按词典序排列。
--返回按 sell_date 排序的结果表。

-- 2022-07-10
select sell_date,
    count(distinct product) num_sold,
    group_concat(distinct product order by product separator ',') products
from Activities
group by sell_date;
