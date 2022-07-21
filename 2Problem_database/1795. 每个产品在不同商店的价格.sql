--请你重构 Products 表，查询每个产品在不同商店的价格，使得输出的格式变为(product_id, store, price) 。如果这一产品在商店里没有出售，则不输出这一行。
--输出结果表中的 顺序不作要求 。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/rearrange-products-table

-- 2022-07-11
select product_id, 'store1' as store, store1 as price
from Products where store1 is not null
union all
select product_id, 'store2' as store, store2 as price
from Products where store2 is not null
union all
select product_id, 'store3' as store, store3 as price
from Products where store3 is not null;
