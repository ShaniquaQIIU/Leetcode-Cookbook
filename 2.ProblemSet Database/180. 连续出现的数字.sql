-- 编写一个 SQL 查询，查找所有至少连续出现三次的数字。

select a.Num as ConsecutiveNums
from Logs as a, Logs as b, Logs as c
where a.Num=b.Num and b.Num=c.Num
      and a.id=b.id-1 and b.id=c.id-1
group by a.Num;


