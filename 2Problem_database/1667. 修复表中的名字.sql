--编写一个 SQL 查询来修复名字，使得只有第一个字符是大写的，其余都是小写的。
--返回按 user_id 排序的结果表。

-- 2022-07-10
select user_id,
  concat(upper(left(name, 1)), lower(substring(name, 2))) as `name`
from Users
order by user_id;
