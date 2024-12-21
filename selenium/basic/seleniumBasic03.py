
# Selenium을 사용하여 Google에서 검색하는 간단한 예제

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# WebDriver 초기화 (Chrome 사용)
# driver = webdriver.Chrome(executable_path="chromedriver 경로")
driver = webdriver.Chrome()

# 웹사이트 열기
driver.get("https://www.google.com")

# # 검색창 찾기
# search_box = driver.find_element(By.NAME, "q")

# # 검색어 입력 및 검색
# search_box.send_keys("Selenium Python")
# search_box.send_keys(Keys.RETURN)

# # 검색 결과 출력
# results = driver.find_elements(By.CSS_SELECTOR, "h3")
# for result in results:
#     print(result.text)

# 브라우저 종료
# driver.quit()