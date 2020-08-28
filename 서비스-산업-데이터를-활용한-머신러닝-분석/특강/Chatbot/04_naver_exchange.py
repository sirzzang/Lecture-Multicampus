# 실습 : 네이버 금융 - 시장지표 - 원달러 환율 가져오기.

# 0. 관련 모듈 import

import requests
from bs4 import BeautifulSoup

# 1. 문자열 형태로 문서 가져오기

url = "https://finance.naver.com/marketindex/"
url_page = requests.get(url).text

# 2. BeautifulSoup 클래스 객체 받기

url_soup = BeautifulSoup(url_page, 'html.parser')
print(type(url_soup))

# 3. 원하는 선택자 내용 가져오기

won_dollar = url_soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").text
# #exchangeList > li.on > a.head.usd > div > span.value : 이거 어떻게 잡으면 될까 -> 너무 selector가 너무 길어.
# span.value라고 그냥 잡으면 너무 여러 가지 나올 수 있음.

# 4. 결과물 출력

print(won_dollar)
