import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd


# 데이터를 CSV파일로 저장
csvFile = open('test.csv', 'w', encoding='UTF-8')
try:
    writer = csv.writer(csvFile)
    # writer.writerow : 행에 입력할 값 입력
    writer.writerow(('number', 'number+2', '(number+2)^2')) # 헤더 정보  # 묶기 위해 괄호가 두개
    for i in range(10):
        writer.writerow((i, i+2, pow(i+2, 2)))
except Exception as e:
    print(e)
finally: #  예외 발생 유무와 상관없이 무조건 실행되어야 하는 구문
    csvFile.close()


# 테이블 데이터를 CSV로 저장

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# 두 개의 테이블 중에 첫 번째 테이블 사용
table = bs.find_all('table', {'class':'wikitable'})[0]  # find_all : 리스트 리턴
# 2개의 테이블 중에 첫번째 테이블만 가져옴
rows = table.find_all('tr')
csvFile = open('editors.csv', 'wt', encoding='utf-8') # t: text mode
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['th', 'td']): # 한 행의 <th>,<td> 데이터 가져옴
            print(cell.text.strip())
            csvRow.append(cell.text.strip())
        writer.writerow(csvRow) # 한 행씩 CSV파일로 저장
finally:
    csvFile.close()

# html_table_parser 사용 예제

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# 두 개의 테이블 중에 첫 번째 테이블 사용: find_all() 사용
#table = bs.find_all('table', {'class':'wikitable'})[0]
table = bs.find('table', {'class':'wikitable'})
table_data = parse.make2d(table) # 2차원 리스트 형태로 변환
# 테이블의 2행을 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1]) # 제대로 나온 헤더

# Pandas DataFrame으로 저장 (2행부터 데이터 저장, 1행은 column 이름으로 사용)
df = pd.DataFrame(table_data[2:], columns=table_data[1]) # 2행부터 데이터
print(df.head())

# csv 파일로 저장
csvFile = open('editors1.csv', 'w', encoding='utf-8') # t: text mode
writer = csv.writer(csvFile)
for row in table_data[1:]: # 0~1행은 자동으로 헤더로 들어감
    writer.writerow(row)
csvFile.close()



# sql 확인
