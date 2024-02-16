from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import requests


html = urlopen('https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')

bs = BeautifulSoup(html, 'html.parser')

weather = bs.find('div',{'class':'api_subject_bx'})

spot = weather.find('h2',{'class':'title'})
tem = weather.find('div',{'class':'temperature_text'})
whe = weather.find('span',{'class':'weather before_slash'})
airlist = weather.find('ul',{'class':'today_chart_list'}).find_all('li')
timewhe = weather.find('div',{'class':'graph_inner _hourly_weather'}).find_all('li')


print('현재 위치: ' ,spot.text)
print('현재 온도:' ,tem.text)
print('날씨 상태: ' ,whe.text)
print('공기 상태:')
for i in airlist:
    print(i.text.strip())
print('-'*30)
print('시간대별 날씨 및 온도')
print('-'*30)
for i in timewhe:
    print(i.text.strip())



