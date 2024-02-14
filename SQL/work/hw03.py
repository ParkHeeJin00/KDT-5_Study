import pymysql
import pandas as pd


# 테이블 생성하는 함수
def create_table(query):
    # 데이터베이스(shoppingmall) 연결
    conn = pymysql.connect(host='localhost', user='root', password='0718', db='shoppingmall', charset='utf8')

    # cursor 객체 생성
    cur = conn.cursor()

    try:
        # 작성한 쿼리를 실행
        cur.execute(query)
        # 변경한 내용 커밋
        conn.commit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)

    # 연결 종료
    cur.close()
    conn.close()
    print('Database 연결 종료')

# 쿼리 실행하는 함수
def query(query):
    # 데이터베이스(shoppingmall) 연결
    conn = pymysql.connect(host='localhost', user='root', password='0718', db='shoppingmall', charset='utf8')

    # cursor 객체 생성
    cur = conn.cursor()

    try:
        # 작성한 쿼리를 실행
        cur.execute(query)
        # 변경한 내용 커밋
        conn.commit()
        print('commit 완료')
    except Exception as e:
        print(e)

    # 연결 종료
    cur.close()
    conn.close()
    print('Database 연결 종료')

    return cur

# 프린트 출력하는 함수
def print_line(n,cur,*args):
    print(f'문제 {n}번')
    print('-'*45)
    for i in args:
        print(i, end = '\t')
    print('\n','-'*45)
    for c in cur:
        print(c)

user_table = '''create table user_table
    (userID char(8) not null primary key,
    userName varchar(10) not null,
    birthYear int not null, 
    addr char(2) not null,
    mobile1 char(3), 
    mobile2 char(8),
    height smallint, 
    mDate date) '''

buy_table = '''create table buy_table(
    num int not null primary key auto_increment,
    userID char(8) not null,
    prodName char(6) not null,
    groupName char(4),
    price int not null,
    amount smallint not null,
    foreign key (userID) references user_table(userID))'''

# 테이블 생성 함수 호출
create_table(user_table)

create_table(buy_table)

# table에 insert 하기

insert_q1 = '''insert into user_table values
('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
('KJD', '김제동', 1974, '경남', NULL, NULL, 173, '2013-03-03'),
('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'),
('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'),
('SDY', '신동엽', 1971, '경기', NULL, NULL, 176, '2008-10-10'),
('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08')
'''
query(insert_q1)

insert_q2 = '''insert into buy_table values
(1, 'KHD', '운동화', NULL, 30, 2),
(2, 'KHD', '노트북', '전자', 1000, 1),
(3, 'KYM', '모니터', '전자', 200, 1),
(4, 'PSH', '모니터', '전자', 200, 5),
(5, 'KHD', '청바지', '의류', 50, 3),
(6, 'PSH', '메모리', '전자', 80, 10),
(7, 'KJD', '책', '서적', 15, 5),
(8, 'LHJ', '책', '서적', 15, 2),
(9, 'LHJ', '청바지', '의류', 50, 1),
(10, 'PSH', '운동화', NULL, 30, 2),
(11, 'LHJ', '책', '서적', 15, 1),
(12, 'PSH', '운동화', NULL, 30, 2)
'''
query(insert_q2)

# 2-1
query1 ='''
select ut.userName, bt.prodName , ut.addr,concat(ut.mobile1, ut.mobile2) '연락처'
from user_table ut join buy_table bt
on ut.userID = bt.userID
'''
q1 = query(query1)
print_line(1,q1,'userName','prodName','addr','연락처')

# 2-2
query2 = '''
select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2)
from user_table ut join buy_table bt
on ut.userID = bt.userID
where ut.userID = 'KYM'
'''
q2 = query(query2)
print_line(2,q2,'userID','userName','prodName','addr','연락처')

# 2-3
query3 = '''
select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2) as '연락'
from user_table ut join buy_table bt
on ut.userID = bt.userID
order by ut.userID
'''
q3 = query(query3)
print_line(3,q3,'userID','userName','prodName','addr','연락처')

# 2-4
query4 = '''
select distinct ut.userID,ut.userName, ut.addr
from user_table ut join buy_table bt
on ut.userID = bt.userID
order by ut.userID
'''
q4 = query(query4)
print_line(4,q4,'userID','userName','addr')

# 2-5
query5 ='''
select ut.userID, ut.userName, ut.addr, concat(ut.mobile1, ut.mobile2) as '연락'
from user_table ut join buy_table bt
on ut.userID = bt.userID
where addr in ('경북', '경남')
order by ut.userID
'''
q5 = query(query5)
print_line(5,q5,'userID','userName','addr','연락처')







