# bs: beautiful soup
# 웹사이트 crawling, scraping 할 때 사용.
# 패키지 깔아야 함.

# 명령어 : pip install bs4

# 네이버 금융 국내증시에서 KOSPI지수 들고오겠다

# 0. 필요한 패키지 import, 변수 선언

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

# 1. 페이지에 요청을 보내서 HTML 문서를, 문자열 형태로 가져온다.

html = requests.get(url).text

# 2. HTML 문서에서 손쉽게 data를 가져오기 위해 BeautifulSoup 클래스 객체를 받아 온다.

soup = BeautifulSoup(html, 'html.parser')       # 변수 선언
print(type(soup))                               # <class 'bs4.BeautifulSoup'>

# 3. 가져올 태그의 선택자를 넣고 결과물을 가져온다.

# copy selector 하는 작업 동일한데.
# #contentarea > div.box_top_submain2 > div.lft > ul : 이걸 바로 넣으면 안 된다.
# BeautifulSoup이 지원하는 방식으로.

# 기본적인 사용법
# 1. .select_one(선택자) : 해당하는 태그 하나
# 2. .select(선택자) : 해당하는 모든 태그

# 우리가 가져오고자 하는 kospi지수 숫자는 하나의 객체이므로, select_one 사용

kospi = soup.select_one('#KOSPI_now')       # KOSPI지수 태그 검사해서 넣으면
print(kospi)                                # <span class="num" id="KOSPI_now">2,105.62</span>
                                            # 모든 게 다 딸려 나오니까

# 애초에 2105.62 있는 애 copy selector하면 "#KOSPI_now"만 나옴.

kospi_text = soup.select_one('#KOSPI_now').text
print(kospi_text)                           # 2105.62

######## 연습할 때 다른 거 가져와보기