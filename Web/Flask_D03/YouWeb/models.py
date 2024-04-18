## 모듈로딩 ( __init__ 파일의 이름을 대신하는 이름 -> 상위 폴더명)
from YouWeb import db

## Question 테이블 클래스
## 컬럼 : id, subject, content, create_date
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True) # not null / unique
    subject = db.Column(db.String(200), nullable=False) # not null
    content = db.Column(db.Text(), nullable=False) # not null
    create_date = db.Column(db.DateTime(), nullable=False) # not null

## Answer 테이블 클래스
## 컬럼 : id, question_id, quesion, content, create_date
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) # quesion 없으면 answer 삭제
    quesion = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)