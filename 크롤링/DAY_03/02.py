from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# chromedriver 자동 다운로드 소스
driver = webdriver.Chrome()
driver.get('https://www.naver.com')
print(driver.current_url)
sleep(2)
driver.close()# 하나의 탭만 종료
driver.quit() # webdriver 전체 종료


# selenium 사용
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.google.com')
print(driver.current_url) # 현재 접속한 url 정보를 가져옴
print(driver.title)
print(driver.page_source)
driver.implicitly_wait(time_to_wait=5) # 수행이 끝나면 자동으로 끝나는데 최대 5초 기다려줌
driver.close()
driver.quit()

# element 접근 에제
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)
# find_element(By.CLASS_NAME, '클래스이름'): 하나의 클래스 이름 검색
name = driver.find_element(By.CLASS_NAME, "green")
print(name.text)
print('-' * 20)
# find_elements(By.CLASS_NAME, '클래스이름'): 해당 클래스 이름을 모두 검색
nameList = driver.find_elements(By.CLASS_NAME, "green")
for name in nameList:
    print(name.text)
driver.quit()

