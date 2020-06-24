# 문자열 처리에 대해서 알아보아요!!
# 빅데이터 : 많은 양의 데이터
#          : 3V
#          : 1. Volume : 많은 양의 데이터
#          : 2. Velocity : 데이터 생성 속도   
#          : 3. Variety : 데이터의 다양성          
# 일반적으로 빅데이터 처리는 문자열 처리를 
# 동반하는 경우가 많아요!
# 문자열 처리는 stringr package를 이용하면 
# 쉽게 편하게 할 수 있어요!
install.packages("stringr")
library(stringr)

var1 = "Honggd1234Leess9032YOU25최길동2009"

# 1. 문자열의 길이를 구해보아요!
str_length(var1)  # 31 (한글1글자도 1개)

# 2. 찾는 문자열의 시작과 끝을 알려줘요!
str_locate(var1,"9032")

# 3. 부분문자열을 구해보아요!
str_sub(var1,3,8) # 시작과 끝 둘 다 inclusive

# 4. 대소문자 변경
str_to_lower(var1)
str_to_upper(var1)

# 5. 문자열 교체
var1 = "Honggd1234Hongss9032YOU25최길동2009"
str_replace(var1,"Hong","KIM")
str_replace_all(var1,"Hong","KIM")

# 6. 문자열 결합
var2 = "홍"
var3 = "길동"
str_c(var2,var3)

# 7. 문자열 분할
var1 = "Honggd1234,Leess9032,YOU25,최길동2009"
str_split(var1,",")

# 8. 문자열 결합
var1 = c("홍길동","김길동","최길동")
paste(var1,collapse = " ")

#########################################

# 문자열 처리를 쉽고 편하기 하기 위해서는
# 정규표현식(regular expression)

var1="Honggd1234,Leess9032,YOU25,최길동2034"

# 조건에 부합되는 문자열을 추출
str_extract_all(var1,"[a-z]{4}")
str_extract_all(var1,"[A-Z]{2}")
str_extract_all(var1,"[a-z]{2,}")
str_extract_all(var1,"[a-z]{2,3}")

str_extract_all(var1,"34")

# 한글만 추출해보아요!
str_extract_all(var1,"[가-힣]{2,}")
# 숫자문자를 추출해 보아요!
var1="Honggd1234,Leess9032,YOU25,최길동2034"
str_extract_all(var1,"[0-9]{2,}")

# 한글을 제외한 나머지 문자들 추출
var1="Honggd1234,Leess9032,YOU25,최길동2034"
str_extract_all(var1,"[^가-힣]{5}")

# 주민등록번호를 검사해 보아요!
myId = "801112-1210419"
str_extract_all(myId,"[0-9]{6}-[1234][0-9]{6}")


var1="Honggd1234,Leess9032,YOU25,최길동2034"
a <- str_extract_all(var1,"[^가-힣]")
a
a[[1]]
paste(a[[1]],collapse = "")



