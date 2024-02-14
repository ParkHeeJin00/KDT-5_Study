from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://google.com')
#driver.implicitly_wait(3)
search_box = driver.find_element(By.NAME, 'q') # google 검색창
search_box.send_keys('Python')
search_box.submit() # 검색 버튼 누름 -> 구글에 Python 검색, 전송

time.sleep(3)

# 검색결과의 타이틀이 <div class=“g”> 내부의 <h3> 태그에 정의되어 있음
search_results = driver.find_elements(By.CSS_SELECTOR, "div.g") # div 태그 중 class가 g인
print(len(search_results))
for result in search_results:
    title_element = result.find_element(By.CSS_SELECTOR, "h3") # h3 태그 찾기
    title = title_element.text.strip()
    print(f"{title}")
driver.quit()