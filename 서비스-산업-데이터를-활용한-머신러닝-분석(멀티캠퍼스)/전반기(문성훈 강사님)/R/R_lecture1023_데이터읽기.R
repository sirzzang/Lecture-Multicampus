# 데이터 입출력
# Input, output : IO.
# 키보드로부터 데이터를 받을 수 있어요!
# data를 직접 typing하는가, 혹은 프로그램 실행하면서부터 바로 데이터를 받는가.
# 예컨대, scan()함수를 이용해서 숫자데이터를 받을 수 있어요!


#키보드로부터 숫자 형태를 받아들임.

# scan()을 이용해서 문자열도 입력받을 수 있어요!
var1 = scan(what=character())
var1
  # what 뒤에 어떤 속성을 받을 것인지 쓰면 됨
var1

var2 = scan(what=character())
var2

var3 = scan()
var3

#키보드로부터 데이터를 받기 위해서 edit() 함수를 이용할 수 있어요!
#data frame을 띄워서 입력받아서 수정하는.

# 직접 데이터 프레임 편집기 떠서 사용할 수 데이터 받을 수 있음

var4 = data.frame()
df = edit(var4)


##############################

# 파일로부터 데이터를 읽어 보아요!

# text 파일에 ","로 구분된 데이터들을 읽어들여 보아요!

# 파일이 있어야 데이터를 읽든 말든 할테니.
# 메모장 대용으로 notepad++ 사용: 충돌 문제 없음.
# working directory(C, Rlecture, data 폴더 안에 txt 파일로 넣음.)


# read.table()을 사용.
getwd()
# C:/R_lecture1021     /data 문자열 2개 합쳐서 내가 사용할 경로 만들어야 함.
setwd(str_c(getwd(), "/data"))
# working directory 잠깐 다시 설정: 그래야 데이터 읽을 수 있으니까.
getwd()
# working directory 다시 설정하고 getwd 해보면 working directory 바뀐 것을 확인할 수 있음.

student_midterm = read.table(file="student_midterm.txt", sep=",")
  #sep : 데이터가 무엇으로 구분되어 있는가.


