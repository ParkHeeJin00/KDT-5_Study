#---------------------------------------------------------
# str 데이터 타입 전용의 함수 즉 메서드(method) 살펴 보기
# - 메서드(Method)
#   특정 데이터 타입에서만 사용 가능한 함수를 의미
# - 사용방법
#   변수명.메서드명() ==> msg="Good"
#                      msg.메서드명()
#   데이터.메서드명() ==> "Good".메서드명()
#---------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => index() 메서드
# - 왼쪽 ----> 오른쪽, 제일 먼저 발견되는 문자의 인덱스 반환
# - 존재하지 않는 str 인덱스 찾으려고 하면 Error 발생
#---------------------------------------------------------
data = "Merry Christmas"
print(f'data.index("C") => {data.index("C")}')
print(f'data.index("r") => {data.index("r")}')

first_r = data.index("r") # 0번 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기
second_r = data.index("r", first_r+1) # 첫번째 'r' 인덱스 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기
third_r = data.index("r", second_r+1) # 두번째 'r' 인덱스 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기

print(f'data.index("r") => {data.index("r",first_r+1)}')
print(f'data.index("r") => {data.index("r",3)}')
print(f'data.index("r") => {data.index("r",4)}')


# !의 인덱스를 찾기
#print(f'data.index("!") => {data.index("!")}')


#---------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => find() 메서드
# - 왼쪽 ----> 오른쪽, 제일 먼저 발견되는 문자의 인덱스 반환
# - 존재하지 않는 str 인덱스 찾으려고 하면 -1 반환   # -1은 전체라는 뜻을 내포
# #---------------------------------------------------------
# !의 인덱스를 찾기
print(f'data.find("!") => {data.find("!")}')


#---------------------------------------------------------
# str 데이터에서 문자열 분리해주는 메서드 => split() 메서드
# - 기본값 : 스페이스 바, 공백 기준으로 1개의 str을 여러 개의 str 분리
# - 반환값/결과값/리턴값 : 여러 개의 str을 담아서 리스트(List)로 변환
#---------------------------------------------------------
data = "Happy New Year"

# str에서 공백을 기준으로 str 나누기
datas =data.split()

print(type(datas), datas)

# list에 저장된 원소/요소 하나씩 일기 => 변수명[인덱스]
print(f'datas[0] => {datas[0]}')
print(f'datas[1] => {datas[1]}')
print(f'datas[-1] => {datas[-1]}')

juminNo = '123456-1234567'

birth = juminNo[:juminNo.index('-')]
number = juminNo[juminNo.index('-')+1:]

print(juminNo.split("-"))
print(juminNo.split("-")[0])
print(juminNo.split("-")[1])
