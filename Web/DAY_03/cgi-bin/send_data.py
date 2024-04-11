# 모듈 로딩
import cgi, sys, codecs, os, datetime
import cgitb

cgitb.enable()  # Error 확인

# Web 인코딩 설정
sys.stdout = codecs.getwriter(encoding='utf-8')(sys.stdout.detach())

# 웹페이지의 form태그 내의 input 태그 입력값 데이터 가져와서 객체에 저장하고 있는 인스턴스
form = cgi.FieldStorage()

# 클라이언트의 요청 데이터 추출
if 'img_file' in form and 'message' in form:
    filename = form['img_file']  # form.getvalues('img_file')
    msg = form['message']  # form.getvalues('message')
    


# 요청에 대한 응답 HTML
# HTML Header
print('Content-Type : text/html; charset=utf-8') # 한글 깨짐 방지 charset = utf-8
print()  # 무조건 한줄 띄어야 함

# HTML Body
print('<TITLE>CGI</TITLE>')
print('<H1>CGI</H1>')
print(f'hello CGI {form}')
print(f'<img src = {filename}>')
print(f'<h3>{msg}</h3>')



