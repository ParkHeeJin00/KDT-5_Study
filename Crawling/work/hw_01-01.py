from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import requests

print('National Weather Service Scraping')
print('-'*40)


html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
bs = BeautifulSoup(html.read(), 'html.parser')

def scraping_use_find(bs):

    print('[find 함수 사용]')
    print('총 tomestone-container 검색 개수:', len(bs.find_all('li', {'class': 'forecast-tombstone'})))
    print('-'*80)
    sevenlist = bs.find_all('li', {'class': 'forecast-tombstone'})

    for i in sevenlist[1:]:
        sevenlistp = i.find_all('p')
        print('[Period]:',sevenlistp[0].text)
        print('[Short desc]:',sevenlistp[2].text)
        print('[Temperature]:',sevenlistp[3].text)
        for j in sevenlistp:
            sevenimg = j.find('img')
            if sevenimg:
                print('[Image desc]:',sevenimg['alt'])
        print('-' * 80)

scraping_use_find(bs)
def scraping_use_select(bs):

    print('[select 함수 사용]')
    print('총 tomestone-container 검색 개수:', len(bs.select('li.forecast-tombstone')))
    print('-' * 80)
    sevenlist = bs.select('li.forecast-tombstone')

    for i in sevenlist[1:]:
        sevenlistp = i.select('p')
        print('[Period]:',sevenlistp[0].text)
        print('[Short desc]:',sevenlistp[2].text)
        print('[Temperature]:',sevenlistp[3].text)
        for j in sevenlistp:
            sevenimg = j.select_one('img')
            if sevenimg:
                print('[Image desc]:',sevenimg['alt'])
        print('-' * 80)


scraping_use_select(bs)