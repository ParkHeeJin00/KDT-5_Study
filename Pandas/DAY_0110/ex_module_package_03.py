# --------------------------------------------------------------------
# 패키지 사용법
# --------------------------------------------------------------------

# 사용할 모듈 로딩 ------------------------------------------------------
# import 패키지명.모듈명
import urllib.request as req

from http.client import HTTPResponse  # 패키지 내의 모듈 내의 클래스만


# form 패키지명 import 모듈명
from urllib import error, parse

dataObj = req.urlopen('https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')  ## 이미지 저장 가능

print(dataObj)