--请编写一条 SQL 查询以找出所有浏览过自己文章的作者，结果按照 id 升序排列。
--请注意，同一人的 author_id 和 viewer_id 是相同的。

-- 2022-07-15
select author_id as 'id'
from Views
where author_id = viewer_id
group by author_id
order by author_id asc;