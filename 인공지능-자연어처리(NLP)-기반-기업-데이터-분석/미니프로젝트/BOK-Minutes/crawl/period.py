import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def getPeriodResults(query, day_start, day_end, results):

    base_url = 'https://search.naver.com/search.naver'
    params = {
        'where': 'news',
        'query': query,
        'sm': 'tab_pge',
        'sort': 1,
        'photo': 0,
        'field': 0,
        'pd': 3,
        'ds': '{}.{}.{}'.format(day_start[:4], day_start[4:6], day_start[6:]),
        'de': '{}.{}.{}'.format(day_end[:4], day_end[4:6], day_end[6:]),
        'start': 1,
        'refresh_start': 0,
    }

    resp = requests.get(base_url, params=params)    
    soup = BeautifulSoup(resp.text, 'lxml')
    total_num = int(soup.find('div', {'class': 'title_desc all_my'}).get_text().split('/ ')[-1].strip('건').replace(',', ''))
    total_page = total_num // 10 + 1

    if total_page < 400:
        print(resp.url, resp.status_code)
        print("           총 {} 개의 글, {} 페이지".format(total_num, total_page))
        results.append([total_page, resp.url])
    else:
        d1 = datetime.strptime(day_start,"%Y%m%d")
        d2 = datetime.strptime(day_end,"%Y%m%d")
        mid_date = d1.date() + (d2-d1) / 2
        mid_date_next = mid_date + timedelta(days=1)
        getPeriodResults(query, day_start, mid_date.strftime("%Y%m%d"), results)
        getPeriodResults(query, mid_date_next.strftime("%Y%m%d"), day_end, results)