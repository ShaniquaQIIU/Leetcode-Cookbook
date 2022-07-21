--写一个 SQL,  报告余额高于 10000 的所有用户的名字和余额. 账户的余额等于包含该账户的所有交易的总和.
--返回结果表单没有顺序要求.

-- 2022-07-17
select name, sum(amount) balance
from Users u, Transactions t
where u.account = t.account
group by u.account having sum(amount) > 10000;