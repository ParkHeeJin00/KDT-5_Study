use test_db;
DROP TABLE IF EXISTS account;
# account 테이블 생성 (7장 p.188)
CREATE TABLE account
(account_id int,
acct_type varchar(20),
balance float);
INSERT INTO account (account_id, acct_type, balance)
VALUES (123, 'MONEY MARKET', 785.22),
(456, 'SAVINGS', 0.00),
(789, 'CHECKING', -324.22);

SELECT account_id, sign(balance), abs(balance) FROM account;

SELECT cast('2019-09-17 15:30:00' as datetime);

SELECT cast('2019-09-17' as date) date_field,
cast('108:17:57' as time) time_field;

SELECT cast('20190917153000' as datetime);

SELECT str_to_date('September 17, 2019', '%M %d, %Y') as return_date;

SELECT CURRENT_DATE(), CURRENT_TIME(), CURRENT_TIMESTAMP();

SELECT extract(year FROM '2019-09-18 22:19:05');

SELECT datediff('2019-09-03', '2019-06-21');


use sakila;
SELECT customer_id, count(*)
FROM rental
GROUP BY customer_id ;


SELECT customer_id, count(*)
FROM rental
GROUP BY customer_id
ORDER BY 2 desc;



SELECT customer_id, count(*)
FROM rental
GROUP BY customer_id
HAVING count(*) >= 40;

• customer_id값이 동일한 행들을 그룹화한 다음, 5개의 집계 함수 적용

SELECT customer_id,
max(amount) as max_amt,
min(amount) as min_amt,
avg(amount) as avg_amt,
sum(amount) as tot_amt,
count(*) as num_payments
FROM payment
GROUP BY customer_id;


SELECT max(amount) as max_amt,
min(amount) as min_amt,
avg(amount) as avg_amt,
sum(amount) as tot_amt,
count(*) as num_payments
FROM payment;

SELECT customer_id,
max(amount) as max_amt,
min(amount) as min_amt,
avg(amount) as avg_amt,
sum(amount) as tot_amt,
count(*) as num_payments
FROM payment
GROUP BY customer_id;


create database sqlclass_sb;
use sqlclass_sb;
CREATE TABLE number_tbl (val smallint);

INSERT INTO number_tbl VALUES(1);
INSERT INTO number_tbl VALUES(3);
INSERT INTO number_tbl VALUES(5);

SELECT count(*) as num_rows,
count(val) as num_vals,
sum(val) as total,
max(val) as max_val,
avg(val) as avg_val
FROM number_tbl;


use sakila;

# 단일 열 그룹화
SELECT actor_id, count(*)
FROM film_actor
GROUP BY actor_id;

# 다중 열 그룹화
SELECT fa.actor_id, f.rating, count(*)
FROM film_actor as fa
INNER JOIN film as f
on fa.film_id = f.film_id
GROUP BY fa.actor_id, f.rating
ORDER BY 1, 2;

# roll up
SELECT fa.actor_id, f.rating, count(*)
FROM film_actor as fa
inner join film as f 
on fa.film_id = f.film_id
GROUP BY fa.actor_id, f.rating with rollup
ORDER by 1,2;