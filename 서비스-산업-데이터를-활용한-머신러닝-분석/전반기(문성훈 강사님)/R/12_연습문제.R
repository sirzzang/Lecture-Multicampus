# 연습문제
# 사용할 데이터 : 2 3 5 6 7 10

# 1. 주어진 데이터로 vector x를 생성하세요
x <- c(2,3,5,6,7,10); x

# 2. 주어진 데이터 각각을 제곱해서 vector x를
# 생성하세요
x = c(2,3,5,6,7,10)^2; x

# 3. 주어진 데이터 각각을 제곱해서 합을 구하세요
sum(c(2,3,5,6,7,10)^2)

# 사용할 데이터 : 2 3 5 6 7 10
# 4. 주어진 데이터에서 5보다 큰 값들로 구성된 vector x를 구하세요
x = c(2,3,5,6,7,10)
var1 = c(2,3,5,6,7,10) > 5 # mask
x[var1]                    # fancy indexing

x = c(2,3,5,6,7,10)
# 5. vector x의 길이를 구하세요!
length(x)

# 6. R의 package중에 UsingR 이 있어요!
install.packages("UsingR")
# 설치된 package를 불러들여요!
library(UsingR)
# 데이터를 불러들일 수 있어요!
# 1부터 2003까지 숫자 중 prime number를 
# 가지고 있어요!
data("primes")
head(primes)  # 앞에서 6개만 출력
tail(primes)  # 뒤에서 6개만 출력

# 7. 1부터 2003까지 숫자 중 prime number는 몇개인가요?
length(primes)   # 총 304개

# 8. 1부터 200까지 숫자 중 prime number는
#몇개인가요?
sum(primes <= 200)

# 9. 평균을 구해보아요!
mean(primes)

# 10.500이상 1000 이하의 prime number만으로
# 구성된 vector p를 구하세요!~
# fancy indexing을 이용해 보아요!!
p = primes[primes >= 500 & primes <= 1000]
p

# 다음과 같은 형태의 데이터를 이용하여
# 아래의 문제를 풀어보아요!
# 1 5 9
# 2 6 10
# 3 7 11
# 4 8 12

# 11. 위의 데이터를 이용해서 matrix x를
# 생성하세요
x = matrix(seq(1,12),
           nrow=4,
           byrow = F)
x

# 12. 전치행렬을 만들어 보아요!
t(x)

# 13. matrix x에 대해 첫번째 행만 추출하세요
x[1,]

# 14. matrix x에 대해 6,7,10,11을 matrix형태로 추출하세요
x[2:3,-1]

# 15. matrix x에 대해 x의 두번째 열의 원소가
# 홀수인 행들만 뽑아서 matrix p를 생성하세요
p = x[x[,2] %% 2 == 1, ]
p

## 프로그래밍
## 홀수개의 숫자로 구성된 숫자문자열이
## 입력으로 제공됩니다. 문자열의 개수는
## 7개 이상 11개 이하로 제한됩니다.
## 입력 문자열의 길이는 7개, 9개 , 11개

## 중앙 숫자를 기준으로 앞과 뒤의 숫자를
## 분리한 후 분리된 두 수를 거꾸로
## 뒤집어서 두수의 차를 구해요!

## 예) 7648623
##     764 623   가운데를 기준으로 나눠요
##     467 326   각 숫자를 거꾸로 뒤집어요
##     141       (467-326) 두 수의 차

## 예) 7648620
##     764 620   가운데를 기준으로 나눠요
##     467 026   각 숫자를 거꾸로 뒤집어요
##               (467-26) 두 수의 차


library(stringr)
input = "7648623"
mid_input=(str_length(input) %/% 2) + 1
var1 = str_sub(input,
               1,
               mid_input-1)
var2 = str_sub(input,
               mid_input+1,
               str_length(input))
abs(
as.integer(paste(rev(str_split(var1,pattern = "")[[1]]),collapse = ""))
-
as.integer(paste(rev(str_split(var2,pattern = "")[[1]]),collapse = ""))
)
########################################

# 기본적인 R 사용
# data type (자료형)
# data structure (자료구조)
# control statement (제어문)

# Web
# 데이터를 구축
# Database로 부터 데이터를 얻어올 수 있어요
# Open API를 이용해서 데이터를 얻어올 수 있어요
# 파일로부터 데이터를 얻어올 수 있어요
# 프로그램적으로 web scraping, crawling을
# 통해 데이터를 구축

# HTML, CSS, JavaScript 
# HTML : 웹페이지의 내용, 구조를 담당
# CSS  : 웹페이지의 styling을 담당
# JavaScript : 웹페이지의 동적처리를 담당

# 기본적으로 Web은 CS구조로 되어 있어요
# CS구조 : client-server구조
# server쪽 프로그램 : web server
#           HTML,CSS,JAvaScript를 제공
# client쪽 프로그램 : chrome(browser)
# 서버로부터 HTML,CSS,JavaScript를 받아서
# 화면에 rendering을 해요!

# HTML, CSS, JavaScript를 이용해서
# 클라이언트에게 제공해주는 Web page를
# 만들어 보아요!
# 개발툴이 있어야 해요!
# WebStorm을 이용해서 개발해 보아요!
# 실행해보아요!

