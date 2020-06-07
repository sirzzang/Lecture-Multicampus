# 2. Flask 기초

## 2.1. Render Templates

> 단순 문자열을 return하지 않고, 미리 준비해 둔 template을 사용자에게 return한다.



* templates 폴더 생성
  * app.py와 같은 경로에 템플릿 폴더를 생성한다.
  * 반드시 `templates`라는 이름으로 폴더 생성해야 한다.

```python
flask/
	templates/
    
    	
```

* app.py 코드 수정

```python
from flask import Flask, render_template

@app.route('/')
def hello_world():
    return render_template('index.html')
```



## 2.2. Variable Routing

> URL 요청을 통해 사용자에게 임의의 값을 입력 받고, 데이터를 적절하게 가공해서 사용자에게 응답해준다.



* 마찬가지로 미리 준비해 둔 템플릿을 `return`할 수도 있다.

```python
# 세제곱을 return하는 페이지
@app.route('/cube/<int:numbers>')
def cube(number):
    
```

