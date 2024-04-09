# 기준 경로 : DAY_02_01

# 모듈 로딩
import cgi, sys, codecs, os, datetime
import cgitb
cgitb.enable()  # Error 확인

# Web 인코딩 설정
sys.stdout = codecs.getwriter(encoding='utf-8')(sys.stdout.detach())

# 요청 처리 및 브라우징
# Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()


# Web 브라우저 화면 출력 코드

filepath = './HTML/test.html'

def print_html(filename, data = ''):
    # HTML 파일 읽기 => body 문자열
    with open(filename, 'r', encoding='utf-8') as f:
    
        # HTML Header
        print('Content-Type : text/html; charset = utf-8')
        print()  # 무조건 한줄 띄어야 함

        # HTML Body
        body = f.read().format(data)
        print(body)

# 데이터 추출
if 'data' in form and 'no' in form:
    result = form.getvalue('data') + '-' + form.getvalue('no')  # = form['data'] + '-' + form['no]
else:
    result = "No Data"

# 브라우징 : 함수 실행
print_html(filepath, result)
