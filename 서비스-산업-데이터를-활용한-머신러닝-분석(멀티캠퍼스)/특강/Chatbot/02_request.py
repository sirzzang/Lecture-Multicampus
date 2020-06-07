import requests

# 1. 요청 보내기
# result = requests.get('https://naver.com')
# print(result)

# 2. Response 객체를 문자열로 변환해서 받아보기
# naver 웹페이지에 있는 모든 문서 상의 객체들이 다 들어오고,
# type을 문자열로서 바꿔서 잘 들어옴 -> class 'str'
# result = requests.get('https://naver.com').text
# print(result)
# print(type(result))

# 3. Response 객체를 통해 상태 코드 받아보기
# http 상태 코드 -> https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C
# 1xx(조건부 응답), 2xx(성공), ...
# 200이면 요청 잘 받은 것.
result = requests.get('https://naver.com').status_code
print(result)
if result == 200:
    print('접속 성공')
elif result == 404:
    print('페이지가 없네요...')