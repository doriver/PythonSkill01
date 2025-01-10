#selenium 라이브러리
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# selenium의 webdriver를 사용하기 위한 import

options = Options()
options.add_argument("disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 표시 제거
options.add_experimental_option('useAutomationExtension', False)  # 자동화 확장 기능 사용 안 함
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from bs4 import BeautifulSoup
from time import sleep

#기타 라이브러리
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# URL 비교 용
from urllib.parse import unquote
# csv로 부터 가져온 url
stored_url_list = pd.read_csv('./url_list.csv', header=None)
# stored_url_set = set(stored_url_list[0]);
ordered_set = list(dict.fromkeys(stored_url_list[0]))
old_url_list = pd.read_csv('./old_url_list.csv',header=None)
old_url_list = list(dict.fromkeys(old_url_list[0]))

print("기존 URL 수: ", len(ordered_set))
BASE = "https://velog.io/recent"
driver.get(BASE)
time.sleep(5)
print("페이지 로딩 완료")

# 해당 요소로 스크롤 이동
for i in range(50):
    target_element = driver.find_element(By.CLASS_NAME, 'PostCard_skeletonBlock__Ov1qn')
    previous_sibling = target_element.find_element(By.XPATH, "preceding-sibling::*[1]")
    try:
        a_tag = previous_sibling.find_element(By.TAG_NAME, "a")
        href_value = a_tag.get_attribute("href")
        decoded_href = unquote(href_value)
        print("현재 마지막 피드 주소: ",decoded_href)
        if decoded_href in old_url_list or decoded_href in ordered_set:
            print("중복 URL")
            break
    except:
        print("No a tag")
        break    
    actions = ActionChains(driver)
    actions.move_to_element(target_element).perform()
    sleep(2)
    print("스크롤 중...")
print("스크롤 완료!")

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

posts = soup.find_all('li',{"class":"PostCard_block__FTMsy"})

for post in posts:
    a_tag = post.find('a')
    if a_tag and a_tag.get('href'):
        print(a_tag.get('href'))
        if a_tag.get('href') not in ordered_set and a_tag.get('href') not in old_url_list:
            ordered_set.insert(0,a_tag.get('href'))
        else:
            print("중복 URL")
            break
    else:
        print("No URL")

print("크롤링 완료")
print("새로 추가 된 URL 수: ", len(ordered_set) - len(stored_url_list))
# 새로운 url Append
new_url_list = pd.DataFrame(ordered_set, columns=['url'])
new_url_list.to_csv('url_list.csv', header=False, index=False)