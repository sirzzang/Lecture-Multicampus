# R은 통계계산을 위한 프로그래밍 언어이자 소프트웨어
# # 통계학과 교수인 로스 이하카와 로버트 젠틀맨 두사람이 일반사람들도 쉡게 통계를 할 수 있도록 Bell 연구소에서 사용하던 s라는 통께프로그램을 모태로 1993년에 만듬.
# R의 장점 : 무료 > 많음 사람들이 사용 > 오픈소스 생태계 잘 유지됨
# R & Python 
# R 다운로드, Rstudio
# R 프로그램의 기본 
# 주석 : #
# statement의 종료 : ;(생략가능)
# Crtl + Enter 사용
# R 은 대소문자 구분 : Case-sensitive
# 변수이름을 지을 때 : Camelcase notataion
myVar = 100
myVar <- 110
120 -> myVar
myVar
print(myVar)
cat(myVar, myVar)
cat("변수의 값은 : ", myVar)
var1 = seq(1, 100, 3)
var1
#######################################################################

# 연산자에 대해 알아보기
# Operator
var1 = 100
var2 = 3
options(digits = 12)  # 기본값은 7
var1/var2
sprintf("%.7f", var1/var2) # 형태를 잡아서 출력하는 함수
# 결과는 문자열로 떨어진다


var1 %/% var2
var1 %% var2

var1 == var2 # 비교연산자 FALSE(F)
var1 != var2 # TRUE(T)

# &, | (AND, OR)연산산
# &&, || (vector에 대한 연산 수행시 첫번째 요소만을 비교)

#######################################################################

# Data Type 
# 기본 타입 4개
# Numeric, Character, Logical, Complex
# NULL, NA(결측치), NaN, Inf

# R이 제공하는 기본함수중에 mode()
var1 = "이것은 소리없는 아우성"
mode(var1)
# is 계열의 함수(확인하기) -> is.character, is.numeric.....

# R의 데이터타입은 우선순위가 존재한다
# 1. character > complex > numeric > logical

# R은 하나의 데이터타입을 다른데이터타입으로 바꿀 수 있다.
# as 계열의 함수(바꾸기) -> 
var1 = "3.141592"
as.numeric(var1)

var2 = TRUE
as.double(var2)
as.numeric(var2)
var3 = 100
as.logical(var3)
