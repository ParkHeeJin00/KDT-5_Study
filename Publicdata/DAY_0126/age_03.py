import csv
import matplotlib.pyplot as plt
import  platform
import koreanize_matplotlib

f = open('../DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)

city = ''
result = []
for row in data:
    if '산격3' in row[0]:  # '산격3동'이 포함된 행만 출력
        city = row[0]
        for data in row[3:]:   # 0세 ~ 100세 이상까지 자료를 리스트에 추가
            if ',' in data:
                data = data.replace(',','')
            result.append(int(data))
f.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()