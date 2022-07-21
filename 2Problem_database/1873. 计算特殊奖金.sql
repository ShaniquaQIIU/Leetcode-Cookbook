-- 写出一个SQL 查询语句，计算每个雇员的奖金。如果一个雇员的id是奇数并且他的名字不是以'M'开头，那么他的奖金是他工资的100%，否则奖金为0。
-- 返回的结果集请按照employee_id排序。
-- 来源：力扣（LeetCode）
-- 链接：https://leetcode.cn/problems/calculate-special-bonus

-- 2022-07-10
select employee_id,
if (employee_id%2=0 or name like 'M%', 0, salary) bonus
from Employees
order by employee_id;

-- AND LEFT(name,1)!='M'
-- and name not regexp('^M')


