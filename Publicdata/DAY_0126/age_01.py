import csv
f = open('../DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
print(header)
# row[0] : 행정기관
for row in data:
    if '산격3동' in row[0]:  # 산격3동만 포함된 행 출력
        print(row)

f.close()