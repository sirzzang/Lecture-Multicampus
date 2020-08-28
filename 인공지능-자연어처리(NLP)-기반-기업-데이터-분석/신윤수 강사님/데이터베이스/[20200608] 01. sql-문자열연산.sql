/*
문자열 연산 : DBMS 종속적.
*/

-- SELECT * FROM sample35;
# 데이터 스키마: value와 unit을 분리해서 저장. ex)IoT : 온도, 습도 등 한 테이블에 모을 때.

# concat : 문자열 합침.
-- SELECT price, CONCAT(quantity, unit) AS amount FROM sample35;

# substring : 문자열 인덱스를 통해 반환.
-- SELECT SUBSTRING('배가너무 아프고 고프고 그렇지만 오늘은폭염주의보...', 1, 10) FROM DUAL;
-- SELECT SUBSTRING('배가너무 아프고 고프고 그렇지만 오늘은폭염주의보...', 3, 5) FROM DUAL;

# trim : 앞뒤로 공백 제거.
SELECT TRIM('     공백이 제 거되 는지 확인해 봅시 다 ...    ') FROM DUAL;

/*
날짜 연산 : DBMS 종속적.
*/
