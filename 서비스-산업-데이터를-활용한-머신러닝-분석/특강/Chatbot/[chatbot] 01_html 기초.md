# HTML

## 1. HTML 문서 생성

* 명령어 : `!` + `tab` 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```



---

## 2. HTML index 

> body 부분에 내용을 작성한다.

### 2-0. 기본 스타일 주기

* 굵게 : `b`
* 기울임체 : `i`
* 강조 : `mark`
* 취소선 : `del`
* 줄바꿈 : `br`

```html
<!-- 굵게(bold) -->
<b> This is bold. </b><br>

<!-- 기울임(italic) -->
<i> This is italic</i>

<!-- 강조(highlighted) -->
<p> 강조하고 싶으면 <mark> mark 태그로 감싸면 </mark>됩니다!</p>

<!-- 취소선 : del -->
<p> 취소선을 주고 싶으면 <del> del태그로 감싸면 </del> 됩니다. </p>
```

![html02](images/html02.jpg)



### 2-1. 제목(Heading)

* `h1` ~ `h6` : 제목 수준별로 level 나눌 수 있음.

```html
<!-- 제목: Heading -->
<!-- 레벨 지정 가능-->
<h1> Hi, h1!   </h1>    
<h2> Hi, h1!   </h2>    
<h3> Hi, h1!   </h3>    
<h4> Hi, h1!   </h4>    
<h5> Hi, h1!   </h5>    
<h6> Hi, h1!   </h6>  
```

![html01](images/html01.jpg)



### 2-2. 문단(paragraph)

* `p` :  문단 설정
* 문단 내 줄바꿈 가능.
* `span` : 문단 내 `span` 태그로 감싸서 스타일 설정 가능.

```html
<!-- 문단 표시(p:paragraph)-->

<!-- 1. 문단 설정하기 -->
  
    <p> 안녕하세요. p 태그입니다.</p>

<!-- 2. 줄바꿈하기 -->

    <p> 안녕하세요. p태그 입니다<br>
        줄바꿈을 하고 싶으면 <br>
        br 태그를 써주세요
    </p>

<!-- 3. 스타일 주기 -->
    <p>
        <span style="color:chocolate">
            스타일을 주고 싶으면 span태그로 감싸서
        </span> 쓰면 됩니다. <br>
        줄바꾸고 싶으면, br을 넣구요. <br>
        줄바꿈 되었나요?
    </p>     
```

