create database scraping;
use scraping;

# pages 테이블이 존재하면 삭제함
drop table if exists pages;

create table pages (
id BIGINT(7) not null auto_increment,
title VARCHAR(200),
content VARCHAR(10000),
created TIMESTAMP default CURRENT_TIMESTAMP,  # 자동으로 날짜가 추가되는 타임스탬프
PRIMARY KEY(id)
);

# 테이블 구조 확인
describe pages;


# 데이터 추가
insert into pages(title, content)
values(
"Test page title",
"This is some test page content. It can be up to 10,000 characters long.");

insert into pages(title, content)
values(
"Second page title",
"This is the second test page content"
);

# 데이터 가져오기
select * from pages where title like "%test%";

select count(*) from pages;