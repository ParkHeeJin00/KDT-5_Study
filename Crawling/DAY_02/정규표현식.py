import re


# compile() 사용 안함
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))
print('-'*70)

# compile() 사용
p = re.compile('[a-z]+') # 알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I like apple 123')) # like
print('-'*70)

# match() 함수
m = re.match('[a-z]+', 'pythoN') # 소문자가 1개 이상
print(m) # pytho

m = re.match('[a-z]+', 'PYthon') # 소문자가 1개 이상
print(m) # None

print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython')) # None -> 문자열 처음에 공백
print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN')) # None -> $ : 문자열의 마지막부터 검사
print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))
print('-'*70)

# findall() 함수 - 일치하는 모든 문자열을 리스트로 반환
p = re.compile('[a-z]+') # 알파벳 소문자
print(p.findall('life is too short! Regular expression test')) # 리스트로 반환
print('-'*70)

# search()함수 - 일치하는 첫 번째 문자열만 반환
result = p.search('I like apple 123')
print(result)
print(result.group()) # group(): 일치하는 전체 문자열 리턴
# result = p.findall('I like apple 123')
# print(result)
print('-'*70)

# 전화번호 분석
# ^ .. $ 을 명시해야 정확한 자리수 검사가 이루어짐
tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
print(tel_checker.match('02-123-4567'))
print(tel_checker.match('02-123-4567').group())
print(tel_checker.match('053-950-45678')) # None - 마지막 숫자의 수가 맞지 않음
print(tel_checker.match('053950-4567')) # None - '-'이 없음
print('-'*70)

tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
m = tel_checker.match('02-123-4567')
print(m.groups())
print('group(): ', m.group())
print('group(0): ', m.group(0))
print('group(1): ', m.group(1))
print('group(2,3): ', m.group(2,3))
# 인덱스 반환
print('start(): ', m.start()) # 매칭된 문자열의 시작 인덱스
print('end(): ', m.end()) # 매칭된 문자열의 마지막 인덱스+1
print('-'*70)

cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')
print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567')) # None
print(cell_phone.match('010-1234567')) # None
print('-'*70)

# 전방 탐색

# 전방 긍정 탐색: (문자열이 won을 포함하고 있으면 won 앞의 문자열 리턴)
lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')
lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10:00:01')
print(lookahead2)

# 전방 부정 탐색 (?!): 4자리 숫자 다음에 '-'를 포함하지 않으면 앞의 문자열 리턴
lookahead3 = re.search('\d{4}(?!-)', '010-1234-5678')
print(lookahead3)
print('-'*70)

# 후방 탐색

# 후방 긍정 탐색 ('am' 다음에 문자가 1개 이상 있으면, 해당 문자열 리턴)
lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)
lookbehind2 = re.search('(?<=:).+', 'USD: $51')
print(lookbehind2)

# 후방 부정 탐색('\b': 공백)
# 공백 다음에 $기호가 없고 숫자가 1개 이상이고 공백이 있는 경우
lookbehind4 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples.')
print(lookbehind4)

print('-'*70)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
# 정규식: ('img.*\.jpg'): img 다음에 임의의 한 문자(.)가 0회 이상(*)
# - img.jpg, img1.jpg, imga.jpg 등
img_tag = re.compile('/img/gifts/img.*.jpg')
# find_all()에서 img의 src 속성값에 정규식 사용
images = soup.find_all('img', {'src': img_tag})
for image in images:
    print(image, end=" -> ['src'] 속성: ")
    print(image['src'])
print('-'*70)

# 대소문자 구분없이 특정 단어 검색
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')
princeList = bs.find_all(string='the prince')
print('the prince count: ', len(princeList))
prince_list = bs.find_all(string=re.compile('[T|t]{1}he prince'))
print('T|the prince count:', len(prince_list))
