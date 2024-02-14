create database shoppingmall;

use shoppingmall;

select * from user_table ut ;

# 2-1
select ut.userName, bt.prodName , ut.addr,concat(ut.mobile1, ut.mobile2) '연락처'
from user_table ut join buy_table bt
on ut.userID = bt.userID;

# 2-2
select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2)
from user_table ut join buy_table bt
on ut.userID = bt.userID
where ut.userID = 'KYM';

# 2-3
select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2) as '연락'
from user_table ut join buy_table bt
on ut.userID = bt.userID
order by ut.userID ;

# 2-4
select distinct ut.userID,ut.userName, ut.addr
from user_table ut join buy_table bt
on ut.userID = bt.userID
order by ut.userID ;

# 2-5
select ut.userID, ut.userName, ut.addr, concat(ut.mobile1, ut.mobile2) as '연락'
from user_table ut join buy_table bt
on ut.userID = bt.userID
where addr in ('경북', '경남')
order by ut.userID ;