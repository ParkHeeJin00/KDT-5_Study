from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request


# 샘플 코드 1
# urllib.error.HTTPError: HTTP Error 406: Not Acceptable 발생
# melon_url = 'https://www.melon.com/chart/index.htm'
# html = urlopen(melon_url)
# soup = BeautifulSoup(html.read(), 'html.parser')
# print(soup)

melon_url = 'https://www.melon.com/chart/index.htm'

# User agent 정보 추가: headers = {'User-Agent': 'Mozilla/5.0'}
# HTTP request 패킷 생성: Request()
urlrequest = Request(melon_url, headers={'User-Agent': 'Mozilla/5.'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
print(soup)