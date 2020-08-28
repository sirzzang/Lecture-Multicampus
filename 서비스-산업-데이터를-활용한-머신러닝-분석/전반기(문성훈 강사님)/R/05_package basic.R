# package 
# R은 기본적으로 설치 시 base package가 같이 설치됨.
# 추가적인 기능을 이용하기 위해서 외부 package를 찾아서 설치해야 함.
# 그래프 그리기 위해서 많이 사용하는 package는 ggplot2를 이용하자.
# package를 설치하기 위해서 
install.packages("ggplot2")
\# 설치된 package를 메모리에 load해야 사용할 수 있다.
library("ggplot2")
require("ggplot2") # 둘중 하나이용

# 간단한 빈도를 나타내는 막대그래프를 그리기 위해 vector 하나 만들어 보자
var1 = c("a","b","c","a","b","a")

qplot(var1)

# package안의 함수를 이용해서 빈도그래프 그려본것!

# 설치된 package를 삭제하려면
remove.packages("ggplot2")

# package가 설치된 폴더 경로를 알아보자

.libPaths()

# package 설치 경로를 변경하고 싶을 때

.libPaths("c:/R_lecture1021/lib")
.libPaths()

# 많은 package에 대한 정보, 사용법 등을 알면 알수록 R을 잘 사용할 수 있다.

# package 를 설치하면 package에서 제공하는 함수를 이용할 수 있다.

help(qplot)

args(qplot)
example(qplot
      )
library(ggplot2)
example(qplot)

# working directory

getwd()
setwd("c:/R_lecture1021/lib")
 