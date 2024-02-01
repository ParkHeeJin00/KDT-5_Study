import	csv
import koreanize_matplotlib


#---------------------------------------------------------------------
# 헤더와 위 다섯개 데이터 뽑아오기
#---------------------------------------------------------------------
f = open('../DATA/subwayfee.csv', encoding ='utf-8-sig')
data = csv.reader(f)
header = next(data)
print(header)

i = 1
for row in data:
    print(row)
    if i > 5:
        break
    i += 1
f.close()

#---------------------------------------------------------------------
# 유임 승차 대 무임 승차 비율 계산
#---------------------------------------------------------------------
# f = open('../PublicData/DATA/subwayfee.csv', encoding = 'utf-8-sig')
# data = csv.reader(f)
# header = next(data)
# max_rate = 0
# rate = 0
#
# for row in data:
#     for i in range(4,8):  # 필요한 컬럼만 가져오기 위해
#         row[i] = int(row[i])  # int로 타입 캐스팅
#     rate = row[4]/row[6]   # 유임승차 / 무임승차 <- row[6]이 0인 값이 있을수도 -> Error
#     if rate > max_rate:
#         max_rate=rate
# print(max_rate)
#
# f.close()

# 무임승차 인원이 0인 역 찾기

f = open('../DATA/subwayfee.csv', encoding ='utf-8-sig')
data = csv.reader(f)
header = next(data)
rate = 0

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    rate = row[4]/(row[4]+row[6])
    if row[6] == 0:   # 6개
        print(row)

f.close()

# 최대 무임 승차 비율 확인

f = open('../DATA/subwayfee.csv', encoding ='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0  # 초기값은 가장 작은 값으로

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    if row[6] != 0:  # 무임승차가 0인 값 제외
        # 무임승차(%) = 무임승차 수 * 100 /(유임 승차 수 + 무임 승차 수)
        rate = (row[6]*100)/(row[4]+row[6])
        if rate > max_rate:  # 최대값 업데이트
            max_rate = rate
            print(row, round(rate,2), '%')  # 업데이트 상황 파악 가능
f.close()

# -------------------------------------------------------------------
# 최대 유임승차 인원이 있는 역은?
# 10만명 넘게 승하차 하는 역에서 유임 승차 비율이 제일 높은 역
# -------------------------------------------------------------------
f = open('../DATA/subwayfee.csv', encoding ='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0
max_row = []
max_total_num=0
for	row	in data	:
    for	i in range(4,8)	:
        row[i] = int(row[i])
    total_count = row[4] + row[6] #	유임승차수 +	무임승차수
    if (row[6] != 0) and (total_count > 100000):
        rate = row[4]/total_count
        if rate > max_rate :
            max_rate = rate
            max_row = row
            max_total_num = total_count
print()
print(f"호선명:{max_row[1]}, 역이름:{max_row[3]}, 전체 인원:{max_total_num:,}명, 유임승차인원:{max_row[4]:,}명, 유임승차 비율: {round(max_rate *	100,2):,}%")
# :, -> 1000 단위 콤마 추가
f.close()

# -------------------------------------------------------------------
# 유임 승차 비율이 50%이하이고 총 승차 인원이 10000명 이상인 것 모두 출력
# 유임 승차 비율이 가장 낮은 역의 비율을 파이차트로 표시
# -------------------------------------------------------------------
import matplotlib.pyplot as plt
import platform

f = open('../DATA/subwayfee.csv', encoding ='utf-8-sig')
data = csv.reader(f)
header = next(data)

min_rate = 100
min_row = []
min_total_count=0

for row in data:
    for i in [4,6]:
        row[i] = int(row[i])  # 타입 캐스팅
    total_count = row[4] + row[6]  # 승차 인원 더하기

    if (row[6] != 0) and (total_count >= 10000):  # 조건 1
        rate = row[4]/total_count  # 유임승차율
        if rate<= 0.5:
            print(row, round(rate,2))
            if rate<min_rate:
                min_rate = rate # 업데이트
                min_row = row  # 해당 조건에 맞는 row 저장  # 업데이트
                min_total_count = total_count  # 유임승차 + 무임승차  # 업데이트
f.close()
print()
print(f'유임 승차 비율이 가장 낮은 역: {min_row[3]}')
print(f'전체 인원:{min_total_count:,}명, 유임승차인원:{min_row[4]:,}명, 유임승차비율:{round(min_rate*100,1)}%')

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.title(min_row[3]+"역 유,무임 승차 비율")
label=['유임승차','무임승차']
values=[min_row[4],min_row[6]]
plt.pie(values,labels=label,autopct='%.1f%%')
plt.legend(loc=2)
plt.show()

print()
# -------------------------------------------------------------------
# 승하차 인원이 가장 많은 역
# -------------------------------------------------------------------

max = [0] * 4
max_station = [''] * 4
label = ['유임승차','유임하차','무임승차','무임하차']  # in data -> idx = 4 5 6 7 / in label -> 0 1 2 3

with open('../DATA/subwayfee.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):
            row[i] = int(row[i])
            if row[i] > max[i-4]:  # 업데이트
                max[i-4] = row[i]
                max_station[i-4] = row[3]+' '+row[1]  # row[3] : 지하철역 / row[1] : 노선

for i in range(4):
    print(f'{label[i]}: {max_station[i]} {max[i]:,}명')

print()
# -------------------------------------------------------------------
# 전체 지하철 역 파이차트 분석
# -------------------------------------------------------------------

label = ['유임승차', '유임하차', '무임승차', '무임하차']
color_list = ['#ff9999', '#ffc000',	'#8fd9b6', '#d395d0']
pic_count = 0

with open('../DATA/subwayfee.csv', encoding='utf-8-sig') as f:

    data = csv.reader(f)
    next(data)

    if(platform.system() == 'Windows'):
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

    for	row	in data:
        for	i in range(4, 8):
            row[i] = int(row[i])
        print(row)

        plt.figure(dpi=100)	#	저장할 그림파일의 dpi	설정
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels=label,	colors=color_list, autopct = '%.1f%%', shadow = True)
        plt.savefig('img/'+ row[3] + ' ' + row[1] + '.png')  # img/지하철역 이름 + 호선번호.png
        plt.close() # 파이차트 닫기

        pic_count += 1
        if	pic_count >= 10:break