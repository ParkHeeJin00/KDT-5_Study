from bs4 import BeautifulSoup
from urllib.request import urlopen

html_text='<span class="red">Heavens! what a virulent attack!</span>'
soup = BeautifulSoup(html_text, 'html.parser')

# attr 사용
object_tag = soup.find('span')
print('object_tag:', object_tag)
print('attrs:', object_tag.attrs) # attrs - dict 형태로 반환
print('value:', object_tag.attrs['class'])
print('text:', object_tag.text)
print('-'*70)

# css 속성을 이용한 태그 검색 (등장 인물 검색)

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, "html.parser")
# 등장인물의 이름: 녹색
nameList = soup.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.string.replace('\n',' '))   # \n이 존재해서 replace로 공백으로 전환
print('-'*70)

#  특정 단어 찾기
princeList = soup.find_all(string='the prince')
print(princeList)
print('the prince count: ', len(princeList))
print('-'*70)

# 자식 : children
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))  # 중간에 \n도 인식해서 개수에 포함 시킴 -> 공백으로 출력
# 행수 + \n 수
for child in table_tag.children:
    print(child)
print('-' * 30)
print('-'*70)

# 자손: descendants
desc = soup.find('table', {'id': 'giftList'}).descendants
print(type(desc))  # list형 아님 why??
list_desc = list(desc)
print('descendants 개수: ', len(list_desc)) # 모든 태그 수 + \n 개수
for tag in list_desc:
    print(tag)
print('-'*70)

# 형제 다루기

# next_siblings 속성
for sibling in soup.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
print('-'*70)

# previous_siblings 속성 - 거꾸로 올라가면서 출력
for sibling in soup.find('tr', {'id': 'gift2'}).previous_siblings:
    print(sibling)
print('-'*70)

# next_sibling, previous_sibling
sibling1 = soup.find('tr', {'id': 'gift3'}).next_sibling
print('sibling1:', sibling1)  # \n 이라서 출력 X
print(ord(sibling1))  # ord(문자): 문자의 Unicode 정수를 리턴

# next_sibling.next_sibling 이용
sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
print(sibling2)
print('-'*70)

# 부모 다루기
img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)
print('-'*70)

