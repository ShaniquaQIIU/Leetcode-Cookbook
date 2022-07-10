--写一条SQL 语句，查询患有 I 类糖尿病的患者ID （patient_id）、患者姓名（patient_name）以及其患有的所有疾病代码（conditions）。I 类糖尿病的代码总是包含前缀 DIAB1 。
--按 任意顺序 返回结果表。
--来源：力扣（LeetCode）
--链接：https://leetcode.cn/problems/patients-with-a-condition

-- 2022-07-10
select patient_id,patient_name,conditions
from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%' ;
