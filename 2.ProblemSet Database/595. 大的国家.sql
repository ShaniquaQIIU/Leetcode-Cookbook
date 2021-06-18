-- 如果一个国家的面积超过 300 万平方公里，或者人口超过 2500 万，那么这个国家就是大国家。
-- 编写一个 SQL 查询，输出表中所有大国家的名称、人口和面积。

-- 2020-12-10
select  `name`, population, `area`
from World
where population > 25000000 or `area` > 3000000;


select w.name,w.population,w.area
from world w
where w.area>3000000
union
select w.name,w.population,w.area
from world w
where w.population>25000000;
