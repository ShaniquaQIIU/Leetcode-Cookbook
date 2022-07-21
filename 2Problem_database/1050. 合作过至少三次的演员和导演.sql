--写一条SQL查询语句获取合作过至少三次的演员和导演的 id 对 (actor_id, director_id)

-- 2022-07-17
select actor_id, director_id
from ActorDirector
group by actor_id, director_id having count(1) >= 3;
