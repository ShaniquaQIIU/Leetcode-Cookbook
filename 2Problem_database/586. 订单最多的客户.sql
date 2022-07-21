--编写一个SQL查询，为下了 最多订单 的客户查找 customer_number 。
--测试用例生成后， 恰好有一个客户 比任何其他客户下了更多的订单。

-- 2022-07-16
select customer_number
from
(select customer_number, count(order_number) cnt
from Orders
group by customer_number
order by count(order_number) desc) a
limit 1;


select customer_number
from (
	select
		customer_number,
		dense_rank() over(order by count(*) desc) as rn
	from orders
    group by customer_number
) temp
where rn = 1;