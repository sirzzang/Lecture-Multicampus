# 데이터 입출력
# 키보드로부터 데이터를 받을 수 있어요!
# scan() 함수를 이용해서 숫자데이터를 받을 수 있어요!!
myNum <- scan()
myNum

# scan()을 이용해서 문자열도 입력받을 수 있어요!!
var1 = scan(what=character())
var1

# 키보드로부터 데이터를 받기 위해서 
# edit() 함수를 이용할 수 있어요!

var1 = data.frame()

df = edit(var1)
df

#######################################

# 파일로부터 데이터를 읽어보아요!

# text 파일에 ","로 구분된 데이터들을 읽어들여 보아요!!

# read.table()을 사용
getwd()
# c:/R_Lecture/data
setwd(str_c(getwd(),"/data"))
# 한글을 사용할 경우 fileEncoding = "UTF-8" 설정
# 파일에 header가 있는 경우 header=T 설정
student_midterm = read.table(file="student_midterm.txt",sep=",",fileEncoding = "UTF-8", header = T)

student_midterm = 
  read.table(file.choose(),
             sep=",",
             fileEncoding = "UTF-8",
             header = T)

student_midterm

############################################

var1 = c("홍길동")  # scalar
var2 = c(10,20,30)

rm(list=ls()) # 환경창에 있는 객체들 삭제
cat("\014")  # console clear

###########################################

# 파일로 부터 데이터를 읽어들일때 
# 일반 txt 형식은 많이 사용되지 않아요!

# 컴퓨터간에 데이터를 주고 받으려고 해요

# process 간에 데이터 통신을 하기 위해서
# 특정 형식을 이용해 데이터를 주고 받아요!


# 1. CSV( comma seperated value )
# comma기호를 이용해서 데이터를 구분.
# 해당 문자열을 전달해서 데이터 통신
# 예) "홍길동,20,서울,김길동,30,부산,최길동,50,인천,..."
# CSV 방식 장점 : 간단해요. 부가적인 데이터가 
# 적어요. 상대적으로 크기가 작아요! => 많은 양의 데이터를 처리할 수 있어요!
# CSV 방식 단점 : 구조적 데이터를 표현하기에
# 적합하지 않아요! => parsing작업이 복잡해요
# 유지보수에 문제가 발생해요!

# 2. XML 방식
# tag를 이용해서 데이터를 표현하는 방식
# 예) <name>홍길동</name><age>20</age><address>서울</address>
# <phone>
#     <mobile>010-111-2221</mobile>
#     <home>02-342-2233</home>
#  </phone>
# 장점 : 구조적데이터를 표현하기에 적합, 사용하기 편리, 데이터의 의미를 표현할 수 있어요
# 단점 : 부가적인 데이터가 너무 커요!

# 3. JSON ( JavaScript Object Notation)
# 예) { name : "홍길동", age : 20, address : 서울 ,...}
# 구조적 표현이 가능하면서 XML보다 크기가 
# 작아요!! 

# read.table() : sep가 있어야 해요!
# read.csv() : sep가 ","이기 때문에 생략
#            : header =T 가 기본
getwd()

df = read.csv(file.choose(),
              fileEncoding = "UTF-8")
df

# Excel 파일을 불러올 수 있어요!
# 확장 package를 이용해야 해요!

# R을 설치하면.. => base system이 설치된다고 표현해요!
# base package, recommended package
# other package

# xlsx package를 설치하고 로딩해요!
install.packages("xlsx")
library(xlsx)

# JAVA_HOME 환경변수 설정
Sys.setenv(JAVA_HOME="C:\\Program Files\\Java\\jre1.8.0_231")

student_midterm <- 
  read.xlsx(file.choose(),
            sheetIndex = 1,
            encoding = "UTF-8")

student_midterm
class(summary(student_midterm))
#########################################

# 처리된 결과를 file에 write 해요!
# write.table() : data frame을 file에 저장
# cat() : 분석결과(vector)를 file에 저장
# capture.output() : 분석결과(List,table)을 file에 저장

cat("처리된 결과는 :","\n","\n",
    file="C:/R_Lecture/data/report.txt",
    append=T)

  write.table(student_midterm,
            file="C:/R_Lecture/data/report.txt",
            row.names = F, # 행번호 삭제!
            quote = F,     # "" 삭제
            append = T)

capture.output(summary(student_midterm),
               file="C:/R_Lecture/data/report.txt",
               append = T)

# write.xlsx()

df = data.frame(x=c(1:5),
                y=seq(1,10,2),
                z=c("a","b","c","d","e"),
                stringsAsFactors = F)
df

write.xlsx(df,"C:/R_Lecture/data/report.xlsx")
















  
