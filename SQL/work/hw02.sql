use sqlclass_db

# 1
select year, category, fullname
from nobel
where year = 1960 and (category = 'Physics' or category = 'Peace');

# 2
select year, category, birth_continent, birth_country
from nobel
where fullname ='Albert Einstein';

# 3
select  year, fullname, birth_country
from nobel
where category = 'Peace' and (year between 1910 and 2010)
order by year asc;

# 4
select category, fullname
from nobel
where fullname like 'John%';

# 5
select * from nobel
where year = 1964 and category <> 'Physiology or Medicine' and category <> 'Chemistry' 
order by fullname asc;

# 6
select year, fullname, gender, birth_country
from nobel
where category = 'Literature' and (year between 2000 and 2019);

# 7
select count(fullname)
from nobel
group by category 
order by count(fullname) desc;

# 8
select distinct year
from nobel
where category = 'Physiology or Medicine';

# 9 
select count(distinct year) as '없던 년도'
from nobel
where year not in
(select year
from nobel
where category = 'Physiology or Medicine');

# 10
select fullname, category, birth_country
from nobel
where gender = 'female';

# 11
select  birth_country, count(*) as 횟수
from nobel
group by birth_country;

# 12
select * from nobel
where birth_country like '%Korea%';

# 13
select * from nobel
where birth_continent not in ('Europe', 'North America','');

# 14 
select birth_country , count(*) as '국가별 수상횟수'
from nobel 
group by birth_country 
having count(*) >= 10
order by count(*) desc;

# 15
select fullname, count(*) as 횟수
from nobel 
where fullname <> ('')
group by fullname 
having count(*) >= 2
order by fullname asc;

