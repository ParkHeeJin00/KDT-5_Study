# inner join
select c.first_name, c.last_name, a.address
	from customer as c inner join address as a
	on c.address_id = a.address_id;

select count(*)  # 총 599개의 행 출력
	from customer as c inner join address as a
	on c.address_id = a.address_id;

# join 조건 : on / 필터 조건 : where

# 이전 문법
select c.first_name, c.last_name, a.address
	from customer as c join address as a
	where c.address_id = a.address_id and a.postal_code = 52137;
# 현재 문법
select c.first_name, c.last_name, a.address, a.postal_code
	from customer as c join address as a
	on c.address_id = a.address_id
	where a.postal_code = 52137;

# 세개 이상 테이블 조인
select c.first_name, c.last_name, ct.city, a.address, a.district, a.postal_code
	from customer as c
	inner join address as a
	on c.address_id = a.address_id
	inner join city as ct
	on a.city_id = ct.city_id;

# 세개 이상 테이블 조인 - 서브 쿼리 사용
select c.first_name, c.last_name, addr.address, addr.city, addr.district
	from customer as c
	inner join
	(select a.address_id, a.address, ct.city, a.district
		from address as a
		inner join city as ct
	on a.city_id = ct.city_id
	where a.district = 'California'
	) as addr
	on c.address_id = addr.address_id;
# 서브 쿼리 단독 실행
select a.address_id, a.address, ct.city, a.district
	from address as a
	inner join city ct
	on a.city_id = ct.city_id
	where a.district = 'California';

# 테이블 재사용
select f.title from film as f
	inner join film_actor as fa
	on f.film_id = fa.film_id
	inner join actor a
	on fa.actor_id = a.actor_id
where ((a.first_name = 'CATE' and a.last_name = 'MCQUEEN')
	or (a.first_name = 'CUBA' and a.last_name = 'BIRCH'));
	
# 두 배우가 같이 출연한 영화만 검색
## 옆으로 조인 : 컬럼 확장
select f.title
from film as f
	inner join film_actor as fa1
	on f.film_id = fa1.film_id	
	inner join actor a1 # film, film_actor, actor 내부 조인 #1
	on fa1.actor_id = a1.actor_id
	inner join film_actor as fa2
	on f.film_id = fa2.film_id
	inner join actor a2 # film, film_actor, actor 내부 조인 #2
	on fa2.actor_id = a2.actor_id
where (a1.first_name = 'CATE' and a1.last_name = 'MCQUEEN')
and (a2.first_name = 'CUBA' and a2.last_name = 'BIRCH');


# 셀프 조인 #

use sqlclass_db;
create table customer
	(customer_id smallint unsigned,
	first_name varchar(20),
	last_name varchar(20),
	birth_date date,
	spouse_id smallint unsigned,
	constraint primary key (customer_id));

desc customer;

insert into customer (customer_id, first_name, last_name, birth_date, spouse_id)
values
(1, 'John', 'Mayer', '1983-05-12', 2),
(2, 'Mary', 'Mayer', '1990-07-30', 1),
(3, 'Lisa', 'Ross', '1989-04-15', 5),
(4, 'Anna', 'Timothy', '1988-12-26', 6),
(5, 'Tim', 'Ross', '1957-08-15', 3),
(6, 'Steve', 'Donell', '1967-07-09', 4);

# 배우자 없는 행(엔티티, 인스턴스, 레코드) 추가
insert into customer (customer_id, first_name, last_name, birth_date)
values (7, 'Donna', 'Trapp', '1978-06-23');

# 셀프 조인 예제
## 배우자 없는 행 -> self join할때 on 조건에서 걸러져서 제외됨
select
	cust.customer_id,
	cust.first_name,
	cust.last_name,
	cust.birth_date,
	cust.spouse_id,
	spouse.first_name as spouse_firstname,
	spouse.last_name as spouse_lastname
from customer as cust
	join customer as spouse
	on cust.spouse_id = spouse.customer_id;


# 실습
use sakila;

# 실습 5-2
select f.title
from film as f
	inner join film_actor as fa
	on f.film_id = fa.film_id
	inner join actor as a
	on fa.actor_id = a.actor_id
where a.first_name = 'JOHN';

# 실습 5-4
select a1.address as addr1, a2.address as addr2, a1.city_id, a1.district
from address as a1
	inner join address as a2
where (a1.city_id = a2.city_id)
and (a1.address_id != a2.address_id);



# 6장 #
# 집합 #
use sakila;
desc customer;
desc actor;

# union all
SELECT 'CUST' type1, c.first_name, c.last_name
FROM customer c
UNION ALL
SELECT 'ACTR' type1, a.first_name, a.last_name
FROM actor a;


SELECT c.first_name, c.last_name
FROM customer c
WHERE c.first_name LIKE 'J%' AND c.last_name LIKE 'D%'
UNION ALL
SELECT a.first_name, a.last_name
FROM actor a
WHERE a.first_name LIKE 'J%' AND a.last_name LIKE 'D%';

