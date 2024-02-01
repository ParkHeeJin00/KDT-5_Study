# -------------------------------------------------------------
# [실습1] 'Hello World" 100번 출력
# -------------------------------------------------------------
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
# --100개

# -------------------------------------------------------------
# 반복문 => for in 반복문 =======================================
# - 여러개의 데이터를 가지고 있는 데이터에서 한 개씩 원소/요소를 읽어와줌
# for 요소저장변수명 in 여러개 데이터가진 타입:
# <-->요소/원소 반복할 코드
# <-->요소/원소 반복할 코드
# -------------------------------------------------------------
msg = "Happy New Year 2024! Good Luck^^"

# msg를 구성하는 문자 한개씩 화면에 출력해주세요!
for i in msg:
    print(i)

# [실습1] 'Hello World" 100번 출력
for cnt in range(100): ## 0~99 총 100개     ## in 뒤에는 반복가능한 타입이 와야함 - range str dict tuple
    print('Hello World')

# [실습2] 좋아하는 음식명을 리스트에 저장하기 (단, 10개)
foods = ['마라탕','삼겹살','찜닭','엽떡','닭발','족발','국밥','막창','곱창전골','짬뽕']
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4])
print(foods[5])
print(foods[6])
print(foods[7])
print(foods[8])
print(foods[9])

for cnt in foods : print(cnt)  # 실행문이 한줄이면 한줄로도 가능

for cnt in foods:
    print(cnt)

# 희진이가 해본 것
for i in range(9):
    print(foods[i])