# 클라이언트에게 제공할 HTML을 작성했어요!
# 서버프로그램(web server)에게 우리 프로젝트를 알려줘야 해요!
# 우리 프로젝트를 web server에게 인지시켜야 해요!! (configure)
# web server 프로그램을 기동시켜서 우리 프로젝트를 웹에 deploy
# web client(browser)를 이용해서 URL(주소, 좌표) 서버쪽 프로그램에 접속해서 HTML을 받아가서 화면에 그려요(표시해요)

# Web server가 webstrom에 내장되어 있어요!





# 10/25 금

#   - kyeworkd로 도서 검색후 출력(실습)
# Web crawling & web scraping



### HTML, CSS, JavaScript 웹 언어

# w3c
# HTML이 발전발전 해서 1999년 4.01 버전
# W3C가 1999년 12월에 HTML 4.01을 마지막으로
# 더이상 HTML의 버전업은 없다고 발표함
# HTML 언어는 기본적으로 2가지 문제점을 가지고 있기 때문임

# HTML의문제점
# 1. 정형성이 없음 : error가 있어도 알아서처리 하여 수행 해 줌 
#                   주기적 유지보수 및 업데이트 시 구조적 문제가 대두됨
# 2. 확장성이 없다  -> 태그의 기능이 고정됨 
#                   (배우기는 쉬우나, 정해진 기능을 벗어날 수 없는 한계) 
# 2000년 부터 W3C는 HTML 표준을 다른 것으로 가미해 
# 위 2가지 문제를 해결하기 위해 
# XML을 HTML에 도입해서 표준으로 끌고가려 함
#    1. 정형성이 있고, 2. 확장성이 있음
# XHTML 1.0 이 시작 => but실패 (배우고 사용하기 어려움)
# XML 사용에 회의적인 시각을가진 몇몇 회사들이 컨소시엄을 구성하여 
# XML대신 HTML을 발전시키기로 했고
# HTML 5를 개발함

# HTML5 의의: 
# 웹페이지 대신 웹어플리케이션이 대세가 될거라는 시각으로 개발 
# 웹 창이 응용프로그램 처럼 열림
#	웹페이지 대신 Front-End Web Application을 사용하게 될 것이라 예상
# Angular, react.js,View.js (Front-End쪽 Frame work) 
# => JavaScript 언어를 이용해 웹 페이지가 아닌 웹 어플리케이션을 만들고 있는 추세

# * 본 과정에서는 HTML5를 사용하나, 웹어플리케이션이 아닌 웹 페이지를 base로 학습할 것
# 










############  10/25 연습문제 #############################

# 입력으로 최대 100자의 문자열을 이용

# 입력으로 사용된 문자열에서 숫자만을 추출하여

# 출력하라

# 예) Hi2567Hello23kaka890L34TT23
#     => "2567238903423"
# 이렇게 추출한 숫자문자열에서
# 개수가 가장 많은 숫자를 찾아서 숫자와
# 출현빈도를 출력하라
# 2 -> 3, 3 > 3, 4-> 1, 5 -> 1, 6 -> 1, 7 -> 

# 만약 출현빈도가 같은 숫자가 여러개인 경우
# 그 중 가장 작은 숫자와 출현빈도를 출력하시오


# 조건에 맞는 내용을 추출하기
# 추출해서
# 붙이기

library(stringr)

var1 <- "Hi2567Hello23kaka890L34TT23"

myNum<-str_c(str_extract_all(var1,"[0-9]{1,}")[[1]],collapse="")
myNum


ymax = 0
maxnum = 0

for (i in seq(1:9)){
    c = as.character(i)
    x <-length(str_extract_all(myNum, c)[[1]])
    if (ymax < x ) {
      ymax <- x
      maxnum <- i
    }
}
                          
cat(maxnum, "->",ymax)



#####################################################################

var1 <- "Hi2567Hello23kaka890L34TT23"
myNum<-paste(str_extract_all(var1,"[0-9]{1,}")[[1]], collapse="")
class(myNum)

L<-str_length(myNum)

maxfrq =0
maxnum =0



for(i in seq(1:L)){
    freq <- length(str_extract_all(myNum,str_sub(myNum,i,i))[[1]])
    if (maxfrq < freq) {
        maxfrq <-freq
        maxnum <- str_sub(myNum,i,i)  
    }
}
    cat(maxnum,"->",maxfrq )

    
#####################################################################
# logical로 만들어보기 

var1 <- "Hi2567Hello23kaka890L34TT23"
    
myNum<-str_replace_all(var1,"[a-z,A-Z]{1,}","")
class(myNum)
mode(myNum)    

myVec<-str_split(myNum,"")[[1]]


for (i in 1:9){

  for (k in 1:L){
    var1< - myVec[k]==i
    
  }  
}
    
       





############################
# 10/28 (월) ~10/29(화)

# jQuery selector , method, event를 이용한 화면 제어

# 응용(도서검색 web application)
# Server program 설정 --> 제외
# - 도서검색 프로그램(제공)
# AJAX 호출 후 browser 동적 처리
# keyword로 도서 검색 후 출력(실습)


cat("\014")
rm(list=ls())


















