# R의 주석은 #을 이용해요..
# 주석을 이용하면 한 줄이 몽땅 comment처리

# 일반적으로 프로그래밍언어에서 statement를종료하기 위해서 사용하는 ";"
# R은 ";"를 생략할 수 있어요!
3+5; 3+6; 2*7;
3+5
# 코드를 수행하기 위해서는 Ctrl+Enter를 사용
# R은 대소문자를 구별해요.
# 변수를 만들때 camelcase를 이용해요.
# 
result = 100;
myResult  # camelcase notation
MyResult  # pascal notation
my_result
myresult = 200 # 먼가 이상해요!!
####################################

myResult = 200   # assignment
myResult <- 300  # assignment
400 -> myResult  # assignment
myResult
print(myResult)  # 변수 출력
# 여러개의 값을 출력하려면 cat()
cat("결과값은 : ",myResult)

#################################
# 멤버를 이용한 변수 선언
goods.price = 3000
goods.code = "001"
goods.name = "냉장고"

################################
# 출력되는 형식을 살펴보아요!
mySeq = seq(100)   # 1부터 100까지 1씩 증가하는 숫자의 집합
mySeq = seq(5,100) # 5부터 100까지 1씩 증가하는 숫자의 집합
mySeq = seq(1,100,by = 2)
mySeq





