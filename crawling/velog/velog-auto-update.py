#selenium 라이브러리
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from time import sleep

#기타 라이브러리
import random
import pandas as pd
from time_converter import convert_relative_time_to_now
from selenium.webdriver.common.by import By
# xpath를 사용하기 위한 라이브러리
from lxml import etree
import json
#게시글 목록의 HTML source를 읽어옴
driver = webdriver.Chrome() 

#수집한 데이터를 저장할 리스트
data_list = []
data_list_with_text = []

# csv로 부터 가져온 url
stored_url_list = pd.read_csv('./url_list.csv', header=None)
stored_url_set = list(dict.fromkeys(stored_url_list[0]))
old_url_list = pd.read_csv('./old_url_list.csv',header=None)
old_url_list = list(dict.fromkeys(old_url_list[0]))

updated_url_list = list(dict.fromkeys(stored_url_list[0]))
# sleep time 현재 테스트 해보려는 중
testUrl = list({"https://velog.io/@unreal77/unreal-공부-ht12qgy5"})
count = 0
for url in stored_url_set:
    targetUrl = url    
    if count == 1000:
        break
    count += 1
    print("현재 수집 중인 갯수", count-1)
    if targetUrl in old_url_list:
        print("이미 수집한 URL", targetUrl)
        count -= 1
        updated_url_list.remove(targetUrl)
        continue
    try:
        driver.get(targetUrl)
        random_sleep_time = round(random.uniform(3,3.5), 2)
        time.sleep(random_sleep_time)
        print("페이지 로딩 완료")
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        # lxml의 etree로 변환
        dom = etree.HTML(str(soup))

        # 게시글 정보 헤더
        header = soup.find('div',{"class":"head-wrapper"})

        # 유저, 작성시간
        postInfo = header.find('div',{"class":"information"})
        info = postInfo.find_all('span')

        title = header.find('h1').text
        userName = header.find('span',{"class":"username"}).text
        date = info[2].text
        converted_data = convert_relative_time_to_now(date)
        
        # 게시글 내용
        target = dom.xpath('//*[@id="root"]/div[2]/div[4]')
        html_content = etree.tostring(target[0], encoding='unicode', pretty_print=True)  # HTML 태그 포함한 내용
        # HTML 태그 제거한 text만 가져오기
        soup_for_text = BeautifulSoup(html_content, 'html.parser')
        text_content = soup_for_text.get_text(strip=True)

        # 좋아요 수
        infoDiv = soup.find('div',{"class":"information"}).find_next_sibling('div')
        spands = infoDiv.find_all('span')
        likeCount = spands[1].text
        
        # 댓글 목록
        comment_data_list = []
        comment_div_list = soup.find_all('div',{"class":"comment"})
        for comment in comment_div_list:
            comment_user = comment.find('div',{"class":"username"}).text

            comment_date = comment.find('div',{"class":"date"}).text
            comment_date = convert_relative_time_to_now(comment_date)

            comment_content = comment.find('p').text
            comment_data_list.append({"commentUser":comment_user, "commentDate":comment_date, "commentContent":comment_content})
        # 수집한 데이터를 저장
        data_list.append({"title":title, "userName":userName, "date":converted_data, "content":html_content, 
                        "likeCount":likeCount,
                        "comments":comment_data_list})
        data_list_with_text.append({"title":title, "userName":userName, "date":converted_data, "content":text_content,
                        "likeCount":likeCount,
                        "comments":comment_data_list})
        old_url_list.append(targetUrl)
        print("게시글 수집 완료")
        sleep(1)
        print("다음 게시글로 이동합니다.")
    except Exception as e:
        print(f"페이지 로딩 실패: {e}")
        print("URL을 열 수 없습니다.")
        continue
    
    
df = pd.DataFrame(data_list)
text_df = pd.DataFrame(data_list_with_text)
# 데이터 저장 접두사는 오늘의 datetime
today = datetime.today().strftime("%Y%m%d_%H%M%S")
df.to_json(f"velog_data_{today}.json", orient='records', lines=False, force_ascii=False, indent=4)
df.to_csv(f"velog_data_{today}.csv", index=False, encoding='utf-8-sig')
text_df.to_json(f"velog_text_data_{today}_text.json", orient='records', lines=False, force_ascii=False, indent=4)

# 수집한 URL Old url list에 append 하여 저
old_url_list = pd.DataFrame(old_url_list, columns=['url'])
old_url_list.to_csv('old_url_list.csv', header=False, index=False)
# 수정 된 updated_url_list을 통해 url_list.csv 업데이트
new_url_list = pd.DataFrame(updated_url_list, columns=['url'])
new_url_list.to_csv('url_list.csv', header=False, index=False)
driver.quit()
print("수집이 완료되었습니다.")



