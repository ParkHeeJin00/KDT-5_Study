## -------------------------------------------------------------
## 역할 : 데이터 저장 및 출력 관련 웹 페이지 라우팅 처리
## URL : /input
##       /input/save
##       /input/delete
##       /input/update
## -------------------------------------------------------------
## 모듈 로딩
from flask import Blueprint, render_template, request, redirect, url_for
import datetime
import os

## BP 인스턴스 생성
dataBP = Blueprint('data',
                    __name__,
                    template_folder='templates',
                    url_prefix='/input') # 기본 url 지정



## 라우팅 함수들
@dataBP.route('/')
# http://127.0.0.1:5000/input/
def input_data():
    return render_template('input_data.html',
                        action = "/input/save",
                        method = "POST")

## GET 방식으로 데이터 저장 처리 함수
## 사용자의 요청 즉, request 객체에 데이터 저장되어 있음
@dataBP.route('/save_get/') # 기본값 : methods=['GET'] 
# http://127.0.0.1:5000/input/save_get/
def save_get_data():
    # 요청 데이터 추출
    req_dict = request.args.to_dict()
    v = req_dict.get('value')
    m = req_dict.get('message')

    # 이미지 출력
    
    # return render_template('save_data.html', value = v, message = m)
    # = return render_template('save_data.html', **req_dict) # 언팩킹
    return v,m

## POST 방식으로 데이터 저장 처리 함수
@dataBP.route('/save_post/', methods=['POST'])
# http://127.0.0.1:5000/input/save_post/
def save_post_data():

    # 속성은 보통 header에 존재하는 값 들고옴
    method = request.method
    headers = request.headers
    args = request.args
    form = request.form # 수정이 불가능한 dict형태로 반환
    file = request.files
    # req_dict = request.form.to_dict()
    # v = req_dict['value']
    # m = req_dict['message']
    # 데이터 저장 처리
    return f'method : {method}<br>headers : {headers}<br>args : {args}<br>form : {form}<br>file : {file}'
    # return render_template('save_data.html', **req_dict)

@dataBP.route('/save/', methods = ['POST','GET'])
def save_data():
    # 요청 데이터 추출
    if request.method == 'GET':
        req_dict = request.args.to_dict()  # type = text만 담김
    elif request.method == 'POST':
        req_dict = request.form.to_dict()

    v = req_dict.get('value')
    m = req_dict.get('message')
    i = request.files['image'] # type = file

    # 현재 디렉토리 절대 경로
    current_dir = os.getcwd()

    # 데이터 저장 처리
    suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    image_folder = os.path.join(current_dir, 'MyWeb', 'static', 'image')

    save_path = os.path.join(image_folder, f'{suffix}_{i.filename}')

    # 데이터 저장 처리
    i.save(save_path)
        
    # 이미지 출력
    req_dict['image'] = url_for('static', filename=f'image/{suffix}_{i.filename}')

    return render_template('save_data.html', **req_dict)


