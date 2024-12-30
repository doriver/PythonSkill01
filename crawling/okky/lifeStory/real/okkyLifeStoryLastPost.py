# okky - 커뮤니티 - 사는얘기
# 마지막 페이지쪽 글detail 부분 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time
import json

import sys
import os
# 프로젝트 루트 경로를 sys.path에 추가
# sys.path.append(os.path.abspath("D:\pythonCrawling"))
sys.path.append(os.path.abspath("D:\pythonCode01"))

# 파이썬에서 다른 .py 파일에 정의된 메서드나 사용하려면 import를 활용
import dataPreProcessing.method.dataMethod01 as dm


driver = webdriver.Chrome()
lines = [] # 여기에 데이터들 넣을꺼
        
driver.get("https://okky.kr/articles/371?topic=life&page=7117")
time.sleep(2 + random.random())

######## 글 뷰 ########
postView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]')

### 글 작성자 부분
writerSection = postView.find_element(By.XPATH, './div[1]/div[1]')
# 작성자 이미지
writerImg = writerSection.find_element(By.CSS_SELECTOR, "div > span > img").get_attribute("src")
# 작성자
writer = writerSection.find_element(By.XPATH, './div/div').text
# 작성 시간 부분
createdAtSection = writerSection.find_elements(By.XPATH, './div/div[2]/span')
# 조회수
_viewCount = writerSection.find_element(By.XPATH, './div/div[2]/div').text
viewCount = dm.convert_k_to_numbers(_viewCount)

### 글 부분
# 글 제목
title = postView.find_element(By.XPATH, './h1').text
# 내용, 이미지
contentBox = postView.find_element(By.XPATH, './div[3]/div/div/div')
# 글 내용
content = contentBox.text
# 글 이미지
img = contentBox.find_element(By.CSS_SELECTOR, 'img').get_attribute("src")
# 좋아요
likeCount = postView.find_element(By.XPATH, './div[4]/div[2]/div/div[1]/span').text


######## 댓글 뷰 ########
replyView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[5]')
postReplyLists = []

###### 댓글들
replyList = replyView.find_elements(By.XPATH, './section/div[3]/ul/li')

for reply in replyList:
### 댓글
    ### 댓글 작성자 부분
    replyWriterSection = reply.find_elements(By.XPATH, './div')[0]
    # 댓글 작성자 이미지
    replyWriterImg = replyWriterSection.find_element(By.XPATH, './div/a/img').get_attribute('src')
    # 댓글 작성자 이름, 작성 시간
    replyNameCreate = replyWriterSection.find_elements(By.XPATH, './div')[1]
    # 작성자 이름
    replyWriter = replyNameCreate.find_element(By.CSS_SELECTOR, 'a').text
    # 작성 시간
    replyCreate = replyNameCreate.find_element(By.XPATH, './div/a').text

    ### 댓글 본문 부분
    replyContentSection = reply.find_elements(By.XPATH, './div')[1]
    text = replyContentSection.find_element(By.CSS_SELECTOR, 'div.tiptap.ProseMirror').text

    postReplyLists.append(
        {"replyWriterImg": replyWriterImg, "replyWriter": replyWriter, "replyCreate": replyCreate, "replyText ":text}
    )

######## 글목록, 페이지 뷰 ########
listPageView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[6]')


lines.append({
            "writerImg": writerImg, "writer": writer, "title": title,
            "content": content, "imgSrc": img, "viewCount": viewCount, "likeCount": likeCount,
            "postReplyLists": postReplyLists # json.dumps(postReplyLists)
        })
# print(lines)


# JSON 문자열로 변환
json_string = json.dumps(lines, ensure_ascii=False, indent=4)

print(json_string)