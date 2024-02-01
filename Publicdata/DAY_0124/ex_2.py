import csv
import matplotlib.pyplot as plt
import platform

f = open('../DATA/daegu_hj-utf8.csv', encoding='utf-8-sig')	#	utf-8-sig	생략 가능
data = csv.reader(f)
header = next(data)


# 데이터를 리스트에 저장하기
result = []  # 빈 리스트 생성
for row in data:
    if row[4] != '': # 최고 기온 값이 빈 값이 아닌 경우
        result.append(float(row[4]))  # result 리스트에 실수형으로 타입 캐스팅 후 추가
    print(len(result))
f.close()
# 그래프 그리기
plt.figure(figsize=(10,	2))	# 그래프 크기 조절(가로 10인치,	세로 2인치)
plt.plot(result, 'r')	# result 리스트에 저장된 값을 빨간색 그래프로 그리기
plt.show()

# -----------------------------------------------------------------------------
# 랜덤 주사위
import random
import matplotlib.pyplot as plt

dice = []
for i in range(10):
    dice.append(random.randint(1,6))

print(dice)

# 그래프 그리기
plt.hist(dice,	bins=6)  # 구간을 6개로 ## hist(데이터, bin = 구간 개수)
plt.xticks([1,	2,	3,	4,	5,	6])
plt.show()


# -----------------------------------------------------------------------------
# 최고 기온 데이터를 히스토그램으로 표현
import csv
import matplotlib.pyplot as	plt
import koreanize_matplotlib

f = open('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)  # for 헤더 제외한 데이터를 뽑기 위해

result = []
for	row	in data	:
    if row[-1] != '':  # = row[4]
        result.append(float(row[-1]))  # 최고 기온을 리스트에 저장

f.close()

# 그래프 그리기
plt.figure(figsize=(10,	2))
plt.hist(result, bins=500, color='blue')    # result에 저장된 값을 히스토그램으로 그림

##  rc(항목, 항목설정) - 여러 사항에 사용 가능
plt.rc('font', family='Malgun Gothic')  # font를 family='Malgun Gothic' 하라

# 레이블에 마이너스('-')기호 깨지는 현상 해결
plt.rcParams['axes.unicode_minus'] = False	    # = plt.rc('axes',	unicode_minus=False)

plt.title("1907년 부터 2023년까지 대구 기온 히스토그램")
plt.show()


# -----------------------------------------------------------------------------
# 날짜 정보 분리

date_string1 = '2024 01	01'
# 공백을 기준으로 분리
print(date_string1.split())

# 구분자:'-' 기준으로 분리
date_string2 = '2023-12-31'
split_date_string = date_string2.split('-')
print(split_date_string)
year = split_date_string[0]
month = split_date_string[1]
day = split_date_string[2]
print(f'연도:{year}, 월:{month}, 일:{day}')

# -----------------------------------------------------------------------------
# 기온 히스토그램 (8월)


f = open('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)

# 히스토그램 데이터 리스트
aug =[]

# 8월달의 최고 기온 정보만 리스트에 추가
for	row	in data	:
    month =	row[0].split('-')[1]
    if row[-1] != '':
        if month == '08':
            aug.append(float(row[-1]))  # 그래프로 표시하기 위해 실수형으로 변환
f.close()

# 그래프 그리기
plt.hist(aug, bins = 100, color='tomato')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel("Temperature")
plt.ylabel("Counts")
plt.show()


# -----------------------------------------------------------------------------
# 1월과 8월의 기온 데이터 히스토그램

f = open('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)

# 히스토그램 데이터 리스트
aug = []
jan = []

# 8월달의 최고 기온 정보만 리스트에 추가
for	row	in data	:
    month =	row[0].split('-')[1]
    if row[-1] != '':
        if month == '08':  # 8월
            aug.append(float(row[-1]))
        if month == '01':  # 1월
            jan.append(float(row[-1]))
f.close()

# 그래프 그리기
plt.hist(aug, bins = 100, color='tomato', label='Aug')
plt.hist(jan, bins = 100, color='b', label='Jan')
plt.title('대구 1월과 8월의 최고 기온 히스토그램')
plt.xlabel("Temperature")
plt.rc('axes', unicode_minus=False) # 레이블에 마이너스('-')기호 깨지는 현상 해결
plt.legend()
plt.show()


# -----------------------------------------------------------------------------
# 매년 특정 날짜의 최고 기온 찾기

def draw_graph_on_date(month, day):
    f = open('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    result = []
    for row in data:
        if row[-1] != '':  # 최고 기온 data가 공백이 아니라면 아래를 실행하라
            date_string = row[0].split('-')
            if date_string[1] == month and date_string[2] == day:
                result.append(float(row[-1])) # 최고 기온을 실수형으로 변환 후 리스트에 추가
    f.close()
    # 그래프 그리기
    plt.figure(figsize=(15,2))
    plt.plot(result, 'royalblue')
    plt.rc('axes', unicode_minus=False)
    plt.rc('font', family='Malgun Gothic')
    plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
    plt.show()

month, date	= input('날짜(월 일)를 입력하세요:  ').split()
draw_graph_on_date(month, date)


# -----------------------------------------------------------------------------
# 2000년도 이후 특정일의 최저, 최고 기온 찾기

def	draw_lowhigh_graph(start_year, month, day):

    f = open('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)

    high_temp = []		#	최고 기온을 저장할 리스트
    low_temp = []			#	최저 기온을 저장할 리스트
    x_year = []					#	x축 연도를 저장할 리스트
    for row in data :
        if row[-1] != '':
            date_string = row[0].split('-')	#	날짜 데이터를 미리 분리함
            if int(date_string[0]) >= start_year:	#	문자열 값을 int형으로 변환해서 비교
                if int(date_string[1]) == month	and	int(date_string[2])	== day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0])	#	연도 저장
    f.close()

# 그래프 그리기
    plt.figure(figsize=(20,	4))
    plt.plot(x_year,	high_temp,	'hotpink',	marker='o',	label='최고기온')	#	최고 기온 그래프
    plt.plot(x_year,	low_temp,	'royalblue',	marker='s',	label='최저기온')	#	최저 기온 그래프
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic', size=8)	#	간단히 맑은 고딕으로 설정
    else:
        plt.rc('font', family='AppleGothic', size=8)	#	한글 폰트 사용 For	Mac	OS
    plt.rcParams['axes.unicode_minus']	=	False	#	음수(-)가 깨지는 것 방지
    plt.title(f"{start_year}년 이후 {month}월 {day}일의 온도 변화 그래프",	size=16)
    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.show()

draw_lowhigh_graph(2000,12, 24)