from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.coffeebeankorea.com/store/store.asp')

# 팝업창 생성됨
# execute_script(‘자바스크립트’)
driver.execute_script('storePop2(1)')

html = driver.page_source # page_source: 해당 웹페이지의 소스가 저장됨
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify()) # HTML 소스를 보기 좋게 출력( 자동으로 들여쓰기 )


# 매장 이름
store_names = soup.select('div.store_txt > p.name > span')
store_name_list = []
for name in store_names:
    store_name_list.append(name.get_text())
print('매장 개수: ', len(store_name_list))
print(store_name_list)

# 매장 주소
store_addresses = soup.select('p.address > span')
store_address_list = []
for addr in store_addresses:
    print(addr.get_text())
    store_address_list.append(addr.get_text())
driver.quit() # web driver 종료

