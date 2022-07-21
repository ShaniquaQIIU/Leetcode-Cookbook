--请写出一条SQL语句以查询每个用户的注册日期和在 2019 年作为买家的订单总数。
--以 任意顺序 返回结果表。

-- 2022-07-16
select user_id buyer_id, join_date,
 if(cnt is null, 0, cnt) orders_in_2019
from Users u
left join
(
    select buyer_id, count(order_date) cnt
    from Orders
    where year(order_date) = 2019
    group by buyer_id
) a
on u.user_id = a.buyer_id;


select user_id buyer_id,
    join_date,
    ifnull(count(order_id),0) as orders_in_2019
from Users u
left join Orders o
on u.user_id = o.buyer_id and year(o.order_date) = "2019"
group by u.user_id;