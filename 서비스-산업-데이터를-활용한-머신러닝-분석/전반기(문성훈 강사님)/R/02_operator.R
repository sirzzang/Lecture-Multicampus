# Operator ( 연산자 )

var1 <- 100
var2 <- 3

var1 / var2 # Java언어 => 33
            # R은 마치 실세계의 연산처럼 수행( 33.3333 )

# 몫을 구해보아요 => 33
var1 %/% var2 # 33
# 나머지를 구해보아요 => 1
var1 %% var2 # 1

# 비교연산자
var1 == var2  # FALSE (F)
var1 != var2  # TRUE (T)

# 논리연산자 
# &, && : 양쪽 값이 TRUE이면 TRUE
TRUE & FALSE
TRUE && FALSE  
# 둘 다 논리 연산자 AND 연산
# | , || : 하나라도 TRUE이면 결과 TRUE
TRUE | FALSE   # TRUE
FALSE || FALSE # FALSE

# 단일변수는 1개짜리 공간
# R은 여러가지 자료구조가 있어요
# 가장 대표적인 자료구조(데이터를 저장하는 구조)에는 vector가 있어요
# R에서 vector는 연속적인 저장공간
# 다른언어의 array와 같은 구조
# vector는 1차원 자료구조
# 저장공간안에 모두 같은 데이터 타입이 들어와요!
# 함수를 이용해서 vector를 생성
# c() => combine의 약자
c(10,20,30)   # 10 20 30
c(TRUE,20,3.14) # 같은 데이터타입으로 vector생성 (오류가 아니예요)

c(TRUE,FALSE) & c(TRUE,TRUE) # vector 연산 결과값 vector
c(TRUE,FALSE) && c(TRUE,TRUE) # 첫번째 요소만 & 연산 수행

c(TRUE,F,TRUE) & c(FALSE,T)
# FALSE FALSE FALSE

!c(T,F,T,F)

# 다른언어와 마찬가지로 다양한
# 수학함수를 내장하고 있어요!
# 필요할 때 찾아서 사용해보아요!!
abs(-3)
round(3.1415)
sqrt(100)







