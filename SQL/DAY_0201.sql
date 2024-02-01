use sakila;

# 모든 열 검색
select * from language;

# 일부 열만 검색
SELECT language_id, name, last_update FROM language;

select name from language;

select language_id,
	'COMMON' language_usage,
	language_id * 3.14 lang_pi_value,
	upper(name) language_name
	from language;
	
# 중복 제거 - distinct 사용
select distinct actor_id from film_actor order by actor_id;

# 서브쿼리 : 파생테이블
select concat(cust.last_name, ', ', cust.first_name) full_name
from
	(select first_name, last_name, email
	from customer
	where first_name = 'JESSIE'
	) as cust;
	
# 임시테이블
create temporary table actors_j
(actor_id smallint(5),  # 5자리 공백을 만들고 출력하려고 (5) 입력
first_name varchar(45),
last_name varchar(45));

desc actors_j;

insert into actors_j
select actor_id, first_name, last_name
from actor where last_name like 'J%';

select * from actors_j;

# 가상테이블(View)
create view cust_vw as
	select customer_id, first_name, last_name, active
	from customer;

select * from cust_vw;

select first_name, last_name from cust_vw
where active=0;

# 테이블 연결 : 조인
select customer.first_name, customer.last_name,
	time(rental.rental_date) as rental_time
from customer inner join rental
	on customer.customer_id = rental.customer_id
where date(rental.rental_date) = '2005-06-14';

## 별칭 사용 - as 생략 가능
select c.first_name, c.last_name,
time(r.rental_date) as rental_time
from customer as c inner join rental as r
on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14';

# where 조건절 : and, or, not 연산자 사용
select title
from film 
where rating='G' and rental_duration>=7;

select title, rating, rental_duration
from film
where (rating='G' and rental_duration >= 7)
or(rating='PG-13' and rental_duration < 4);

# Group by절과 having절
select c.first_name, c.last_name, count(*) as 대여횟수
from customer as c inner join rental as r
on c.customer_id = r.customer_id
group by c.first_name, c.last_name
having count(*) >= 40
order by count(*) desc;

# order by절
select c.first_name, c.last_name,
time(r.rental_date) as rental_time
from customer as c inner join rental as r
on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by c.last_name, c.first_name asc;


# 연습문제 # 
# 실습 3-1
select actor_id,first_name,last_name
from actor
order by last_name, first_name;
# 실습 3-2
select  actor_id,first_name,last_name
from actor
where last_name ='WILLIAMS' or last_name ='DAVIS';
# 실습 3-3
select distinct customer_id
from rental
where date(rental_date) = '2005-07-05';
# 실습 3-4
select c.store_id,  c.email, r.rental_date, r.return_date
from customer as c inner join rental as r
	on c.customer_id = r.customer_id 
where date(r.rental_date) = '2005-06-14'
order by r.return_date desc;


# 범위 조건
select customer_id, rental_date
from rental
where rental_date < '2005-05-25';

select customer_id, rental_date
from rental
where rental_date <= '2005-06-16' # 6-16 포함 X
and rental_date >= '2005-06-14';

select customer_id, rental_date
from rental
where date(rental_date) <= '2005-06-16' # 6-16 포함
and date(rental_date) >= '2005-06-14';

# between 연산자 사용
select customer_id, rental_date
from rental
where date(rental_date) between '2005-06-14' and '2005-06-16';

select customer_id, payment_date, amount
from payment
where amount between 10.0 and 11.99;

select last_name, first_name
from customer
where last_name between 'FA' and 'FRB';

# in 연산자 사용
select title, rating
from film
where rating in ('G', 'PG');

# 서브 쿼리 사용
select title, rating
from film
where rating in (select rating from film where title like '%PET%');

# not in 연산자 사용
select title, rating
from film
where rating not in ('PG-13', 'R', 'NC-17');


# 일치 조건

# 문자열 부분 가져오기
select left('abcdefg',3);
select mid('abcdefg', 2, 3);
select right('abcdefg', 2);

# 와일드 카드 사용
select last_name, first_name
from customer
where last_name like '_A_T%S';

select last_name, first_name
from customer
where last_name like 'Q%' or last_name like 'Y%';

# 정교 표현식 사용
select last_name, first_name
from customer
where last_name REGEXP '^[QY]';

# Null
select rental_id, customer_id, return_date
from rental
where return_date is null;

select rental_id, customer_id, return_date
from rental
where return_date is not null;

select rental_id, customer_id, return_date
from rental
where return_date is null
or date(return_date) not between '2005-05-01' and '2005-08-31';


# 실습 4-1
select payment_id, customer_id, amount, date(payment_date) as payment_date
from payment
where (payment_id between 101 and 120)
and customer_id != 5 and (amount > 8 or date(payment_date) = '2005-08-23');

# 실습 4-2
select payment_id, customer_id, amount, date(payment_date) as payment_date
from payment
where (payment_id between 101 and 120)
and customer_id = 5 and not (amount > 6 or date(payment_date) = '2005-06-19');

# 실습 4-3
select amount from payment
where amount in (1.98, 7.98, 9.98);
