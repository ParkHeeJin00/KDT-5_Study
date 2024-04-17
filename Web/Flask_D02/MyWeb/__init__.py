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

    from .views import data_view
    from flask import Blueprint

    # Blueprint 등록
    app.register_blueprint(data_view.dataBP)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/<popcorn_color>')
    def popcorn_col(popcorn_color):
        # return f"<h1>Give me the {popcorn_color} color popcorn"
        return render_template(f'color_popcorn.html', popcorn_color=popcorn_color)


    ## Flask Server 인스턴스 반환
    return app
