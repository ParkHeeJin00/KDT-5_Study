import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

html = requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
soup = BeautifulSoup(html.text, 'html.parser')
top10 = soup.find('tbody')
top10no = top10.find_all('td',{'class':'no'})
top10title = top10.find_all('a', {'class':'tltle'})
top10link = top10.find_all('a')[::2]

print('-'*30)
print('[네이버 코스피 상위 10대 기업 목록]')
print('-'*30)

for idx in range(10):
    print(f'[{top10no[idx].text:>2}] {top10title[idx].text}')

while True:
    n = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
    if n == -1:
        print('프로그램 종료')
        break
    print(f"https://finance.naver.com/{top10link[n-1]['href']}")
    driver = webdriver.Chrome()
    driver.get(f"https://finance.naver.com/{top10link[n-1]['href']}")
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    info = list(bs.find('dl',{'class':'blind'}).stripped_strings)

    infodict = {}
    for i in info[2:]:
        isplit = i.split()
        if isplit[0] == '종목코드' or isplit[0] =='현재가':
            infodict[isplit[0]] = isplit[1]
        else:
            infodict[isplit[0]] = isplit[-1]
    print(f"종목명: {infodict['종목명']}")
    print(f"종목코드: {infodict['종목코드']}")
    print(f"현재가: {infodict['현재가']}")
    print(f"전일가: {infodict['전일가']}")
    print(f"시가: {infodict['시가']}")
    print(f"고가: {infodict['고가']}")
    print(f"저가: {infodict['저가']}")

    driver.quit()




