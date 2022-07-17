--编写一个SQL查询，报告2019年春季才售出的产品。即仅在2019-01-01至2019-03-31（含）之间出售的商品。
--以 任意顺序 返回结果表。

-- 2022-07-17
select p.product_id, product_name
from Product p
left join Sales s
on p.product_id = s.product_id
group by s.product_id
having min(sale_date) >= '2019-01-01' and max(sale_date) <='2019-03-31';

