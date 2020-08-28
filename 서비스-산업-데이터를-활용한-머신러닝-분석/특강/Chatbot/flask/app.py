from datetime import datetime
from flask import Flask, render_template
import random


app = Flask(__name__)

@app.route('/') # 이 경로로 들어왔을 때
def hello_world(): # 이 함수가 실행된다
    return render_template('index.html')

@app.route('/mulcam') #사용자가 mulcam 경로로 오면
def mulcam():
    return '멀캠에서 취업하자!!'
# 이런 결과물을 주겠다.

@app.route('/dday')
def dday():
    today = datetime.now()
    new_year = datetime(2020, 1, 1)
    result = new_year - today
    return f'<h1>더 성숙해지기까지 {result.days}일 남았습니다!</h1>' # fstring 사용해서 print

# @app.route('/greeting/<string:name>')
# def greeting(name):
#     return render_template('greeting.html', html_name = name)

@app.route('/greeting_if/<string:name>')
def greeting(name):
    return render_template('greeting_if.html', html_name = name)

# 숫자를 입력하면 세제곱 결과를 돌려주는 페이지.

# @app.route('/cube/<int:number>')
# def cube(number):
#     return f'{number}의 세제곱의 값은 {number**3}입니다.'

@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    return render_template('cube.html', number_html = number, result_html = result)

# 인원 수에 맞게 메뉴를 추천해주는 페이지

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['보쌈수육정식', '고추잡채덮밥', '돼지불백', '샐러드', '히레카츠']
    order = random.sample(menu, people)
    return str(order)




@app.route('/movie')
def movie():
    movie_list = ['나이브스 아웃', '조커', '엔드게임']
    return render_template('movies.html', movie_list=movie_list)


# 플라스크 통한 요청 응답 구조

from flask import request

# 핑으로 오묜 사용자가 요청할 수 있게 ping html 열어.
# -> 그러면 그 ping이라는 페이지에서 input 받고 pong으로 쏴줌.

@app.route('/ping')
def ping():
    return render_template('ping.html')

# 사용자에게 돌려줄 웹페이지는 pong

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age = age )

## 검색하는 웹페이지

@app.route('/naver')
def naver():
    return render_template('naver.html')

# 실행해보면 처음 그냥form 화면 나오고
# 입력 값에 검색어 넣으면 네이버 화면 뜸
# 나중에 직접 해보고 캡쳐해서 넣기

# 사용자에게 입력 받으면 요청을 구글 서버로 보내서 출력하도록 하는 로직 구현!

@app.route('/google')
def google():
    return render_template('google.html')


# return 함수 바꾸고 싶으면, hello world 내용 수정하고, terminal에서 ctrl c 눌러서 서버 종료하고, 다시 flask run 해서 시작하면 된다.


# 그런데 내용 수정할 때마다 이렇게 하면 귀찮으니까, 
# 아래의 내용을 
# app.py 가장 하단에위치
# 앞으로 flask run으로 서버를 켜는 게 아니라, python app.py로 서버를 실행한다.
# 내용이 바뀌어도 서버를 껏다 켜지 않아도 된다.

if __name__ == '__main__':
    app.run(debug = True)