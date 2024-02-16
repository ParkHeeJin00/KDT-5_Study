from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


# # 임의의 위키 페이지에서 모든 링크 목록 가져오기
# html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')
# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
# print('-'*70)
#
#
# html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')
# body_content = bs.find('div', {'id': 'bodyContent'})
# pattern = '^(/wiki/)((?!:).)*$'
# for link in body_content.find_all('a', href=re.compile(pattern)):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
#

# 링크간 무작위 이동하기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

#random.seed(datetime.datetime.now())
random.seed(None) # Python 3.9 이상
# def getLinks(articleUrl):
#     html = urlopen('https://en.wikipedia.org' + articleUrl)
#     bs = BeautifulSoup(html, 'html.parser')
#     bodyContent = bs.find('div', {'id': 'bodyContent'})
#     wikiUrl = bodyContent.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
#     return wikiUrl
#
# links = getLinks('/wiki/Kevin_Bacon')
# print('links 길이: ', len(links))
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newArticle)
#     links = getLinks(newArticle)

# getLinks() 함수 수정
# pages = set() # 중복안됨
# count = 0
# def getLinks(pageUrl):
#     global pages
#     global count
#     html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     print(len(bs.find_all('a', href=re.compile('^(/wiki/)'))))
#     for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages: #
#
#                 # 새로운 페이지 발견
#                 newPage = link.attrs['href']
#
#                 count += 1
#                 print(f'[{count}]: {newPage}'.format(count, newPage))
#                 pages.add(newPage) # 세트에 추가
#
#                 getLinks(newPage) # 재귀함수

#getLinks('')

# 전체 사이트 데이터 수집 소스
pages = set()
count = 0
def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text()) # <h1>태그 검색

        print(bs.find(id='mw-content-text').find('p').text)

        #print(bs.find('div', attrs={'id': 'mw-content-text'}).find('p').text)
    except AttributeError as e:
        print('this page is missing something! Continuing: ', e)

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'*40)
                count += 1
                print(f'[{count}]: {newPage}')
                print('-' * 40)
                pages.add(newPage)
                getLinks(newPage)
# getLinks('')

# 네이버 블로그 검색
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

query='ChatGPT'
url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'html.parser')
html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
blog_results = soup.select('a.title_link')
print(f'검색 결과수 : {len(blog_results)}')
for blog_title in blog_results:
    title = blog_title.text
    link = blog_title['href']
    print(f'{title}, [{link}]')