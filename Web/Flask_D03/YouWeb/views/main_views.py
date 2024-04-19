    ## 모듈로딩
from flask import Blueprint, render_template, request, redirect, url_for
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

@bp.route('/question/input/')
def input_question():
    # 질문 입력 페이지 출력
    return render_template('question_input.html')

@bp.route('/question/input/finish/', methods=['POST'])
def input_finish():
    # 질문 입력 페이지 출력
    req_dict = request.form.to_dict()
    title = req_dict.get('title')
    content = req_dict.get('content')       
    return render_template('question_input_finish.html', title = title, content = content)