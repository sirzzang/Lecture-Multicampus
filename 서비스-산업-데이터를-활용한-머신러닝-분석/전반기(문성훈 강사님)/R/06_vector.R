# Data Type : 저장된 데이터의 성격(numeric, character, logical)
# Data Structure : 변수에 저장된 데이터의 메모리 구조.

# R이 제공하는 자료구조
# 6개 기억하시면 되요!!
# 2개의 분류로 나누어져요!
# 같은 데이터 타입인가 아닌가
# vector : 1차원, 같은 data type
# matrix : 2차원, 같은 data type
# Array : 3차원, 같은 data type

# List : 1차원, 다른 data type
# 중첩 자료구조
# Data Frame : 2차원, 다른 data type 
# Factor : 범주형 자료구조

###########################################

# 1. vector
# vector는 scalar의 확장, 1차원 선형구조
# vector는 같은 data type으로 구성되요!
# vector는 첨자형태로 access가 가능( [] )
# 첨자(index)의 시작은 1

# vector를 생성하는 방법
# 1. combine 함수를 사용해서 생성! ( c() )
#    일반적으로 규칙성이 없는 데이터를 이용해서
#    vector를 생성할 때 이용
#    vector를 이용해서 다른 vector를 만들 수 있어요!
var1 = c(1,2,6,9,10)
var1
mode(var1)
var2 = c(TRUE,FALSE,TRUE)   # 
var2
var3 = c("홍길동","김길동","최길동")
var3
var4 = c(200,TRUE,"아우성!!")
var4
var5 = c(var1,var2)   # 1 2 6 9 10 1 0 1 
                      # vector의 결합 
var5
# 2. :  을 이용해서 vector를 생성할 수 있어요!
#       numeric에서만 사용가능하고 1씩 증가하거나
#       감소하는 숫자의 집합을 vector로 만들 때 사용
#       start:end 형태로 사용되고 둘 다 inclusive
var1 = 1:5; var1
var2 = 5:1; var2
var3 = 3.4:10; var3

# 3. seq()를 이용해서 vector를 생성할 수 있어요!
#    : 의 일반형으로 등차수열을 생성해서 vector화
#    시킬 때 사용
var1 = seq(from=1,to=10,by=3)# readability가 좋아요
var1 = seq(1,10,3)
var1

# 4. rep()를 이용해서 vector를 생성할 수 있어요!
#    replicate의 약자
#    지정된 숫자만큼 반복해서 vector를 생성
var1 = rep(1:3, 3)   # times는 생략이 가능
var1                 # 1 2 3 1 2 3 1 2 3 
var2 = rep(1:3, each=3)
var2                 # 1 1 1 2 2 2 3 3 3 

# vector의 데이터 타입을 확인해 보아요!
mode(var1)     # numeric

# vector안의 데이터의 개수를 알아내려면??
# length() 함수를 이용.
var1 = c(1:10)
var1
length(var1)         # 10
# length를 다른 의미로 사용할 수 있어요!

var1 = seq(1,100, length=7); var1

# vector에서 데이터 추출
# vector의 사용은 []를 이용해서 데이터 추출
var1 = c(67,90,87,50,100)
var1

var1[1] # vector의 제일 처음 원소를 추출
var1[length(var1)]  # vector의 제일 마지막 원소를 추출
var1[2:4]  # vector를 만들기 위해서 사용한 :, c(), seq(), rep()를 vector 요소를 access하기 위한 용도로 사용할 수 있어요!
var1[c(1,5)]
var1[seq(1,4)]
var1[6]     # NA
var1[-1]    # "-"는 제외의 의미 
var1[-c(1:3)] # 50 100 

# vector 데이터의 이름
var1 = c(67,90,50)
var1
names(var1)   # vector의 각 데이터에 붙은 이름은 없어요!!

names(var1) = c("국어","영어","수학")  # name 설정

var1

var1[2]   # index를 이용해서 vector 데이터를 추출
var1["영어"]  # name을 통해서 vector 데이터를 추출

# vector의 연산
# 수치형 vector는 scalar를 이용하여 사칙연산을 할 수 있어요! 그리고 vector와 vector간의 연산도 수행할 수 있어요!
var1 <- 1:3   # 1 2 3 
var2 <- 4:6   # 4 5 6 
var1; var2

var1 * 2      # 2 4 6     
var1 + 10     # 11 12 13

var1 + var2   # 5 7 9 

var3 = 5:10   # 5 6 7 8 9 10

var1 + var3   # 1 2 3 1 2 3    # recycling rule   
              # 5 6 7 8 9 10
              # 6 8 10 9 11 13

var4 = 5:9    # 5 6 7 8 9

var1 + var4   # 1 2 3 1 2
              # 5 6 7 8 9
              # 6 8 10 9 11  # 동작은 가능. warning

# vector간의 집합 연산
# union() : 합집합
# intersect() : 교집합
# setdiff() : 차집합

var1 = c(1:5)
var2 = c(3:7)
union(var1,var2)
intersect(var1,var2)
setdiff(var1,var2)

# vector간의 비교( 두 vector가 같은가 다른가 확인)
# identical : 비교하는 두 vector의 요소가 개수, 순서, 내용이 같아야지 TRUE를 return
# setequal : 비교하는 두 vector의 크기, 순서와 상관없이 내용만을 비교

var1 = 1:3; var1
var2 = 1:3
var3 = c(1,3,2,1,1,1,3,3,4)

var2 = c(1,2,3); var2

class(var1)

identical(var1, var2) # 같은 vector이기 때문에 TRUE
identical(var1, var3) # 같은 vector가 아니예요!!
setequal(var1,var2)   # vector의 내용이 같아요!!


# 요소가 없는 vector
var1 = vector(mode="character", length=10)
var1

