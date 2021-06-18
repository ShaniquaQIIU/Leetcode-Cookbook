-- 写一段 SQL 语句查出 2013年10月1日 至 2013年10月3日 期间非禁止用户的取消率。
-- 基于上表，你的 SQL 语句应返回如下结果，取消率（Cancellation Rate）保留两位小数。
-- 2020-12-13
select t.Request_at as 'Day',
round(sum(if(t.Status != 'completed', 1 ,0))/count(t.id), 2) as 'Cancellation Rate'
from Trips t
left join Users u
on t.Client_Id = u.Users_Id
where u.Role = 'client'
    and t.Request_at between '2013-10-01' and '2013-10-03'
    and u.Banned ='No'
group by t.Request_at
order by t.Request_at;