from selenium import webdriver
from selenium.webdriver.common.by import By

# User Agent 정보 추가
agent_option = webdriver.ChromeOptions()
user_agent_string = 'Mozilla/5.0'
agent_option.add_argument('user-agent=' + user_agent_string)
driver = webdriver.Chrome(options=agent_option)
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(5)

# <input>의 이름이 id를 검색
driver.find_element(By.NAME, 'id').send_keys('mybae78')
driver.find_element(By.NAME, 'pw').send_keys('qkrgmlwls1')
#//*[@id="log.login"]
#driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
driver.find_element(By.ID, 'log.login').click()
driver.quit()