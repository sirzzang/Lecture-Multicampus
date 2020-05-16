##### factor #####
# 범주형 데이터를 저장하기 위한 자료구조: 자료를 몇 개의 level로 정리해서 빈도수 등 통계치를 쉽게 구할 수 있음.
# 범주형 데이터는 예를 들어 방의 크기가 "대", "중", "소" => level
# 일반적을 vector를 이용해서 factor를 만들어요.

#6명의 혈액형 데이터를 vector에 저장하고 factor로 변형해보아요!

var1 = c("A", "AB", "O", "A", "B", "B")
var1 #character 형태의 벡터 형성 : 아직 factor는 아니고 vector일 뿐.

# 범주형 데이터 factor로 바꿔 보자.

factor_var1 = factor(var1) 
#factor 함수 안에 해당 변수를 넣어줌.
factor_var1
# A, AB, B, O 등 값들이 어떤 범주를 가지고 있는지 level 제공됨.
# factor 만들 때 level 지정해줄 수 있음. 지정하지 않으면 함수가 알아서 어떤 level이 될 것 같다고 보고 지정함.

nlevels(factor_var1) # 4, level의 개수.
levels(factor_var1) # 해당 factor의 level들만 출력: 어떤 level이 factor 안에 포함되어 있는지.
is.factor(factor_var1) # factor도 factor인지 아닌지 확인작업 가능 : TRUE.

####################################################################################

# factor 언제 사용? 주로 빈도. 범주형 데이터로 나눠서 해당 범주에 대한 빈도 수 구할 때 사용.
# 간단하게 프로그래밍, 함수 이용해 구할 수도 있지만, factor이용하면 더 쉽고 빠르게 처리 가능.

# 남성과 여성의 성별 데이터로 factor를 생성하고, 빈도수를 구해보아요!

var1 = C("MAN", "WOMAN", "MAN", "MAN", "MAN", "WOMAN") # 남성 4명, 여성 2명인 벡터.
var1
factor_gender = factor(var1)
factor_gender
table(factor_gender) # 범주가 나오고 그 범주에 몇 명이 속해 있는지 안에 있는 데이터 계산해서 빈도수 나옴.
plot(factor_gender) # 빈도수를 알아내면 그래프 그릴 수 있음. 우측 plot 창에 바로 빈도수 가지고 그래프를 그릴 수 있음.




