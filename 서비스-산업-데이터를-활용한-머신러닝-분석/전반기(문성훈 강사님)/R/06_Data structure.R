# Data Type : 저장된 데이터의 성격(character, numeric, logical)
# Data Structure : 변수에 저장된 데이터의 메모리 구조.

# R이 제공하는 자료구조
# 6개 기억하면 된다.
# 2개의 분류로 나뉜다.
# 같은 데이터 타입인가 아닌가.
# vector : 1차원, 같은 data type 
# matrix : 2차원, 같은 data type
# Array : 3차원, 같은 data type
##############################################
# List : 1차원, 다른 data type 
# 중첩 자료구조 (List 안에 모든 자료구조가 들어갈 수 있다.)
# Data Frame : 2차원, 다른 data type 
# 데이터 테이블과 같은 형식
# Factor : 범주형 자료구조
################################################

# 1. vector
# vector는 scalar의 확장, 1차원 선형구조 
# vector는 같은 data type으로 구성되요!
# vector는 첨자형태로 access가 가능( [] )
# R은 첨자(index)의 시작이 1 !!(0이 아니다)

# vector를 생성하는 방법
# 1. combine 함수를 사용해서 생성 ( c() )
# 일반적으로 규칙성이 없는 데이터를 이용할 때 사용
# vector를 이용해서 다른 vector를 만들 수 있다.
var1 = c(1,13,2,35,4)
var1
mode(var1)
var2 = c(TRUE, FALSE, TRUE)
var2
mode(var2)
var3 = c("홍길동", "김길동", "최길동")
var3
var4 = c(200, TRUE, "아우우아")
mode(var4)
var5 = c(var1, var2)
var5  # 같은 데이터 타입으로 연결된 새로운 벡터로 만들어진다(vector의 결함)

# 2. : 을 이용해서 vector를 생성할 수 있다.
# numeric에서만 사용가능하고 1씩 증가하거나 감소하는 숫자의 숫자의 집합을 vector로 만들 때 사용
var1 = 1:5
var1
var2 = 5:1; var2
var3 = 3.3:10; var3
# start : end 형태로 사용되고 둘다 inclusive

# 3. seq()를 이용해서 vector를 생성할 수 있다.
# : 의 일반형으로 등차수열을 생성해 vector화 시킬 때 사용

var1 = seq(from=1, to=10, by=3); var1
var1 = seq(1, 10, 3); var1 # 속성을 제거하고 사용 똑같다.

# 4. rep()를 이용해서 vector를 생성할 수 있다.
# replicate의 약자
# 지정된 숫자만큼 반복해서 vector를 생성
var1 = rep(1:3, times=3); var1
var1 = rep(1:3, times=3); var1 # 1 2 3 1 2 3 1 2 3
var2 = rep(1:4, each=4); var2 # 각각 반복  1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4

# vector의 데이터 타입 확인해보기
mode(var1) # numeric

# vector안의 데이터 개수를 알아내려면 
# length() 함수를 이용
var1 = c(1:10)
var1
length(var1) # vector의 길이를 갯수를 알 수 있다.
# length를 다른 의미로 사용할 수 있다.

var1 = seq(1, 100, 3); var1
var1 = seq(1, 100, length=3); var1 # length의 숫자만큼 나눠서 표현해준다.
                                   # 1.0  50.5 100.0

# vector에서 데이터 추출
# vector의 사용은 []를 이용해서 데이터 추출
var1 = c(67, 90, 87, 50, 100); var1
var1[1] # 67 vector의 첫 원소 추출
var1[length(var1)] # 100 vector의 마지막(크기) 원소를 추출출
var1[2:4] # 90 87 50  vector를 만들기 위해서 사용한 :, c(), seq(), rep()를                        # vector요소를 access하기 위한 용도로 사용할 수 있다.
var1[c(1,5)] # 67 100
var1[seq(1,4)] # 67 90 87 50
var1[6] # NA
var1[-1] # 90  87  50 100 1번째 항을 제외한 나머지  (역의 의미)
var1[-c(1:3)] # 50 100 1, 2, 3번 째 항을 제외한 나머지(역의 의미)
 
# vector 데이터의 이름
var1 = c(67, 90, 50)

names(var1) # NULL vector의 각 데이터에 붙은 이름은 없다.

names(var1) = c("국어","영어","수학") # name 설정 (레이블과 같이 행이아님)
var1 # 국어 영어 수학 
     # 67   90   50 
var1[2] # index를 이용해서 vector 데이터를 추출

var1["영어"] # 해당 name을 통해서 access

# vector의 연산
# 수치형 vector는 scalar를 이용하여 사칙연산을 할 수 있다.
# vector와 vector간의 연산도 수행 가능.
var1 = 1:3; var1
var2 = 4:6; var2
var1 * 2 # 2 4 6
var1 + 10 # 11 12 13

var1 + var2 # 5 7 9

var3 = 5:10; var3
var1 + var3 # 1 2 3 1 2 3  # recycling rule
            # 5 6 7 8 9 10 
            # 6  8 10  9 11 13

var4 = 5:9; var4
var1 + var4 # 6 8 10 9 11 warning message뜸

# vector간의 집합 연산
# union() : 합집합
# intersect() : 교집합
# setdiff() : 차집합

var1 = c(1:5);var1
var2 = c(3:7); var2
union(var1,var2)
intersect(var1,var2)
setdiff(var1,var2)

# vector간의 비교 (두 vector가 같은가 다른가 확인)
# identical : 비교하는 두 vector의 요소가 길이, 갯수, 순서, 내용이 같아야지                 True를 return
# setequal : 비교하는 두 vector의 크기, 순서와 상관없이 내용만을 비교

identical(var1,var2)
var1 = 1:3; var1
var2 = 1:3; var2
identical(var1, var2) # TRUE
var3 = c(1, 3, 2)
identical(var1, var3) # FALSE

setequal(var1, var3) # TRUE 가지고 있는 데이터에 차이가 있는지

# 요소가 없는 vector
var1 = vector(mode="numeric", length=10)
var1 # 0 0 0 0 0 0 0 0 0 0
var2 = vector(mode="logical", length=8)
var2 # FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
 
