# MiniWeb은 Webserver directory

### 모듈 로딩
from flask import Flask, render_template, Blueprint


### 애플리케이션 팩토리 함수
def create_app():
      myapp = Flask(__name__)

      # bp등록
      from .views import main_view
      myapp.register_blueprint(main_view.bp)
      
      return myapp

# ### 전역변수
# myapp = Flask(__name__)


# ### 사용자 요청 URL 처리 기능 => 라우팅(Routing)
# ### 형식 : @Flask_instance_name.route(URL문자열)

# # 웹 서버의 첫 페이지 : http://127.0.0.1:5000/ ( 5000 뒷부분부터 적으면 됨)
# @myapp.route("/")
# def index_page():
#       # return '<h3><font color = "red">My Web Index Page</font></h3>'
#       return render_template('tem.html')

# ### 사용자마다 페이지 반환
# ### 사용자 페이지 URL : http://127.0.0.1:5000/<username>
# @myapp.route('/<username>')   # username이 딱 존재해야 가능
# def username(name):
#       return f"username : {name}"

# @myapp.route('/<int:number>')   # number이 숫자형태로 존재해야 가능
# def usernumber(number):
#       return f"Select Number : {number}"

# @myapp.route('/hello/')  # /hello( = 파일과 비슷 ) 와 /hello/( = 폴더와 비슷 ) 는 다름
# def hello():
#       return 'Hello!'

# @myapp.route('/hello/<name>')
# def hello_name(name):
#       return f'Hello {name}'

# @myapp.route('/user_info2')
# def user_login2():
#       return myapp.redirect('/')  # 기본 페이지로 이동

# ### 사용자 페이지 URL : http://127.0.0.1:5000/<username>/<age>
# ### 실행제어 
# if __name__ == "__main__":
#     # Flask 웹 서버 구동
#       myapp.run(debug=True) # debug = True : 수정 업로드


