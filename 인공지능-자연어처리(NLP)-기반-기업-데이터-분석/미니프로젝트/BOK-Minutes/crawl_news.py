from crawl.period import getPeriodResults
from crawl.links import getNaverNewsLinks
from pprint import pprint

period_results = []
getPeriodResults('금리', day_start='20110701', day_end='20110731', results=period_results)