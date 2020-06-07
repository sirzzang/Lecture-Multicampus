# R에서 JSON 데이터 처리

# Network을 통해서 JSON데이터를 받아서 
# Data Frame으로 만들기 위해 새로운 package를
# 이용해보아요!

# 1. package 설치
install.packages("jsonlite")
# Network관련된 package
install.packages("httr")  
# 2. package를 사용하기 위해 loading작업필요
library(jsonlite)

# 3. 문자열 처리하기 위한 package loading
library(stringr)

url <- "http://localhost:8080/bookSearch/search?keyword="

request_url <- str_c(url,
                     scan(what=character()))
# 한글처리
request_url <- URLencode(request_url) 

request_url


# 주소가 완성되었어요!!
df <- fromJSON(request_url)

df
View(df)  
str(df)   # str() : data frame의 구조를 파악
names(df) # 

# 찾은 도서 제목만 console에 출력!
for(idx in 1:nrow(df)) {
  print(df$title[idx])
}

# JSON을 이용해서 Data Frame을 생성할 수 있어요
# data frame을 csv형식으로 file에 저장

write.csv(df,
          file="C:/R_Lecture/data/book.csv",
          row.names = FALSE,
          quote = FALSE)

# Data Frame을 JSON으로 변경하려면 어떻게
# 하나요??
df_json <- toJSON(df)
df_json
prettify(df_json)

write(df_json,
      file="C:/R_Lecture/data/book_json.txt")

write(prettify(df_json),
      file="C:/R_Lecture/data/book_json.txt")

##########################################

# 2018년 10월 30일 박스오피스 순위를
# 알아내서 제목과 누적관람객수를
# CSV파일로 저장하세요!

# 얻어온 데이터에서 필요한 내용만 추출해서
# Data Frame을 새로 생성한 후 파일 출력

# Data Frame에서 로직처리(for문) 해서
# 데이터를 추출해 text 파일에 append해서 
# 파일 출력

########################################

# Web Crawling : 인터넷 상에서 필요한 정보를
# 읽어와서 수집하는 일련의 작업(과정)

# Web scraping
# => 하나의 web page에서 내가 원하는 부분을
#    추출하는 행위
# web crawling(web spidering) : 
# 자동화 봇인 crawler가 정해진 규칙에 따라
# 복수개의 web page를 browsing하는 행위

# scraping을 할 때 CSS(jQuery) selector를 
# 이용해서 필요한 정보를 추출
# selector를 이용해서 추출하기 힘든놈들도
# 있어요!
# 추가적으로 xpath도 이용해 볼 꺼예요.

# 특정 사이트에 접속해서 내가 원하는 데이터를
# 추출해보아요!!

# 1. 서버로 부터 받은 HTML 태그로 구성된
# 문자열을 자료구조화 시키는 패키지를 이용해야
# 해요!!
install.packages("rvest")
library(rvest)
library(stringr)
# 2. url을 준비해요!
url <- "https://movie.naver.com/movie/point/af/list.nhn"
page <- "page="

request_url <- str_c(url,"?",page,1)
request_url
# 3. 준비된 URL로 서버에 접속해서 HTML을 읽어온 후 자료구조화 시켜요!
html_page = read_html(request_url)
html_page
# 4. selector를 이용해서 추출하기 원하는
# 요소(element)를 선택해요!
nodes = html_nodes(html_page,"td.title > a.movie")
nodes
# 5. tag사이에 들어있는 text를 추출해요!
title <- html_text(nodes, trim = TRUE)
title

# 6. selector를 이용해서 리뷰 요소(element)
#    를 선택해요!
nodes = html_nodes(html_page,"td.title")
review <- html_text(nodes, trim = TRUE)
review
  
# 7. 필요없는 문자들을 제거
review = str_remove_all(review,"\t")
review = str_remove_all(review,"\n")
review = str_remove_all(review,"신고")
review

# 8. 영화제목과 리뷰에 대한 내용을 추출
df = cbind(title,review)
View(df)

# 9. 이렇게 구축한 데이터를 파일에 저장해요!

##########################################

# 이번에는 같은 작업을 xpath를 이용해서
# 처리해 보아요!!

install.packages("rvest")
library(rvest)
library(stringr)
url <- "https://movie.naver.com/movie/point/af/list.nhn"
page <- "page="
request_url <- str_c(url,"?",page,1)
html_page = read_html(request_url)
nodes = html_nodes(html_page,"td.title > a.movie")
title <- html_text(nodes, trim = TRUE)
# Review부분은 xpath로 가져와 보아요!

review = vector(mode="character", length=10)
## //*[@id="old_content"]/table/tbody/tr[1]/td[2]/text()
for(idx in 1:10) {
  myPath = str_c('//*[@id="old_content"]/table/tbody/tr[',
                 idx,
                 ']/td[2]/text()')
  nodes = html_nodes(html_page,
                     xpath=myPath)
  txt <- html_text(nodes, trim = TRUE)
  review[idx] = txt[3]  
}
df = cbind(title,review)
View(df)

#########################################

# 반복해서 page를 browsing하는 crawling까지
# 포함해보아요!

extract_comment <- function(idx) {
  url <- "https://movie.naver.com/movie/point/af/list.nhn"
  page <- "page="
  request_url <- str_c(url,"?",page,idx)
  html_page = read_html(request_url,
                        encoding = "CP949")
  nodes = html_nodes(html_page,"td.title > a.movie")
  title <- html_text(nodes, trim = TRUE)
  # Review부분은 xpath로 가져와 보아요!
  
  review = vector(mode="character", length=10)
  
  for(idx in 1:10) {
    myPath = str_c('//*[@id="old_content"]/table/tbody/tr[',
                   idx,
                   ']/td[2]/text()')
    nodes = html_nodes(html_page,
                       xpath=myPath)
    txt <- html_text(nodes, trim = TRUE)
    review[idx] = txt[3]  
  }
  df = cbind(title,review)
  return(df)
}

### 함수를 호출해서 crawling을 해보아요!!
result_df = data.frame();
  
for(i in 1:10) {
  tmp <- extract_comment(i)
  result_df = rbind(result_df,tmp)
}

View(result_df)
















