-- 例如上述 Employee 表，n = 2 时，应返回第二高的薪水 200。如果不存在第 n 高的薪水，那么查询应返回 null。

-- 2020-12-05 做题
-- 沿用176的思路
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N-1;
  RETURN (
      select
        IFNULL( (select Salary from Employee
        group by Salary
        order by Salary desc
        limit N,1 ), null
    ) as SecondHighestSalary
  );
END