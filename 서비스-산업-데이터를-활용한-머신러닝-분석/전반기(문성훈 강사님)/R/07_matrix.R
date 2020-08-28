# matrix : 동일한 data type을 가지는 2차원 형태의 자료구조
# matrix의 생성
var1 = matrix(c(1:5)) # matrix의 생성기준은 열!!
var1  #      [,1]
      #[1,]    1
      #[2,]    2
      #[3,]    3
      #[4,]    4
      #[5,]    5

var1 = matrix(c(1:10), nrow=2)
var1 # 2행 5열 짜리 매트릭스

var1 = matrix(c(1:10), nrow=5, ncol=10)
var1
var1 = matrix(c(1:10), nrow=3); var1
# recycling rule 적용됌

var1 = matrix(c(1:10), nrow=2, byrow = T); var1
# byrow는 행기준으로 데이터를 채워나간다

var1 = matrix(c(1:10), nrow=2, ncol=3)
var1

# vector를 연결해서 matrix를 만들 수 있다.
# vector를 가로방향, 세로방향으로 붙여서 2차원 형태로 만들 수 있다!
var1 = c(1,2,3,4); var1
var2 = c(5,6,7,8); var2

mat1 = rbind(var1, var2) # rbind 를 이용해서 row끼리 붙인다
mat1
[,1] [,2] [,3] [,4]
var1    1    2    3    4
var2    5    6    7    8

mat2 = cbind(var1, var2); mat2 # cbind 를 이용해서 colum 끼리 붙인다

var1 = matrix(c(1:21), nrow=3, ncol=7); var1
var1[1, 7] # matrix의 행과 열의 index번호로 추출
var1[2,] # 2행의 모든 열을 다 가지고 온다
var1[,5] # 5열의 모든 행을 다 가지고 온다
var1[c(2,3),c(4,5)] # 앞에서 배웟던 내용으로 응용해서 추출할 수 있다.

length(var1) # 원소 개수
nrow(var1)
ncol(var1)

# matrix에 적용할 수 있는 함수가 있다.
# apply() 함수 이용해서 matrix에 특정함수를 적용
# apply() 함수는 속성이 3개 들어감 apply(X=, MARGIN= ,FUN=)
# X => 적용할 matrix
# MARGIN => 1이면 행 기준, 2이면 열 기준
# FUN => 적용할 함수명
apply(X=, MARGIN= ,FUN=)

var1 = c(20, 60, 90, 100, 40, 76, 99); var1
mean(var1)
var1 = matrix(c(1:21), nrow=3, ncol=7); var1
apply(X = var1, MARGIN = 1 ,FUN = max) # 19 20 21
# 이미 우리에게 제공되는 함수만 이용할 수 있는게 아니라 
# 우리가 적용할 함수를 직접 만들어서 사용할 수 있다.

# matrix의 연산
# matrix의 요소단위의 곱연산
# 전치행렬을 구해보자
# 행렬곱(matrix product)
# 역행렬(matrix inversion)

var1 = matrix(c(1:6), ncol=3); var1
var2 = matrix(c(1,-1,2,-2,1,-1), ncol=3); var2
var3 = matrix(c(1,-1,2,-2,1,-1), ncol=2); var3
# elementwise product (요소단위 곱연산)
var1 * var2
# matrix product (행렬곱)
var1 %*% var3

# 전치행렬 ( transpose)
var1
t(var1) # 행이 열로 열이 행으로

# 역행렬 : matrix A가 N x N일 때 다음의 조건을 만족하는 행렬 B가 존재하면 행렬 #          B를 A의 역행렬 이라고 함
# AB = BA = I(단위행렬 E)
var1 = matrix(seq(3,15,2),ncol = 3); var1
solve(var1)

                  [,1]            [,2]           [,3]
[1,] -0.0952380952381 -0.892857142857  0.8214285714286
[2,]  0.0238095238095  0.535714285714 -0.3928571428571
[3,]  0.0714285714286 -0.142857142857  0.0714285714286

##########################################################################

# Array : 3차원 이상. 같은 데이터 타입으로 구성
var1 = array(c(1:24), dim = c(3,2,4)) # 행 열 면 순서
var1

