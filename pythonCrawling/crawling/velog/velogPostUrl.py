from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time


driver = webdriver.Chrome()
driver.get("https://velog.io/recent")
time.sleep(2 + random.random())

actions = ActionChains(driver)
from urllib.parse import unquote

postUrls=[]
startIndex = 0

for i in range(5):
    try:
        liList = driver.find_elements(By.CSS_SELECTOR, "ul.PostCardGrid_block__AcTqY > li.PostCard_block__FTMsy")

        # post URL 수집
        for i in range(startIndex, len(liList) -1):
            targetPost = liList[i]
            postLink = targetPost.find_element(By.CSS_SELECTOR, 'a.VLink_block__Uwj4P').get_attribute("href")
            postUrls.append(unquote(postLink)) # unquote해주면 url에 한글나옴
            print(f"   ====    ====  {i}   ====    ====   ")

        # 무한스크롤에서 터치하면 스크롤 확장되는 요소
        lastLi = driver.find_element(By.CLASS_NAME, 'PostCard_skeletonBlock__Ov1qn') 
        startIndex = liList.index(lastLi) # 마지막으로 이동한다음엔 이거부터 url 수집하면 될듯?
        # 해당요소로 이동 , 이동하면 post 20개 증가
        actions.move_to_element(lastLi).perform() 
        time.sleep(2 + random.random())

    except:
        print("예외발생")


line = {'postUrls': postUrls} # 여기에 데이터들 넣을꺼
# csv파일로 저장
df = pd.DataFrame(line)
# df.to_csv(r"D:\pythonCrawling\crawling\okky\lifeStory\real\okkyLifeStoryPostUrl.csv",encoding ='utf8',index = False)
df.to_csv("velogUrl.csv",encoding ='utf8',index = False)