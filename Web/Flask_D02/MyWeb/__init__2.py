### Application Factory 기반의 Flask Server 구동

## 모듈 로딩
from flask import Flask, render_template, url_for
# from .views import views

### Application Factory 기반의 함수 정의
### 함수명 : create_app 변경 불가
### 반환값 : Flask Server 인스턴스
def create_app():
    ### Flask Server 인스턴스 생성
    app = Flask(__name__)

    ## Blueprint 인스턴스 등록 : 서브 카테고리의 페이지 라우팅 기능
    # app.register_blueprint(views)
    @app.route('/')
    def index():
        return render_template('index.html')  
        # templates 폴더 아래에 있다고 가정하기 때문에 파일명만 입력하면됨
    
    # 데이터 전송하는 라우팅 => 변수<타입:변수명>
    @app.route('/popcorn/<popcorn_color>')
    def popcorn_col(popcorn_color):
        # return f"<h1>Give me the {popcorn_color} color popcorn"
        return render_template(f'{popcorn_color}_popcorn.html', popcorn_color=popcorn_color)

    # 보통 상대경로 이용
    # flask routes로 제대로 경로 들어가는지 확인

    ## Blueprint 인스턴스 반환

    ## 테스트 기능 - 경로 확인
    with app.test_request_context():
        print(url_for('static', filename='css/style_1.css'))

    ## Flask Server 인스턴스 반환
    return app
