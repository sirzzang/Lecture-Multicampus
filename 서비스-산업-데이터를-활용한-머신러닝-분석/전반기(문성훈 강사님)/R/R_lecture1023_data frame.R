### data frame ###

# matrix와 같은 2차원 형태의 자료구조.
# matrix와 달리, 다른 데이터 타입도 사용할 수 있음.
# column명을 이용할 수 있음.
# 마치 database의 table과 유사하다고 보면 됨.

# 간단한 예로 data frame 알아보아요.

# vector를 이용해 data frame을 만들어 보아요.

no=c(1, 2, 3)
name=c("홍길동", "김길동", "최길동")
age=c(10, 20, 30)

no; name; age # 벡터 만든거지 지금까지는?

df = data.frame(s_no=no,
                s_name=name,
                s_age=age)
# data frame에서는 column의 이름이 있어야 한다. 그런데 벡터와 이름 동일하면 이상할 수 있으니까 여기서는 s_를 붙여서 column명을 만들고, 그 뒤에 실제 사용할 벡터를 가져올게!

str(df)


# cf) data frame은 recycling rule따위 없다. 오류 나서 밑에 보면 differing number얘기 나오지!
error_df = data.frame(x=c(1:5),
                      y=seq(2, 10, by=2),
                      z=c("a", "b", "c", "d", "e"))
str(error_df)

error_df_2 = data.frame(x=c(1:5),
                        y=seq(2, 10, by=2),
                        z=c("a", "b", "c", "d", "e"),
                        stringsAsFactors = F)
error_df_2
str(error_df_2)

# data frame이 문자열 벡터를 읽어들일 때 factor로 읽어온다...!!

# 가장 간단하게 만드는 방식이었는데
# matrix 있다면 간단하게 data frame 만들 수 있음.
myMatrix = matrix(c(1:12), 
                  ncol=3, 
                  nrow=4, 
                  byrow = T)
myMatrix 
    # 왜 뜬금없이 myMatrix라고 하나요? 변수명을 함수랑 똑같이 하면 나중에 오류날 수 있음. 좋지         않아 굉장히.

# myMatrix를 data frame으로 만들어 볼까요?
df_mat = data.frame(myMatrix) # 그냥 바로 data frame 함수 안에 matrix 넣으면 전환 가능.
    # 가장 큰 차이점: matrix는 column 명이 존재하지 않음. 그런데 data frame은 column명이 필요함. 
    # 지금은 column 이름을 지정하지 않았기때문에 임의로 x1, x2, 등으로 잡힘.
df_mat
    # 실행해 보면 바로 알 수 있지? column 명이 x1, x2, x3 default 값으로 잡힌다!

df[1] # 첫 번째 열 지칭
df$s_name # data frame 안에 있는 s_name 안에 있는 데이터 알고 싶을 때 사용.
  # list에서 $의 의미는 key의 이름 vs. data frame에서 $의 의미는 column.
  # $ 표시 하고 s_name 뽑았더니, 실행 결과가 level, 즉, 범주로 나온다.
  # 이렇게 범주 형태로 raw data 가져 오면 문제가 될 수 있음. 일반적인 문자열(character)로 땡겨       오는 게 편하다.
  # 범주형으로 잡지 않으려면 access할 때 무엇을 봐야 할지 나중에 알려줄게!

df_mat[1]; df[1]
df_mat$s_name; df$s_name



### data frame의 함수##

#1. str: data frame의 전반적인 구조(행의 개수, 열의 개수, 각 행의 자료 타입 등)
str(df) 
        # obs: data frame 안에 몇 개의 행이 있는지.
        # variable: data frame 안에 몇 개의 열이 있는지.
        # $ ~~ : column 이름, num: numeric - 데이터 구조.
        
#2. summary: 요약통계 - 간단한 통계량 보여줌.
summary(df)
            # s_no, s_age와 같은 숫자 자료에 대해서는 최소, 최대, 사분위값 등.
            # s_name은 factor 자료니까 빈도수. 최소, 최대 등 통계량 없으니까.

#3. apply: 행 단위, 열 단위로 특정 함수(최대값, 최소값, 평균값 등) 적용.
apply(X=df, MARGIN=1, FUN=min)
apply(X=df, MARGIN=2, FUN=mean)
apply(X=df, MARGIN=1, FUN=max)

df

    # Q) 연습문제: 아래의 data frame의 1, 2번째 column에 대해 각각의 합계를 구하라!
    new_df = data.frame(x=c(1:5),
                    y=seq(2, 10, 2),
                    z=c("a", "b", "c", "d", "e"))
    new_df
    
    apply(X=new_df[1:2], MARGIN=2, FUN=sum)
    apply(X=new_df[-3], MARGIN=2, FUN=sum)
    apply(X=new_df[, c(1:2)], MARGIN=2, FUN=sum)
    
    apply(X=new_df, MARGIN=2, FUN=sum)
    # 위와 같은 방식이 오류가 나는 이유? Z 열이 FACTOR니까 합계에 사용될 수 없음.
    
    
    # s_name이 왜 factor???? : str 함수에서 속성 알려줄 때는 그냥 의미 없게 나오는 건가???

    
#4. subset: 하나의 data frame 안에서 건에 맞는 행만 추출해서 독립적인 data frame을 생성.
    
again_df = data.frame(x=c(1:5),
                      y=seq(2, 10, 2),
                      z=c("a", "b", "c", "d", "e"))
again_df                      

subset(again_df, x>3)
# subset 문법: 앞에 데이터 프레임 놓고, 뒤에다가 각 열 에 맞게 조건 넣음.

# Q) x가 3보다 작고, y가 10 이상인 데이터 추출
    subset(again_df, x>3 & y>=10)
    subset(again_df, x<2 & y<5)

#subset 이용해 새로운 data frame 형성하려면?    
df_subset <- subset(again_df, x<4 | y>=10)
df_subset

#### 여기까지 6개의 자료구조에 대해 알아보았습니다!! :) ####
