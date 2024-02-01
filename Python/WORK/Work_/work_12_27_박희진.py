#1
my_hometown = "대구"
my_bloodtype = "O"
fav_season = "여름"
my_height = 172.6
my_number = "010-7680-0016"
my_country = "대한민국"

#2
mbti = 'INFP'
blood = 'A'
gender = 'M'
height = 171.7
weight = 77

#여러데이터 출력 방식
print("[ 신상 정보 ]\nMBTI :", mbti,"\t 혈액형 :", blood, "\t 성별 :", gender, "\n몸무게 :", weight,"\t 키 :", height)
#서식 지정자 출력 방식
print("[ 신상 정보 ]\nMBTI : %s \t 혈액형 : %s \t 성별 : %s \n몸무게 : %d \t 키 : %.1f" %(mbti, blood, gender, weight, height))
#F-스트링 출력 방식
print(f'[ 신상 정보 ]\nMBTI : {mbti} \t 혈액형 : {blood} \t 성별 : {gender} \n몸무게 : {weight} \t 키 : {height}')

#3-1
a = 50
b = 0.91
c = "Winter"
d = False

print(f"데이터 {a}   => ",type(a), "타입")
print(f"데이터 {b}   => ",type(b), "타입")
print(f"데이터 {c}   => ",type(c), "타입")
print(f"데이터 {d}   => ",type(d), "타입")
#3-2
fav_sea = input("좋아하는 계절은?")
print(f'당신은 {fav_sea}을 좋아하는 군요!')

spring_eng = input("봄은 영어로?")
print(f'봄은 영어로 {spring_eng}입니다.')

#4
# 힙영역 / 스택영역

#5
#int, float, str, bool
#2진수, 8진수, 16진수

#6
width_length = int(input("직육면체 가로길이(cm) :"))
vertical_length = int(input("직육면체 세로길이(cm) :"))
height = int(input("직육면체 높이길이(cm) :"))
sq_area = width_length * vertical_length
sq_vol = sq_area * height
print(f'직사각형 넓이 : {sq_area}\n직사각형 부피 : {sq_vol}')