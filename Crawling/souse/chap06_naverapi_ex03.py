"""
    Naver OpenAPI를 활용한 뉴스 검색 Step 2
    - url 접속 및 json 데이터 가져오기
    - 1000개의 뉴스 검색
    - csv 파일 저장
"""
import urllib.request
import datetime
import json
import pandas as pd
import csv


def get_request_url(url):
    client_id = 'octgyKZ1lVHFylPaRFOZ'
    client_secret = 'lfKIMwiF6E'

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            #print(f"[{datetime.datetime.now()}] Url Reqeust Success")
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")


def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    # f"?query={query_string}&start={start}&display={display}"
    parameters = ("?query={}&start={}&display={}".
                  format(query_string, start, display))

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)  # json 문자열을 Python 객체로 변환


def get_post_data(post, json_result_list, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    '''
     strptime()
     - %a: abbreviated weekday name     
     - %b" abbreviated month name
    '''
    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')

    print(f"[{cnt}]", end=" ")
    print(title, end=": ")
    print(pdate, end=" ")
    print(link)
    # print(description)
    # print(org_link)

    # ['번호', '날짜', '제목', '개요', '원본기사링크', '네이버링크']
    json_result_list.append([cnt, pdate, title, description, org_link, link])

    # json_result.append({'cnt': cnt, 'title': title, 'description': description,
    #                     'org_link': org_link, 'link': link, 'pdate': pdate})



def main():
    node = 'news'  # 크롤링 대상
    # search_text = input('검색어를 입력하세요: ')
    search_text = '인공지능'
    cnt = 0
    json_result_list = []

    json_response = get_naver_search(node, search_text, 1, 100)
    #total = json_response['total']
    while (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1
            get_post_data(post, json_result_list, cnt)

        start = json_response['start'] + json_response['display']
        json_response = get_naver_search(node, search_text, start, 100)


    print(f'전체 검색 수: {cnt}')

    # csv 파일로 저장
    # ['번호', '날짜', '제목', '개요', '원본기사링크', '네이버링크']
    columns = ['count', 'date', 'title', 'description', 'org_link', 'link']
    result_df = pd.DataFrame(json_result_list, columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8')

    # with open(f'{search_text}_naver_{node}.csv', 'w', encoding='utf-8') as outfile:
    #     writer = csv.writer(outfile)
    #     writer.writerow(json_result)

if __name__ == '__main__':
    main()
