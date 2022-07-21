--写出一个查询语句，找到所有 丢失信息 的雇员id。当满足下面一个条件时，就被认为是雇员的信息丢失：
--雇员的 姓名 丢失了，或者
--雇员的 薪水信息 丢失了，或者
--返回这些雇员的id  employee_id ， 从小到大排序 。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/employees-with-missing-information

-- 2022-07-11
select employee_id
from employees
where employee_id not in (select employee_id from salaries)
union
select employee_id
from salaries
where employee_id not in (select employee_id from employees)
order by employee_id;