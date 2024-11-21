import requests
from bs4 import BeautifulSoup

# URL 설정
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 웹페이지 요청
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 기사 제목 추출
# 기사 제목은 주로 특정 클래스나 태그 안에 포함되어 있습니다.
# (아래는 예시로, 실제 크롤링 시 HTML 구조를 확인해야 합니다)
titles = soup.select(".news_tit")  # Naver 뉴스 검색 결과의 경우 .news_tit 클래스에 제목이 포함되어 있음

# 추출한 제목 출력
for idx, title in enumerate(titles, 1):
    print(f"{idx}. {title.text}")
    print(f"링크: {title['href']}")
