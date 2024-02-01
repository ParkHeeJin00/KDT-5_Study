import pandas as pd
import matplotlib.pyplot as plt
import csv
import koreanize_matplotlib

f = open('../DATA/gender.csv', encoding='utf-8-sig')
data = csv.reader(f)

i = 1
for row in data:
    if i == 10: break
    if '대구광역시' in row[0]:
        maleNum = int(row[104].replace(',',''))
        femaleNum = int(row[207].replace(',',''))

        plt.subplot(3,3,i)
        plt.rc('font', size=5)
        plt.pie([maleNum, femaleNum], labels = ['남성', '여성'], startangle=90, autopct='%.1f%%')
        i += 1
        plt.title(row[0])

plt.suptitle('대구광역시 구별 남녀 인구 비율')
plt.show()