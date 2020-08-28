import requests
from bs4 import BeautifulSoup
import re

def getNaverNewsLinks(url, results, link_pattern=None, press_list=None):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    news_list = soup.find('ul', {'class': 'type01'})
    for news in news_list:
        print(news)
    return results