from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

driver = webdriver.Chrome()
driver.get("https://velog.io/@ethan-lee/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C")
time.sleep(1 + random.random())

contentHTML = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div').get_attribute("innerHTML")
print(contentHTML.replace('\n', '<br>'))
# Thymeleaf에서  <div th:utext="${html}"></div> 이런식으로 렌더링하면 됨