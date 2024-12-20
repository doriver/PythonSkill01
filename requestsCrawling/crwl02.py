import requests
from bs4 import BeautifulSoup as bs

# 1. 크롤링할 웹페이지 URL 설정
url = "https://news.naver.com/"

# 2. HTTP GET 요청
response = requests.get(url)

# 3. 요청 성공 여부 확인
if response.status_code == 200:
    # 4. HTML 파싱
    soup = bs(response.text, 'html.parser')

    # 5. 원하는 데이터 추출 (여기서는 헤드라인 뉴스 제목)
    headlines = soup.select(".hdline_article_tit a")  # CSS 선택자로 추출

    print("네이버 뉴스 헤드라인:")
    print(headlines)
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline.get_text(strip=True)}")  # 텍스트만 출력
else:
    print(f"HTTP 요청 실패: {response.status_code}")