# union 
SELECT c.first_name, c.last_name
FROM customer c
WHERE c.first_name LIKE 'J%' AND c.last_name LIKE 'D%'
UNION
SELECT a.first_name, a.last_name
FROM actor a
WHERE a.first_name LIKE 'J%' AND a.last_name LIKE 'D%';

# intersect - inner join으로 동일한 결과 출력 가능
SELECT c.first_name, c.last_name
FROM customer c
WHERE c.first_name LIKE 'J%' AND c.last_name LIKE 'D%'
INTERSECT
SELECT a.first_name, a.last_name
FROM actor a
WHERE a.first_name LIKE 'J%' AND a.last_name LIKE 'D%';

SELECT c.first_name, c.last_name
FROM customer as c
INNER JOIN actor as a
ON (c.first_name = a.first_name) and (c.last_name = a.last_name)
WHERE a.first_name LIKE 'J%' and a.last_name LIKE 'D%';

# except 
SELECT a.first_name, a.last_name
FROM actor a
WHERE a.first_name LIKE 'J%' AND a.last_name LIKE 'D%'
EXCEPT
SELECT c.first_name, c.last_name
FROM customer c
WHERE c.first_name LIKE 'J%' AND c.last_name LIKE 'D%';

# 실습 6-3
SELECT first_name, last_name
FROM actor
WHERE last_name LIKE 'L%'
UNION
SELECT first_name, last_name
FROM customer
WHERE last_name LIKE 'L%'
ORDER BY last_name;


# 7장 #
use test_db;


CREATE TABLE string_tbl
(char_fld CHAR(30),
vchar_fld VARCHAR(30),
text_fld TEXT);

desc string_tbl ;

INSERT INTO string_tbl (char_fld, vchar_fld, text_fld)
VALUES ('This is char data',
'This is varchar data',
'This is text data');

SELECT * FROM string_tbl;

# 문자열의 최대 크기 넘어가면 ERROR 발생 - table의 vchar_fld 데이터 타입을 변경하는 게 낫다!
UPDATE string_tbl
SET vchar_fld = 'This is a piece of extremely long varchar data';

# 따옴표 추가
update string_tbl
set text_fld = 'This string didn''t work, but it does now';

update string_tbl
set text_fld = 'This string didn\'t work, but it does now';

select text_fld from string_tbl;

# quote() 함수 :  전체 문자열을 따옴표로 묶고, 문자열 내부의 작은 따옴표에 escape문자를 추가
select quote(text_fld)
from string_tbl;

# length() 함수 : 문자열의 개수 반환
SELECT length(char_fld) as char_length,
length(vchar_fld) as varchar_length,
length(text_fld) as text_length
FROM string_tbl;

# position() 함수 : 부분 문자열의 시작 위치를 반환
select vchar_fld from string_tbl st ;

SELECT position('piece' in vchar_fld), vchar_fld 
FROM string_tbl;   # 없으면 0 반환

# locate('문자열', 열이름, 시작위치) 함수 : 시작위치부터 문자열 검색 
SELECT locate('is', vchar_fld, 5), vchar_fld 
FROM string_tbl;

SELECT locate('is', vchar_fld, 1), vchar_fld 
FROM string_tbl;

# strcmp('문자열1', '문자열2') 함수: 문자열 비교
DELETE FROM string_tbl;

INSERT INTO string_tbl(vchar_fld)
VALUES ('abcd'),
('xyz'),
('QRSTUV'),
('qrstuv'),
('12345');

select * from string_tbl;

select vchar_fld from string_tbl order by vchar_fld;

SELECT strcmp('12345', '12345') 12345_12345,
	strcmp('abcd', 'xyz') abcd_xyz,
	strcmp('abcd', 'QRSTUV') abcd_QRSTUV,
	strcmp('qrstuv', 'QRSTUV') qrstuv_QRSTUV,
	strcmp('12345', 'xyz') 12345_xyz,
	strcmp('xyz', 'qrstuv') xyz_qrstuv; # 대소문자 구분 X
	
# like 또는 regexp 연산자 사용 : 0 또는 1의 값 반환
use sakila;

SELECT name, name LIKE '%y' ends_in_y
FROM category;

SELECT name, name REGEXP 'y$' ends_in_y
FROM category;


# 문자열 조작
use test_db;

INSERT INTO string_tbl (text_fld)
VALUES ('This string was 29 characters');

# concat(): 문자열 추가 함수
UPDATE string_tbl
SET text_fld = CONCAT(text_fld, ', but now it is longer');

select * from string_tbl st ;

# concat() 함수 사용 #2
use sakila;
SELECT concat(first_name, ' ', last_name,
' has been a customer since ', date(create_date)) as cust_narrative
FROM customer;

# insert() 함수
SELECT INSERT('goodbye world', 9, 0, 'cruel ') as string;

SELECT INSERT('goodbye world',1, 7, 'hello') as string;

# replace() 함수
SELECT replace('goodbye world', 'goodbye', 'hello') as replace_str;

# substr() 또는 substring() 함수
SELECT substr('goodbye cruel world', 9, 5);