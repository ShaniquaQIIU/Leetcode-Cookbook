-- 编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 id 。
-- 2020-12-09
select w1.id
from Weather w1, Weather w2
where w1.Temperature > w2.Temperature
    and subdate(w1.recordDate, interval 1 day) = w2.recordDate;