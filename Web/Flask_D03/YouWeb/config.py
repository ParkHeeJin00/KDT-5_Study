# 모듈 로딩
import os

# 다양한 DBMS URI - SQLITE
BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'app.db'

# 다양한 DBMS URI 
DB_SQLITE_URI = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME_SQLITE)}'
                               # id : pw                 / database 이름 ( database 창 열고 show databases; / 아무거나 선택 )
DB_MYSQL_URI = 'mysql+pymysql://root:0718@localhost:3306/test_db'

# DB_MARIA_URI = 'mariadb+mariadb://root:0718@localhost:3306/testdb'
                                    # id : pw
# DB_POST_URI = 'postgresql+pg8000://scott:tiger@localhost/test'

## 사용할 DBMS 설정 / SQLALCHMY_ 시작 변수명 고정
SQLALCHEMY_DATABASE_URI = DB_MYSQL_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


# flask db init
# flask db migrate
# app.db를 DB( SQLite or mySQL )에 연결

# conda install pymysql

# 다른 DB에 연결하고 싶다면 migrate 폴더와 app.db 삭제하고 아래 다시 실행

# flask db init
# flask db migrate
# flask db upgrade