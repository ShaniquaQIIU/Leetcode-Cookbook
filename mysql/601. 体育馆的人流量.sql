-- 编写一个 SQL 查询以找出每行的人数大于或等于 100 且 id 连续的三行或更多行记录。
-- 返回按 visit_date 升序排列的结果表。
-- 2020-12-13
select distinct s1.*
from Stadium s1, Stadium s2, Stadium s3
where s1.people >= 100 and s2.people >= 100 and s3.people >= 100
    and ( ( s1.id = s2.id-1 and s2.id = s3.id-1 )
     or ( s1.id = s2.id-1 and s3.id = s1.id-1 )
     or ( s1.id = s2.id+1 and s2.id = s3.id+1 )
    )
order by s1.visit_date;