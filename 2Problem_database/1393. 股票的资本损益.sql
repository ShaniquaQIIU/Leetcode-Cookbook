--编写一个SQL查询来报告每支股票的资本损益。
--股票的资本损益是一次或多次买卖股票后的全部收益或损失。
--以任意顺序返回结果即可。

-- 2022-07-16
select stock_name,
 sum(if(operation='Sell', price, -price)) capital_gain_loss
from Stocks
group by stock_name;