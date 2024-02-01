show databases;
use sakila;
select now();

create database test_db;
use test_db;

# person 테이블 생성
# CONSTRAINT PK PERSON : 제약조건의 별칭 설정
drop table if exists person;
CREATE TABLE person
	(person_id SMALLINT UNSIGNED,
	fname VARCHAR(20),
	lname VARCHAR(20),
	eye_color ENUM('BR','BL','GR'),
	birth_date DATE,
	street VARCHAR(30),
	city VARCHAR(20),
	state VARCHAR(20),
	country VARCHAR(20),
	postal_code VARCHAR(20),
	CONSTRAINT pk_person PRIMARY KEY (person_id)
	);
	
# person 테이블 확인
desc person;

drop table if exists favorite_food;
CREATE TABLE favorite_food
	(person_id SMALLINT UNSIGNED,
	food VARCHAR(20),
	CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
	CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id) REFERENCES person(person_id)
	);

# favorite_food 테이블 확인
desc favorite_food ;

# 숫자 키 자동 증가 기능 추가 : auto_increment
# 기본키의 경우 - 테이블 수정 : 비활성화 -> 수정 -> 활성화
set foreign_key_checks=0;
ALTER TABLE person MODIFY person_id smallint unsigned auto_increment;
set foreign_key_checks=1;
# person 테이블 확인
desc person;

# 테이블 추가
INSERT INTO person
	(person_id, fname, lname, eye_color, birth_date) # 없는 컬럼은 null값으로 추가
	VALUES (null, 'William', 'Turner', 'BR', '1972-05-27');
	
# 데이터 확인
select * from person;

# lname이 Turner인 데이터만 person 테이블에서 출력
select person_id, fname, lname, birth_date
	from person where lname = 'Turner';
	
# food 테이블에 데이터 추가
DELETE FROM favorite_food where person_id=1; # person_id값이 1인 데이터 삭제
INSERT INTO favorite_food (person_id, food)
	VALUES (1, 'pizza'),
	(1, 'cookie'),
	(1, 'nachos');
	
# 데이터 확인
select * from favorite_food;

# 컬럼의 값을 알파벳 순서로 정렬
SELECT food FROM favorite_food
	WHERE person_id=1 ORDER BY food;
	
# 데이터 확인
select * from favorite_food;

# person 테이블에 데이터 추가
INSERT INTO person
	(person_id, fname, lname, eye_color, birth_date,
	street, city, state, country, postal_code)
	VALUES(, 'Susan', 'Smith', 'BL', '1975-11-02',
	'23 Maple St.', 'Arlington', 'VA', 'USA', '20220');

# 데이터 확인
SELECT person_id, fname, lname, birth_date FROM person;

# 데이터 수정
UPDATE person
SET street = '1225 Tremon St.',
	city = 'Boston',
	state = 'MA',
	country = 'USA',
	postal_code = '02138'
	WHERE person_id=1;

# 데이터 확인
select * from person;

# 데이터 삭제
DELETE FROM person WHERE person_id=2;

# 데이터 확인
SELECT * FROM person;

# food에 id가 3인 데이터를 추가하기 위해선 person 테이블에 id 3이 존재해야함
INSERT INTO person (person_id, fname, lname) VALUES(3, 'Kevin', 'Kern');

INSERT INTO favorite_food (person_id, food) VALUES (3, 'lasagna');

# 데이터 확인
select * from favorite_food;

# 날짜 데이터 업데이트
UPDATE person SET birth_date = str_to_date('DEC-21-1980', '%b-%d-%Y')
	WHERE person_id=1;
