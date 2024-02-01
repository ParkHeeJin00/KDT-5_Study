import csv

f = open('../DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)


result = []
for row in data:
    if '산격3동' in row[0]:  # '산격3동'이 포함된 행만 출력
        for data in row[3:]:   # 0세 ~ 100세 이상까지 자료를 리스트에 추가
            result.append(data)
print(result)
f.close()