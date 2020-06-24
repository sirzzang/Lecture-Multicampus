# 같은 데이터 타입을 저장하는 자료구조
# vector(1차원), matrix(2차원), Array(3차원 이상)

# 다른 데이터 타입을 저장하는 자료구조
# List(1차원), data frame(2차원)

# 범주형 자료구조 => factor
##################################################

# factor 
# 범주형 데이터를 저장하기 위한 자료구조
# 범주형 데이터는 
# 예를 들어 방의 크기가 "대", "중", "소" => level
# 일반적으로 vector를 이용해서 factor를 만들어요 

# 6명의 혈액형 데이터를 vector에 저장하고 factor로
# 변형해 보아요!


var1 = c("A","AB","O","A","B","B")
var1

factor_var1 = factor(var1)
factor_var1  

nlevels(factor_var1)   # 4 , level의 개수
levels(factor_var1)    # 사용되는 level 출력
is.factor(factor_var1) # TRUE  

###########################################
# 남성과 여성의 성별데이터로 factor를 생성하고
# 빈도수를 구해보아요!

var1 = c("MAN","WOMAN","MAN","MAN","MAN","WOMAN")
var1

factor_gender = factor(var1)
factor_gender  

table(factor_gender)  
  
plot(factor_gender)  

##########################################

# List 
# 1차원 선형구조, 다른 데이터 타입이
# 들어올 수 있어요. 
# 중첩 자료구조로 이용

# 지금까지 했던 여러 자료구조들을 생성해서
# List안에 저장해 보아요!

var_scalar = 100; var_scalar   # scalar

var_vector = c(10,20,30)       # vector
var_vector 

var_matrix = matrix(c(1:12), 
                    ncol=3, 
                    nrow=4,
                    byrow=T)
var_matrix

var_array = array(c(1:12), dim=c(2,2,3))
var_array

var_df = data.frame(id=1:4,
                    name=c("홍길동","김길동","최길동","이길동"),
                    age=c(30,40,20,10))
var_df

myList = list(var_scalar,
              var_vector,
              var_matrix,
              var_array,
              var_df)

myList
myList[1]
myList[[1]]
# key와 value로 저장되는 자료구조이고
# 데이터를 출력할 때 key값도 같이 출력


myList = list(name=c("홍길동","김길동"),
              age=c(20,30),
              address=c("서울","부산"))

myList
myList[1]
myList$name    # List에서 key를 사용할 때는 $기호를 이용해요!!

myList$name[2]

myList[[1]]   # 이 형태도 가능해요!
myList[["name"]]
myList$name   # 이 형태를 일반적으로 사용

#######################################

# data frame
# matrix와 같은 2차원 형태의 자료구조
# 다른 데이터 타입을 사용할 수 있어요!
# column명을 이용할 수 있어요
# Database의 Table과 유사해요!

# 간단한 예를 이용해 보아요!

# vector를 이용해서 data frame을 만들어 보아요!

no=c(1,2,3)
name=c("홍길동","김길동","최길동")
age=c(10,20,30)

df = data.frame(s_no=no,
                s_name=name,
                s_age=age)
df$s_name

# data frame의 함수
str(df)    # data frame의 구조를 볼 수 있어요

summary(df)  # data frame의 요약통계를 볼 수 있어요!

apply()  # data frame에도 적용할 수 있어요!

df = data.frame(x=c(1:5),
                y=seq(2,10,2),
                z=c("a","b","c","d","e"),
                stringsAsFactors = F)
df
str(df)
# 연습문제
# 주어진 data frame의 1,2번째 column에 
# 대해서 각각 합계를 구하세요!
# apply()함수를 이용해 보아요!
apply(X=df[,c(1:2)],MARGIN=2,FUN=sum)

# subset()
# data frame에서 조건에 맞는 행을 추출해서
# 독립적인 data frame을 생성

df = data.frame(x=c(1:5),
                y=seq(2,10,2),
                z=c("a","b","c","d","e"))
df
help(data.frame)
subset(df,x > 3)

# x가 3보다 작고  y가 4이상인 데이터를 
# 추출하세요
df_sub <- subset(df,x < 3 & y >= 4)

#######################################

# 6개의 자료구조에 대해서 알아보았어요!
# 배운내용을 복습하기 위해서 간단한
# 연습문제를 풀어보아요!

# 1. 4,6,5,7,10,9,4 데이터를 이용해서
# 숫자형 vector x를 생성하세요!
x <- c(4,6,5,7,10,9,4); x

# 2. 아래의 두 벡터의 연산 결과는?
x1 = c(3,5,6,8)
x2 = c(3,3,4)

x1+x2              # 6 8 10 11
                   # recycling rule

# 3. data frame을 이용하여 다음의 결과를
# 도출하세요
Age <- c(22,25,18,20)
Name <- c("James","Mathew","Olivia","Stella")
Gender <- c("M","M","F","F")
## 출력형태
##    Age    Name     Gender
## 1   22    James      M
## 2   25    Mathew     M

df = data.frame(Age=Age,
                Name=Name,
                Gender=Gender)
df
subset(df, Gender == "M")
subset(df, Gender != "F")
subset(df, Age >= 22)

# 4. 아래의 구문을 실행한 결과는?
x <- c(1,2,3,4,5)
(x*x)[!is.na(x) & x > 2]   # 9 16 25

# (1 4 9 16 25)[(F F T T T)] #Fancy indexing
# (1 4 9 16 25)[]

# 5. 다음의 계산 결과는?
x <- c(2,4,6,8)
y <- c(T,T,F,T)
sum(x[y])

# 6. 제공된 vector에서 결측치(NA)의 개수를
# 구하는 코드를 작성하세요!
var1 <- c(34,55,89,45,NA,22,12,NA,99,NA,100)
sum(is.na(var1))
# 결측치를 제외한 평균을 구하세요!
mean(var1[!is.na(var1)])

# 7. 두개의 벡터를 결합하려 해요!
x1 <- c(1,2,3)
x2 <- c(4,5,6)
c(x1,x2)   # 1 2 3 4 5 6
# vector를 결합해서 matrix를 만들어보아요
rbind(x1,x2)
cbind(x1,x2)

# 8. 다음 코드의 실행 결과는?
x = c("Blue",10,TRUE,20)
is.character(x)   # TRUE











