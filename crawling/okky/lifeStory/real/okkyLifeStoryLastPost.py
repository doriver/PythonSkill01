# okky - 커뮤니티 - 사는얘기
# 페이지 넘어가면서 크롤링 하는거

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time

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
viewCount = writerSection.find_element(By.XPATH, './div/div[2]/div').text

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

###### 댓글들
replyList = replyView.find_elements(By.XPATH, './section/div[3]/ul/li')

### 댓글
reply = replyList[1]

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

######## 글목록, 페이지 뷰 ########
listPageView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[6]')


lines.append({
            "writerImg": writerImg, "writer": writer, "title": title,
            "content": content, "imgSrc": img, "viewCount": viewCount, "likeCount": likeCount,
            "replyWriterImg": replyWriterImg, "replyWriter": replyWriter, "replyCreate": replyCreate, "replyText ":text
        })
print(lines)