# ------------------------------------------------------------
# 파일 입출력 => 출력 즉, 읽기(Read)
# - 사용 내장 함수 : open(file, mode = 'rt'[기본값], encoding = '시스템 기본값')
# - encoding 설정 : 파일에 적용된 인코딩을 설정해야 함!!
# ------------------------------------------------------------

# (1) open
file = open('message.txt', encoding='utf8')  ## encoding 값이 none이면 시스템 운영체제를 따라감
## open()의 리턴값 - 파일을 열고 접근할 수 있는 객체의 접근값 - 파일 저장하는 데이터 타입
print(f'file => {type(file)}, {file}')

# (2) IO => read() : 파일 안에 모든 내용 다 읽어오기
# fdata= file.read()   ## 인코딩 방법 다르면 에러
# print(f'fdata => {type(fdata)}, {fdata}')    ## setting에서 incoding 방법 바꿀 수 있음

# # (2) IO => read(n) : 지정된 숫자 만큼 문자를 파일에서 읽어오기(공백 포함)
# fdata = file.read(5)     ## 5byte 읽음
# print(f'fdata => {type(fdata)}, {fdata}')

# (2) IO => readline() : '\n'기분으로 한 줄 읽어오기
## 모두 받아오는 게 아니라 거르고 받아와야 할 때 사용!!
# datas = []
# while True:     ## 다 담기 위해서 반복문
#     fline = file.readline()  ## 줄바꿈이 포함되어있음
#     datas.append(fline)
#     if not fline: break
#     print(f'fline => {type(fline)}, {fline}', end = '')
#
# print(f'datas => {type(datas)}, {datas}')

# (2) IO => readlines() : '\n' 기준으로 한 줄 씩 읽은 것을 리스트에 담아서 반환
datas = file.readlines()   ## 반복문 돌린것과 기능 같음
print(datas)



# (3) close
file.close()