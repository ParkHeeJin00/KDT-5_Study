from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import requests


# 01
html = urlopen('https://www.daangn.com/hot_articles')
print(type(html))
print(html.read())

print('-'*70)
# 02
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs) # 전체 html 코드를 가짐
print(bs.h1) # h1 태그 포함 문자열 가져옴 # 첫번째 h1태그만 반환
print(bs.h1.string) # .string: 태그 내부의 문자열만 가져옴
print(bs.title)
print('title:',bs.title.string)

print('-'*70)
# 03
def getTitle(url, tag):
    try:
        html = urlopen(url)
    # 에러발생 - None 리턴
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        value = bsObj.body.find(tag)
        # find : 특정한 태그 찾아주는 함수
    # 에러발생 : h2태그가 없는 경우 - None 리턴
    except AttributeError as e:
        return None
    # error가 발생하지 않으면 value 리턴
    return value

tag='h2'  # h1이나 title은 출력됨 - error 발생X
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag)

if value == None:
    print(f'{tag} could not be found')
else:
    print(value)

print('-'*70)
# 04
url = 'http://www.pythonscraping.com/pages/page1.html'
# html 객체에 url에서 불러온 데이터 저장
html = requests.get(url)
print('html.encoding:',html.encoding)
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

print()
print('h1.string:',soup.h1.string)

print('-'*70)

