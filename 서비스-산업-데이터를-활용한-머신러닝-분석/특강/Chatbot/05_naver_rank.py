# 네이버 실시간 검색어

# 일단 선택자만 가져와보자.
# 8위 : #PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(4) > a > span.ah_k

# 이번에는 여러 개 가져와야 하니까 명령어가 좀 달라지겠지

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
searches = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(4) > a > span.ah_k')
# select 뽑으니까 -> list 형태로 나옴. 
# 실제로 text 붙여 보면 오류 : AttributeError: 'list' object has no attribute 'text'

# print(searches)   # 이러면 하나만 나오니까 그 위에 애랑 for loop 돌려야 할 듯?

# 다른 구조 봐보면
# #PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(5) > a > span.ah_k

# li:nth-child(4), ~(5) 이게 문제인듯!

# 아예 전체 다 뽑아올 수 없을까?

# 1) 번호 매기는 거 없애야 할 듯: nth-child 없애!
# 2) a 태그 안에 span태그가 있다.

names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
print(names)
# [<span class="ah_k">최영수</span>, <span class="ah_k">백예린</span>, <span class="ah_k">인터스텔라</span>, <span class="ah_k">네이처셀</span>, <span class="ah_k">박항서</span>, <span class="ah_k">채연</span>, <span class="ah_k">게릿 콜</span>, <span class="ah_k">한국 홍콩</span>, <span class="ah_k">블랙독</span>, <span class="ah_k">3억2400만달러</span>, <span class="ah_k">쥬만지 넥스트레벨</span>, <span class="ah_k">백예린 square</span>, <span class="ah_k">알파홀딩스</span>, <span class="ah_k">장희웅</span>, <span class="ah_k">미세먼지</span>, <span class="ah_k">챔피언스리그</span>, <span class="ah_k">토트넘 뮌헨</span>, <span class="ah_k">김수현</span>, <span class="ah_k">댄싱퀸</span>, <span class="ah_k">에스텍파마</span>]
# 제대로 뽑힌 것 같아.

# 이제 text만 뽑으면 되니까
# for loop 돌리면서 돌리자.

for name in names:
    print(name.text, end = ' ')


# 최영수
# 백예린
# 인터스텔라
# 네이처셀
# 박항서
# 채연
# 게릿 콜
# 한국 홍콩
# 블랙독
# 3억2400만달러
# 쥬만지 넥스트레벨
# 백예린 square
# 장희웅
# 알파홀딩스
# 미세먼지
# 챔피언스리그
# 토트넘 뮌헨
# 김수현
# 에스텍파마
# 댄싱퀸

# 한 줄로 뽑을라면, end = ' '
# 최영수 보니하니 백예린 채연 인터스텔라 네이처셀 박항서 게릿 콜 한국 홍콩 블랙독 3억2400만달러 쥬만지 넥스트레벨 백예린 square 장희웅 토트넘 뮌헨 미세먼지 알파홀딩스 챔피언스리그 김수현 에스텍파마
