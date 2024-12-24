# html쪽에서 막혔다가 , 선택한 selenium객체를 html으로하고, 보기좋게해서, html파일로 만들어버림 

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
lines = [] # 여기에 데이터들 넣을꺼

driver.get("https://okky.kr/articles/1523255?topic=community&page=1")
time.sleep(4)

sel01 = driver.find_elements(By.CSS_SELECTOR, "div.w-full.min-w-0.flex-auto > div.min-w-0.flex-auto > div")
sel02 = sel01[1]
# sel01: <div> 3개   ,  sel02: <div> 1개 ( 안에 div 6개 들어있음 ) 
# 저 6개 div를 선택해야해
sel03 = sel02.find_elements(By.XPATH, './div')
print(len(sel03))


