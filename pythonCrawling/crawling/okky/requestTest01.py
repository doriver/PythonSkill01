import requests 

# 가져올 url 문자열로 입력
url = 'https://okky.kr/articles/1517562?topic=life&page=100'
response = requests.get(url)
html_text = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_text, "html.parser")

json_data = soup.select_one("#__NEXT_DATA__").get_text()

import json
json_obj = json.loads(json_data)
print(json_obj['props']['pageProps']['result']['title']) # 올해 프로젝트 탈추각
print(json_obj['props']['pageProps']['result']['content']['text']) # 잘 가져옴
print(json_obj['props']['pageProps']['result']['content']['dateCreated']) # 2024-10-17T09:35:30
print(json_obj['props']['pageProps']['result']['viewCount']) # 712
print(json_obj['props']['pageProps']['result']['assentCount']) # 2
print(json_obj['props']['pageProps']['result']['displayAuthor']['nickname']) # 위카룬
# print(json_obj['props']['pageProps']['result'][''])

# 이방법으로는 댓글을 못가져옴, 나머진 가져올수 있을듯?
