# R은 프로그래밍 언어예요.. 따라서 제어문도
# 가지고 있어요!

# if구문 (조건문)
var1 = 100
var2 = 20
# 조건에 따라서 실행되는 code block을 제어할
# 수 있어요!!

if(var1 > var2) {
  # 조건문이 참일 때 실행
  cat("참이예요!!")
} else {
  # 조건문이 거짓일 때 실행
  cat("거짓이예요!!")
}

# ifelse : 3항 연산자
var1 = 10
var2 = 20

ifelse(var1 > var2,"참일경우 선택","F일 경우 선택")

# 반복문( for, while )
# for : 반복 횟수만큼 반복 실행
# while : 조건이 TRUE일 동안 반복 실행

for( var1 in seq(1:5)) {
  print(var1)  
}

idx = 1
mySum = 0

while(idx < 10) {
  mySum = mySum + idx 
  idx = idx + 1
}
mySum
sum(c(1:9))

# 로직(제어문을 이용해서) 1부터 100사이에 있는
# 3의 배수를 출력하세요!
for( var1 in seq(1,100)) {
  if( var1 %% 3 == 0 ) {
    print(var1)
  }
}

# 1부터 100사이에 있는 prime number를 출력하세요
for(var1 in 2:100) {
  divCount = 0
  var2 = c(2:var1)
  for(var3 in var2) {
    if(var1 %% var3 == 0) {
      divCount = divCount + 1
    }
  }
  if(divCount == 1) {
    print(var1)
  }
}

# 사용자 정의 함수( User Define Function )
# 제공된 함수말고 우리가 함수를 만들 수 있을까?
# 함수명 <- function(x) { ... }
# 입력받은 숫자를 제곱해서 돌려주는
# 함수를 하나 만들어 보세요!
myFunc = function(x) {
  x = x * x
  return(x)
}
var1 = myFunc(5)
var1

var1 = c(1:10)
sum(var1)   

# sum함수와 동일한 역할을 하는 mySum을
# 만들어 보아요!
# vector를 입력으로 받아서 합을 구해주는 
# 함수
mySum = function(x) {
  result = 0
  for(t in x) {
    result = result + t
  }
  return(result)
}
var1 = c(1:10)
mySum(var1)

#########################################

# 연습문제를 풀어보아요!
# 로직문제를 풀어보아요!
# Web





















