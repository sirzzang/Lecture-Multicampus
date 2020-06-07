### 자료 구조에 대해 배운 내용을 알아보기 위해 연습 문제를 풀어봅시다 ^-^ ###

# 1)  4, 6, 5, 7, 10, 9, 4, 데이터를 이용해서 숫자형 vector를 생성하세요.
var1<-c(4, 6, 5, 7, 10, 9, 4) # colon, seq, rep는 규칙성이 있어야 하는데 이 숫자들은 규칙성 없다!
var1  
mode(var1)

# 2) 아래의 두 벡터의 연산 결과는?
x1<-c(3,5,6,8)
x2<-c(3,3,4)
x1; x2
x1 + x2 
    # recycling rule 이용해 vector length 맞춘 후 연산 수행. 그러나 오류 메시지 뜬다. 오류메시지 안       뜨려면 recycling rule로 돼서 사이즈가 딱 맞아떨어져야 함.
    # warning은 뭔가 착각하고 있는 것 아닌지 경고하는 것, error는 아예 틀린 것.

# 3) data frame을 이용하여 다음의 결과를 도출하시오.
Age = c(22, 25, 18, 20)
Name = c("James", "Mathew", "Olivia", "Stella")
Gender = c("M", "M", "F", "F")


Age; Name; Gender

question_df <- data.frame(Age = Age[1:2],
                          Name = Name[1:2],
                          Gender = Gender[1:2])
question_df

        #강사님 정답 : subset 사용
        newnewDf= data.frame(Age=Age,
                             Name=Name,
                             Gender=Gender)
        newnewDf
        
        subset(newnewDf, Gender=="M")
        subset(newnewDf, Gender!="F")
        subset(newnewDf, Age>=22)

        
# 4) 아래의 구문을 실행한 결과는?

x <- c(1,2,3,4,5)
(x*x)[!is.na(x) & x>2] #9 16 25
is.na
  # 결측치가 아니고, 2 초과인 애들 벡터 원소끼리 곱해서 연산.
  # x*x : 벡터끼리 연산. (1 4 9 16 25)
  # []: 벡터 안에서 요소 뽑아내려고 하겠지, is.na? 이 값 na야? 하고 물어보는 것. 근데 전부 다 na가 아니니까 false false false false false 이렇게 나오는데 거기에 not이 붙으니까 TTTTT 이러겟찌. 그거랑 & 연산. -> (T T T T T) & (F F T T T) = 앞에 두 원소 날아가고 뒤에 세 개 원소 남아서 결과적으로는 -> (F F T T T)
  # (1 4 9 16 25)[(F F T T T)] : 이렇게 나옴! 뒤에 있는 대괄호[] 안에 있는 애들 가지고 indexing 해야 함. -> fancy indexing이라고 부름,
  # fancy indexing: length가 같은, T, F로 이루어진 벡터.-> 같은 위치에 mapping 시켜서 T 위치에 있는 애들만 남기고 날림. index 부분에 logical type의 벡터가 들어와서 indexing 하는 것을 fancy indexing이라고 해여~~
  # 특이하게 logical type의 벡터가 길이 같을 때 indexing에 사용되면 TRUE(T) 부분만 남고 날아감.
  # 결국, F 자리에 해당하는 1, 4, 날리고 9 16 25만 남겠찌.


# 5) 다음의 계산 결과는?
x<- c(2, 4, 6, 8)
y<- c(T, T, F, T)
sum(x[y]) # 14 나오겟쪄!
      #fancy indexing: 2, 4, 8만 남음. 같은 size의 logical type이 index에 들어왔으니까.


# 6) 제공된 vector에서 결측치가 몇 개가 있는지 개수를 구하는 코드 작성.
var1 <- c(34, 55, 89, NA, 22, 12, NA, 99, NA, 100)
var1

  # NA인지 아닌지 알아내야 함(is.NA) -> sum 해주면 true만 1로 나와서 결측치 개수 알 수 있음.
  var2<-is.na(var1)
  var2
  sum(var2)

# 7) 6)의 vector에서 결측치를 제외한 평균?
  # fancy indexing 사용
mean(var1[!is.na(var1)])

# 8) 두 개의 벡터를 결합하려 해요.
x1<- c(1, 2, 3)
x2<- c(4, 5, 6)

x3<- c(x1, x2)
x3

# 혼동하지 말 것! list vs. c?
list(x1, x2)
c(x1, x2)

# 9) vector를 결합해서 matrix를 만들어 보아요. 행 단위 결합, 열 단위 결합 모두 가능. 2행 3열 matrix
rbind(x1, x2) # 2행 3열
cbind(x1, x2) # 3행 2열

# 10) 다음 코드의 실행 결과는?
x = c("Blue", 10, TRUE, 20) # vector 같은 데이터 타입 사용: 우선순위 높은 character로 바뀜.
x
is.character(x)
is.factor(x)

# 11) 