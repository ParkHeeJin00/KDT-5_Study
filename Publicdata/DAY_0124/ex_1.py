import csv

f = open('../DATA/daegu_hj.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
print(data) # csv_reader
f.close()


# 상위 5개 줄만 프린트 해보기

f = open('../DATA/daegu_hj.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
count=0
for row in data:
    if count > 5:
        break
    else:  # count = 0 1 2 3 4
        print(row)
    count += 1
f.close()


# 데이터 수정 (utf-8-sig 및 ‘\t’ 제거)

# encoding='utf-8-sig'로 '\ufeff' 제거
fin = open('../DATA/daegu_hj.csv', 'r', encoding='utf-8-sig')  # 읽기용으로 파일 open
data = csv.reader(fin, delimiter=',') ## reader -> fin에 저장된 파일 객체를 읽어온 것

# newline='': 한 라인씩 건너 뛰며 저장되는 현상 없앰

### filename : daegu-utf8.csv 로 저장
fout = open('../DATA/daegu_hj-utf8.csv', 'w', newline='', encoding='utf-8-sig')   # 쓰기용으로 파일 open
wr = csv.writer(fout)  ## writer -> fout에 저장된 파일 객체를 변경할 수 있도록 불러온 것 / fout을 바꿀거니까!!!!
for row in data:
    for i in range(len(row)):  # 5번
        row[i] = row[i].replace('\t', '')
    print(row)
    wr.writerow(row) # writerow(row): 한 행씩 파일로 저장

fin.close()
fout.close()
print('파일 저장 완료')


 ### 헤더 및 5개의 데이터 출력하기
f = open('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f, delimiter=',') # delimiter 생략 가능
header = next(data)  ## 현재 위치는 파일의 시작 위치 - next()함수에 의해   ## header가 두개면 next 두번
print(header)  ## 파일의 시작 즉 첫번째 라인만 확인 그리고 그 다음 줄을 읽을 준비 완료 -> data는 2번째 줄을 가르킴

i = 1
# 실제 기온 정보만 가지고 있음 / 헤더 제외
for row in data:
    print(row)
    if i >= 5:
        break # 5개의 데이터를 출력하면 break
    i += 1
f.close()




  ### 대구 최저, 최고 기온 날짜와 온도 구하기
def get_minmax_temp(data):
    '''
                    최고 기온 및 최고 기온의 날짜 구하기
'''
    header = next(data)

    min_temp = 100  # 최저 기온값을 저장할 변수 초기화(가장 큰 값)
    min_date = ''  # 최고 기온의 날짜를 저장할 변수 초기화
    max_temp = -999  # 최고 기온을 저장할 변수 초기화(가장 작은 값)
    max_date = ''

    # row[3] : 최저기온 / row[4] : 최고기온
    for row in data:

        # 최저/최고 기온의 날짜를 저장할 변수 초기화 / float으로 타입 캐스팅
        if row[3] == '':   ## 값이 없는 경우
            row[3] = 100
        row[3] = float(row[3])
        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])

        # 최저/최고 기온 계산
        if row[3] < min_temp:
            ## 계속해서 업데이트
            min_temp = row[3]
            min_date = row[0]
        if row[4] > max_temp:
            ## 계속해서 업데이트
            max_temp = row[4]
            max_date = row[0]  # 날짜:	index[0]

    print('-' * 50)
    print(f'대구 최저 기온 날짜:	{min_date},	온도:	{min_temp}')
    print(f'대구 최고 기온 날짜:	{max_date},	온도:	{max_temp}')

def main():
    f = open('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    get_minmax_temp(data)
    f.close()


main()