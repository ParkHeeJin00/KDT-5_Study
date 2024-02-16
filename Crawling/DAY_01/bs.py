from urllib.request import urlopen
from bs4 import BeautifulSoup


# 1
html = urlopen('https://www.daangn.com/hot_articles')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
# 공백 제거 후 출력
print(bs.h1.string.strip())
print('-'*70)

# 2 태그를 사용하여 요소에 직접 접근하기
html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link", href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link", href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link", href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''
soup = BeautifulSoup(html_example, 'html.parser')
print(soup.title) # <title> 태그 전체를 가져옴
print(soup.title.string) # <title>태그의 텍스트만 리턴
print(soup.title.get_text()) # .string, .text(예전 버전)와 동일한 기능

# title의 상위 태그 포함해서 출력
print(soup.title.parent)
# body 태그 출력
print(soup.body)
# h1 태그 출력
print(soup.h1)
print(soup.h1.string)
# a 태그 출력
print(soup.a) # <a> 태그 포함 출력
print(soup.a.string) # <a> 태그 내부의 텍스트 추출 (google)
print(soup.a['href']) # <a> 태그 내부의 href 속성의 url을 추출
print(soup.a.get('href')) # a['href']와 동일 기능

# find 함수
print(soup.find('div'))

# div 태그 중에서 id가 text_id2인 태그를 추출해라
print(soup.find('div', {'id': 'text_id2'}))

div_text = soup.find('div', {'id': 'text_id2'})
print(div_text.text)
# string : 한 개 이상의 child 태그를 가지면 None 반환
print(div_text.string) # None 반환  why? -> p태그 존재
print('-'*70)

# <a class="internal_link", href="/pages/page1.html">Page1</a>
# class가 internal_link인 a 태그를 추출해라
href_link = soup.find('a', {'class': 'internal_link'}) # 딕셔너리 형태
# = href_link = soup.find('a', class_='internal_link') # class_사용: class는 파이썬 예약어
print(href_link) # <a class="internal_link", ...>
print(href_link['href']) # <a>태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href')) # ['href']와 동일 기능
print(href_link.text) # <a> Page1 </a>태그 내부의 텍스트(Page1) 추출
print('-'*70)

# a 태그 내부의 모든 속성 가져오기 : attrs
print('href_link.attrs: ', href_link.attrs) # <a>태그 내부의 모든 속성 출력 -> dict로 반환
print('class 속성값: ', href_link['class']) # class 속성의 value 출력 -> lisg로 반환
print('values():', href_link.attrs.values()) # 모든 속성들의 값 출력
values = list(href_link.attrs.values()) # dictionary 값들을 리스트로 변경!!
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1])) # 인덱스로 접근 가능
print('-'*70)

# href 속성의 값이 'www.google.com'인 항목 검색
# attr = {'속성이름' : '속성값'}
href_value = soup.find(attrs={'href' : 'www.google.com'})
href_value = soup.find('a', attrs={'href': 'www.google.com'})
print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)
print('-'*70)

# span 태그의 속성 가져오기

span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs) # attrs : dict형으로 리턴
print('value:', span_tag.attrs['class']) # 키가 class인 값 리턴 = class 속성의 속성값 리턴
print('text:', span_tag.string)
print('-'*70)

# class 속성 불러오기
tr = '''
<table>
<tr class="passed a b c" id="row1 example"><td>t1</td></tr>
<tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''
table = BeautifulSoup(tr, 'html.parser')
print(table)
for row in table.find_all('tr'):
    print(row.attrs)
print('-'*70)

# find_all() 함수
# 모든 div 태그를 검색 (리스트 형태로 반환)
div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))
for div in div_tags:
    print('-----------------------------------------------')
    print(div)
print('-'*70)

# 모든 a 태그 검색 및 속성 보기
links = soup.find_all('a')
for alink in links:
    print(alink)
    print(f"url:{alink['href']}, text: {alink.string}")
    print()
print('-'*70)

# 여러 <a>태그에서 2개의 class 속성값 검색: 'external_link’, 'internal_link’만 검색
link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags) # list에 담겨서 반환

# <p>태그의 id값이 'first', 'third'인 항목 검색
p_tags = soup.find_all('p', {'id':['first', 'third']})
for p in p_tags: # p_tags는 list형
    print(p)
print('-'*70)

# select_one() 함수
head = soup.select_one('head')
print(head)
print('head.text:', head.text.strip())
print()
h1 = soup.select_one('h1') # 첫 번째 <h1>태그 선택
print(h1)
print('-'*70)

# <h1>태그의 id가 "footer"인 항목 추출
footer = soup.select_one('h1#footer')
print(footer)
class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.string)
print(class_link['href'])
print('-'*70)

#  계층적 하위 태그 접근
# 계층적 접근 - select_one()함수
link1 = soup.select_one('div#link > a.external_link')
print(link1)

# 계층적 접근 - find()함수
link_find = soup.find('div', {'id': 'link'})
external_link = link_find.find('a', {'class': 'external_link'})
print('find external_link: ', external_link)
print('-'*70)

# 계층적 하위 태그 접근 - 공백으로 하위 태그 선언
# 자손 관계의 하위 태그
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)
print('-'*70)

# select() 함수
h1_all = soup.select('h1')  # 모든 <h1> 태그 선택 - list에 담아서 객체에 전달
print('h1_all: ', h1_all)

# html문서의 모든 <a> 태그의 href 값 추출
url_links = soup.select('a')
for link in url_links:
    print(link['href'])
print('-'*70)

# <div id=“class1”> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a') # list에 담아서 객체에 전달
print(div_urls)
print(div_urls[0]['href'])

div_urls2 = soup.select('div#class1 a') # 자손관계 - 공백으로도 구분 가능
print(div_urls2)
print('-'*70)

# <h1 id="heading”>과 <h1 id="footer”> 항목 가져오기
h1 = soup.select('#heading, #footer')
print(h1)

url_links = soup.select('a.external_link, a.internal_link')
print(url_links)
print('-'*70)


national_anthem ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>애국가</title>
</head>
<body>
    <div>
        <p id="title">애국가</p>
        <p class="content">
            동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
        <p class="content">
            이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
            무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
        </p>
    </div>
</body>
</html>
'''
# 제목과 가사 추출
soup = BeautifulSoup(national_anthem, 'html.parser')
print(soup.select_one('p#title').string)
contents = soup.select('p.content')
for content in contents:
    print(content.text)

