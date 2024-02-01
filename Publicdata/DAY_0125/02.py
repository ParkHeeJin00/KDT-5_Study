import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

# -------------------------------------------------------------------
# 새벽 4시 지하철 승차 전체 인원
# -------------------------------------------------------------------

result = []
total_number = 0

with open('../DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    for row in data:
        row[4:] = map(int, row[4:])
        total_number += row[4]
        result.append(row[4])

print(f'총 지하철 역의 수: {len(result)}')
print(f'새벽 4시 승차인원: {total_number}')

# -------------------------------------------------------------------
# 새벽 4시 지하철 이용 인원 수 (그래프)
# -------------------------------------------------------------------
with open('../DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result = []
    total_number = 0   # 총 몇명 탔는지
    max_num = -1
    max_station = ''

    for row in data:
        row[4:] = map(int, row[4:])
        total_number += row[4]
        result.append(row[4])
        if row[4] > max_num:
            max_num = row[4]  # 업데이트
            max_station = row[3]  # 업데이트
print('새벽 4시 승차 인원 수: {0:,}'.format(total_number))
# print(f'새벽 4시 승차 인원수: {total_number:,}')
print('최대 승차역: {0}, 인원수: {1:}'.format(max_station, max_num))  ## {:.} : 1000단위 쉼표 표시
result.sort()
plt.figure(dpi = 100)
plt.bar(range(len(result)), result)
plt.title('새벽 4시 지하철 승차인원 현황')
plt.show()

# -------------------------------------------------------------------
# 출근 시간대(7-9시) 모든 역의 승차 인원을 내림차순으로 10개 역의 승차 인원을 막대그래프로
# 7시 : [10] / 8시 : [12] / 9시 : [14]
# -------------------------------------------------------------------

with open('../DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    result = []
    total_number = 0   # 총 몇명 탔는지
    max_num = -1
    max_station = ''

    for row in data:
        row[4:] = map(int, row[4:])
        row_sum = sum(row[10:15:2])
        result.append(row_sum)
        if row_sum > max_num:
            max_num = row_sum   # 계속 업데이트
            max_station = row[3] + '(' + row[1] + ')'  # 계속 업데이트
                        #  역이름    /    호선명
print(f'최대 승차 인원역: {max_station} {max_num:,}')
result.sort(reverse=True)  # sort는 원본 변환 함수 / 내림차순으로 정렬

plt.figure(figsize = (10,4))
ax1 = plt.subplot(1,2,1)
plt.title('10개 역의 승차 인원수', size = 12)
plt.bar(range(10),result[:10]) # y값 : 상위 10개 값(내림차순)
plt.ylabel('승차인원수')

ax2 = plt.subplot(1,2,2, sharey = ax1)
plt.title('전체 역의 승차 인원수', size = 12)
plt.bar(range(len(result)), result)

plt.suptitle('출근 시간대 승차 인원 현황\n', size = 20)
plt.tight_layout()   # 여백 정리
plt.show()

# -------------------------------------------------------------------
# 시간대 별 가장 많이 승차하는 역 정보 분석
# -------------------------------------------------------------------

with open('../DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    max = [0] * 23  # 시간대 별 맥스 값
    max_station = [''] * 23 # 시간대 별 맥스 값의 지하철 역 리스트
    xtick_list = []

    for i in range(4,27):
        n = i % 24   # % : 나머지 값   # 4~23 : 4~23 그 값 / 24 : 0 / 25 : 1 / 26 : 2
        xtick_list.append(str(n))

    for row in data:
        row[4:] = map(int, row[4:])
        for j in range(23):
            a = row[j * 2 + 4]
            if a > max[j]:
                max[j] = a
                max_station[j] = xtick_list[j]+'시 '+row[3]

    for i in range(len(max)):
        print(f'[{max_station[i]}]: {max[i]:,}')

if(platform.system() == 'Windows'):
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.figure(figsize=(10,10))
plt.title('시간대 별 최대 승차역 정보')
plt.bar(range(23), max)
plt.xticks(range(23), labels=max_station, rotation = 80)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 시간대 별 승하차 인원
# -------------------------------------------------------------------

with open('../DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    subway_in = [0] * 24   # 승차 인원 저장 리스트
    subway_out = [0] * 24   # 하차 인원 저장 리스트

    for row in data:  # 전체 역 승하차 인원 구하기 위해 반복
        row[4:] = map(int, row[4:])
        for i in range(24):   # 하나의 역에서 24시간 동안 승하차한 인원 구하기
            subway_in[i] += row[4 + i*2]
            subway_out[i] += row[5 + i*2]

    if (platform.system() == 'Windows'):
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

xtick_list = []
for i in range(4,28):
    n = i % 24   # % : 나머지 값   # 4~23 : 4~23 그 값 / 24 : 0 / 25 : 1 / 26 : 2
    xtick_list.append(str(n))



plt.figure(dpi = 100)
plt.title('지하철 시간대 별 승하차 인원 추이' , size = 16)
plt.grid(linestyle = ':')
plt.plot(subway_in, label = '승차')
plt.plot(subway_out, label = '하차')
plt.xticks(range(24), labels=xtick_list)
plt.xlabel('시간')
plt.ylabel('인원 (천만명)')
plt.tight_layout()
plt.show()

