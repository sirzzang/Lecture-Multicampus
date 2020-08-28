# 파이썬 개발환경 구축

---



## 1. 파이썬 설치

### 1-1. 파이썬 버전 확인

> 바탕화면 - git bash - `python -V`

```bash
$ python -V
```



### 1-2. 파이썬 홈페이지 다운로드



* `Add python 3.8 to PATH` 반드시 체크.
* `Disable Path Limit` 클릭.

![python01](images/python01.jpg)

![python02](images/python02.jpg)



### 1-3. 파이썬 버전 다시 확인

```bash
$ python -V
Python 3.8.0
```



---



## 2. 개발환경 구축

### 2-1. chatbot 폴더 생성

* 마우스 우클릭 - `open with code`

![python03](images/python03.jpg)

### 2-2. git bash 환경 선택

* `bash` : 내장 bash 화면 뜸
  * `menu - view - terminal`
  * `ctrl` + `backtick` 
* `Ctrl + Shift + P` - `Default Shell` - `git bash` 

![python04](images/python04.jpg)



---



## 3. 가상환경 설정

> python 사용해서 개발할 때, global 환경에 모든 패키지를 설치하면 용량이 비대해진다.
>
> 따라서 가상환경을 구축해서, chatbot을 만드는 데에 필요한 패키지만 설치하고 관리한다.



### 3-1. 가상환경 구축

* terminal 창에 다음의 명령어 입력

```bash
$ python -m venv venv
	# 가상환경 만들겠다.
	# 이름은 'venv'.
```

* 파일 목록에 venv 가상환경 만들어짐.

![python05](images/python05.jpg)



### 3-2. 가상환경 진입

* 가상환경 진입 방법: `scripts - activate`로 가면 됨.
* terminal 창에 다음의 명령어 입력.

```bash
$ source venv/Scripts/activate
```

![python06](images/python06.png)

* `VSCode` 기능으로 terminal 창 열면 바로 가상환경으로 진입하도록 설정하기

  * 확장코드 설치: 좌측 하단 마지막 메뉴 창에서 `python` 검색 후 install.

  ![python07](images/python07.png)

  * `Ctrl + Shift + P` - `interpreter` - 세 번째에 있는 가상환경 `venv` 선택

  ![python08](images/python08.jpg)

  ![python09](images/python09.jpg)
  * 확인: terminal창 `clear`(휴지통 아이콘 가능) - terminal창 다시 켜기 - 저절로 venv로 들어가야 함.

  ![python10](images/python10.jpg)

### 3-3. 가상환경 탈출

* 어느 위치나 관계 없이 다음의 명령어 입력.

```bash
$ deactivate
```

* 가상환경 빠져 나갔다가, 다시 들어오면 무조건 setting에 venv 잡힘.

### 3-4. gitignore 설정

> 가상환경에 이것 저것 모두 설치하면 용량 커진다.
>
> gitignore을 통해 git에 push할 때 무시하도록 할 파일 설치할 것.

* gitignore.io 접속
* 가상환경에서 진행할 프로젝트에 사용할 파일 모두 넣고 생성.
  * `flask, visualstudiocode, venv`

![python11](images/python11.jpg)

![python12](images/python12.jpg)

* `vim` 모드에서 `.gitignore` 파일 생성

```bash
$ vi .gitignore
```

```bash
(vim 화면)
i 선택 - 입력모드
gitignore 파일 모두 다 복사해서 붙여 넣기
esc
:wq
```

![python13](images/python13.jpg)

### 3-5. 설정 완료

* 폴더 2개, `.gitignore` 파일 있으면 설정 끝.

![python14](images/python14.jpg)



---



## 4. 기타

* 설치된 목록 확인

```bash
$ pip list
	# 구버전이라서 노란 글씨로 warning message 뜸.

$ python -m pip install --upgrade pip
	# 버전 업그레이드하고,
	# warning message 안 뜨게 된다.

```

![python15](images/python15.jpg)



# 원격저장소에 올려둔 가상환경 불러오기

> 기본적으로 원격 저장소에는가상환경 폴더(venv)를 통재로 올리지 않는다.
>
> 그 이유는 가상환경 폴더에 각종 라이브러리가 설치되기 때문에, 파일의 개수가 많고 용량이 크기 때문이다.
>
> 또한, 개개인의 PC 환경이 다르기 때문에, 본인의 PC에서 잘 돌아가던 가상환경 세팅이라도, 다른 사람의 PC에 통째로 건네주면 그 사람의 환경과 충돌할 위험이 있다.
>
> 따라서 프로젝트 환경에 필요한 프로젝트 목록만 넘겨주고, 그 프로젝트를 받아서 **실행 혹은 개발**하고 싶은 사람이, 해당하는 패키지를 설치해서 사용할 수 있게 한다. 



---

* 상황 예시
  * `requirements.txt`가 만들어져 있고, 이 안에 가상환경에 필요한 패키지 목록이 나열되어 있다.
  * 내가 작업하고자 하는 환경에는, 가상환경이 **세팅되어 있지 않다.**

---



## 1. 원격저장소 내용 가져오기

### 1-1. 원격저장소와 내 local 환경 동기화

* clone을 받아 두었을 경우

```bash
$ git pull origin master
```

* 아무 것도 없을 경우

```bash
$ git clone GithubURL
```

* 동기화된 것을 확인할 수 있다.



### 1-2. Git Bash

* 가상환경을 설치할 폴더로 들어가서 `git bash`를 연다.

```bash
~/이레/바탕화면/TIL/chatbot
$
```

```bash
[집에 가서 아무 것도 안 했을 상황이라면]
TIL/
	chatbot/
		python-recap/
		.gitignore
		requirements.txt
```



### 1-3. 파이썬 가상환경 설치

* 명령어

```bash
$ python -m venv venv(가상환경 이름)
```

* 가상환경 폴더 생성 확인

```bash
TIL/
	chatbot/
		venv/							# 이게 생성되었는지 확인
		python-recap/
		.gitignore
		requirements.txt
```



### 1-4. 가상환경 진입 후 패키지 설치

* 가상환경 진입해서 패키지 목록 확인

```bash
~이레/바탕화면/TIL/chatbot
$ source venv/Scripts/activate			# 가상환경 진입

(venv)									# venv 진입한 상태
$ pip list								# 패키지 목록 확인 명령
...										# 비어 있는 상태
...
```

* 프로젝트에 필요한 패키지 설치
  * 필요한 패키지 목록은 `requirements.txt`에 저장되어 있다.
  * 명령어를 통해 자동으로 읽으면서 설치하도록 한다.

```bash
~/이레/바탕화면/TIL/chatbot
$ pip install -r requirements.txt		# 자동으로 읽어서 설치하도록 함.
```

* 패키지 목록 확인

```bash
$ pip list
```

* `requirements.txt`에 필요한 패키지들이 설치된 것을 확인할 수 있다.



### 1-5. VSCode에서 자동으로 가상환경 진입하도록 설정

* 확장코드 설치: 좌측 하단 마지막 메뉴 창에서 `python` 검색 후 install.

![python07](images/python07.png)

* `Ctrl + Shift + P` - `interpreter` - 세 번째에 있는 가상환경 `venv` 선택



## 2. 실습

> 집이라고 생각하고, 폴더 하나 만들어서 실습하기

![practice01](images/practice01.jpg)

![practice02](images/practice02.jpg)

![practice03](images/practice03.jpg)

![practice04](images/practice04.jpg)

![practice05](images/practice05.jpg)





