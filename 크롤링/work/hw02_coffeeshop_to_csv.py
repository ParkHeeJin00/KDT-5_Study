import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
def print_shop():
    n = 1
    shoplist = []
    for i in range(1,52):
        url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        shops = bs.find('table', {'class': 'tb_store'}).find_all('tr')
        for j in shops[1:]:
            shopinfo = []
            shop = j.select('td')
            print('[{:>3}]: 매장이름: {}, 지역: {},주소: {}, 전화번호: {}'.format(n, shop[1].text, shop[0].text,shop[3].text, shop[5].text))
            n+=1
            for i in [1,0,3,5]:
                shopinfo.append(shop[i].text.strip())
            shoplist.append(shopinfo)
    print(f'전체 매장 수: {len(shoplist)}')
    return shoplist

def shop_to_csv(shoplist):
    filename = 'holly_branches.csv'
    shopDF = pd.DataFrame(shoplist, columns = ['매장이름','위치(시/구)','주소','전화번호'])
    shopDF.to_csv(filename, encoding='utf-8', index=False)
    print(f'{filename} 파일 저장완료')

shoplist = print_shop()
shop_to_csv(shoplist)
