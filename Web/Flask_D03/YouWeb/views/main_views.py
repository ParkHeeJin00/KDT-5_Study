## 모듈로딩
from flask import Blueprint, render_template
from YouWeb.models import Question

# BP 인스턴스 생성
bp = Blueprint('main', 
               __name__,
                template_folder='templates',
                url_prefix='/')

## 라우팅 함수들
@bp.route('/')
def index():
    # Question 테이블에 저장된 데이터 읽어서 출력
    question_list = Question.query.order_by(Question.create_date.desc())

    return render_template('question_list.html', question_list = question_list)