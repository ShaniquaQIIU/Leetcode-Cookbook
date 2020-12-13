-- 改变相邻俩学生的座位。
-- 如果学生人数是奇数，则不需要改变最后一个同学的座位。

-- 2020-12-13
select
 if(id%2=0, id-1, if(id=(select max(id) from seat), id, id+1) ) as id,
 student
from seat
order by id;


-- 妙哉
select rank() over(order by (id-1)^1) as id,student
from seat;
