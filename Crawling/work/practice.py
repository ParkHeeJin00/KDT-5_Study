import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

html = requests.get('https://www.jobkorea.co.kr/Recruit/GI_Read/43965451?rPageCode=SL&logpath=21')
soup = BeautifulSoup(html.text, 'html.parser')
infoname = soup.select('dl.tbList>dt')
info = soup.select('dl.tbList>dd')
print(infoname)
print(info)