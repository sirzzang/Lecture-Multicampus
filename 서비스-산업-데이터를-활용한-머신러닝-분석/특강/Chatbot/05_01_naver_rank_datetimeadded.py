# 1) 네이버 실시간 검색어
# 2) 현재 시간까지 같이 출력
# 3) fstring 형식 사용

import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')


now = datetime.now()
print(f'{now} 기준 실시간 검색어')
for name in names:
    print(name.text)
