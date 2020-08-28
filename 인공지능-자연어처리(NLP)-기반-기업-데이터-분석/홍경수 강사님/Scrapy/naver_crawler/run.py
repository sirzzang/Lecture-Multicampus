import os
from scrapy.cmdline import execute # 커맨드라인 실행 패키지

# pwd로 경로 변경
# run.py 파일 액세스 위해 파이썬 현재 실행 중인 파일(__file__)의 경로 가져 옴.
os.chdir(os.path.dirname(os.path.realpath(__file__))) 

try:
    execute(["scrapy", "crawl", "naver"]) # cmd 창에서의 scrapy crawl naver 명령.

# 에러 나면 시스템 종료
except SystemExit:
    pass
        