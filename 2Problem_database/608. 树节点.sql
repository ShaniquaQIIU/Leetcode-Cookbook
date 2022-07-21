--树中每个节点属于以下三种类型之一：
--叶子：如果这个节点没有任何孩子节点。
--根：如果这个节点是整棵树的根，即没有父节点。
--内部节点：如果这个节点既不是叶子节点也不是根节点。
--写一个查询语句，输出所有节点的编号和节点的类型，并将结果按照节点编号排序
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/tree-node

-- 2022-07-11
select
    id,
    case when p_id is null then "Root"
         when id not in (select p_id from tree) then "Leaf"
         else "Inner"
    end as Type
from tree;


select id, 'Root' as type
from tree
where p_id is null
union
select id, 'Leaf' as type
from tree
where p_id is not null and id not in (select distinct p_id from tree where p_id is not null)
union
select id, 'Inner' as type
from tree
where p_id is not null and id in (select distinct p_id from tree where p_id is not null)
order by id;

