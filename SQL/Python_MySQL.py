import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root',password='0718',db = 'sakila', charset='utf8')

cur = conn.cursor()
cur.execute('select * from language')
# cursor.excute('쿼리문장', args = None) : 작성한 쿼리를 실행
rows = cur.fetchall() # 모든 데이터를 가져옴 -> DF로 변환 가능
print(rows)
language_df = pd.DataFrame(rows) # DataFrame 형태로 변환
print(language_df)
cur.close()
conn.close() # 데이터베이스 연결 종료

# ------------------------------------------------------------------
# MySQL에 연결
conn = pymysql.connect(host='localhost', user='root',password='0718',db = 'sakila', charset='utf8')
# cursor 객체 생성
cur = conn.cursor()
# 실행할 쿼리 문장
query = '''
select c.email
from customer as c
inner join rental as r
on c.customer_id = r.customer_id
where date(r.rental_date) = (%s)'''
# execute('쿼리문장', args) -> %s = 2005-06-14
cur.execute(query, ('2005-06-14'))

rows = cur.fetchall() # 모든 데이터를 가져옴
for row in rows:
    print(row)
cur.close()
conn.close()

# ------------------------------------------------------------------
import pymysql
def create_table(conn, cur):
    try:
        query1 ='drop table if exists customer'
        query2 = """
        create table customer
        (name varchar(10),
        category smallint,
        region varchar(10))
        """
        # 작성한 쿼리를 실행
        cur.execute(query1)
        cur.execute(query2)
        # 변경한 내용 커밋
        conn.commit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)

def main():
    # 데이터베이스(sqlclass_db) 연결
    conn = pymysql.connect(host='localhost',user='root', password='0718',db = 'sqlclass_db', charset='utf8')

    # cursor 객체 생성
    cur = conn.cursor()

    # 테이블 생성 함수 호출
    create_table(conn, cur)

    # 연결 종료
    cur.close()
    conn.close()
    print('Database 연결 종료')

main()

import pymysql
conn = pymysql.connect(host='localhost', user='root', password='0718',db='sqlclass_db', charset='utf8')

curs = conn.cursor()
sql = """insert into customer(name, category, region)

values (%s, %s, %s)"""

curs.execute(sql, ('홍길동', 1, '서울'))
curs.execute(sql, ('이연수', 2, '서울'))
conn.commit()
print('INSERT 완료')
curs.close()
conn.close()


import pymysql
conn = pymysql.connect(host='localhost', user='root', password='0718',db='sqlclass_db', charset='utf8')

curs = conn.cursor()
sql = """insert into customer(name, category, region)
values (%s, %s, %s)"""

data = (
('홍진우', 1, '서울'),
('강지수', 2, '부산'),
('김청진', 1, '대구'),
)
# data는 tuple 형식으로
curs.executemany(sql, data)
conn.commit()
print('executemany() 완료')
curs.close()
conn.close()

'''
UPDATE, DELETE
'''
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='0718',db='sqlclass_db', charset='utf8')

curs = conn.cursor()

# region이 서울 특별시면 region을 서울으로 변경해라
sql = """update customer
set region = '서울특별시'
where region = '서울'"""

curs.execute(sql)
print('update 완료')
sql = "delete from customer where name=%s"
curs.execute(sql, '홍길동')
print('delete 홍길동')
conn.commit()
conn.close()