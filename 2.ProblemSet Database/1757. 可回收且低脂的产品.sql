-- 写出 SQL 语句，查找既是低脂又是可回收的产品编号。
-- 返回结果 无顺序要求 。

-- 2022-07-08
select product_id
from Products
where low_fats = 'Y' and recyclable = 'Y';


select product_id
from Products
where (low_fats , recyclable) = ('Y', 'Y');