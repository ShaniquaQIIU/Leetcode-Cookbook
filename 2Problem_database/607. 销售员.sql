--编写一个SQL查询，报告没有任何与名为 “RED” 的公司相关的订单的所有销售人员的姓名。
--以 任意顺序 返回结果表。

-- 2022-07-15
select `name`
from SalesPerson
where sales_id not in (
    select sales_id
    from Orders o, Company c
    where o.com_id = c.com_id and c.`name` = 'RED'
);