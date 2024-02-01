# 1
create database sqlclass_db;
use sqlclass_db;

create  table world	
	(country VARCHAR(30),
	continent varchar(30),
	area int,
	population int,
	capital varchar(30),
	top_level_domain varchar(30),
	primary key (country)
	);
desc world;


insert into world values
('Afghanistan', 'Asia', 652230, 25500100, 'Kabul', '.af'),
('Algeria', 'Africa', 2381741, 38700000, 'Algiers', '.dz'),
('New Zealand', 'Oceania', 270467, 4538520, 'Wellington', '.nz'),
('Australia', 'Oceania', 7692024, 23545500, 'Canberra', '.au'),
('Brazil', 'South America', 8515767, 202794000, 'Brasilia', '.br'),
('China', 'Asia', 9596961, 1365370000, 'Beijing', '.cn'),
('India', 'Asia', 3166414, 1246160000, 'New Delhi', '.in'),
('Russia', 'Eurasia', 17125242, 146000000, 'Moscow', '.ru'),
('France', 'Europe', 640679, 659060000, 'Paris', '.fr'),   
('Germany', 'Europe', 357114, 807160000, 'Berlin', '.de'),
('Denmark', 'Europe', 43094, 5634437, 'Copenhagen', '.dk'),
('Norway', 'Europe', 323802, 5124383, 'Oslo', '.no'),
('Sweden', 'Europe', 450295, 9675885, 'Stockholm', '.se'),
('South Korea', 'Asia', 100210, 50423955, 'Seoul', '.kr'),
('Canada', 'North America', 9984670, 35427524, 'Ottawa', '.ca'),
('United States', 'North America', 9826675, 318320000, 'Washington, D.C.', '.us'),
('Armenia', 'Eurasia', 29743, 30174000, 'Yerevan', '.am');

# 2-1
select * from world;

# 2-2
select country, capital, top_level_domain from world
	where continent = 'Europe';

# 2-3
select country, population from world
	where continent = 'Asia'
	order by population desc;

# 2-4
select country, continent, area from world
	order by area desc;

# 2-5
select country, top_level_domain from world
	order by top_level_domain asc;
	

