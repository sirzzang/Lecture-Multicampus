/*
수치 연산 : + - * / % mod
- 나머지 연산의 경우: % 대신 mod를 사용하는 DBMS도 있다.
- 연산 우선순위는 우리가 상식적으로 알고 있는 순위.
*/


-- SELECT * FROM sample34;

# select로 연산하기
-- SELECT *, price*quantity
-- FROM sample34;
-- SELECT *, price*quantity AS amount FROM sample34; # column 별칭, 한글도 가능, 웬만하면 영어로 뽑자.

# where에서의 연산
-- SELECT *, price*quantity AS amount 
-- FROM sample34
-- WHERE amount >= 2000; # 오류: select가 제일 나중에 실행된다!

-- SELECT *, price*quantity AS amount 
-- FROM sample34
-- WHERE price*quantity >= 2000;

# null값과의 연산
-- SELECT 1+NULL FROM DUAL;
-- SELECT 1/NULL FROM DUAL;

# order by에서의 연산 : 여기서는 별칭으로 해도 됨.
-- SELECT *, price*quantity AS amount FROM sample34 ORDER BY price*quantity DESC;
-- SELECT *, price*quantity AS Amount FROM sample34 ORDER BY Amount ASC;

# mod 연산
-- SELECT *, MOD(price, quantity) FROM sample34;
-- SELECT 1000 MOD 3 FROM DUAL;

# round 함수: 반올림. 소수점 뒤 절삭.
-- SELECT * FROM sample341;
-- SELECT *, ROUND(amount) FROM sample341;
-- SELECT ROUND(11.1896) FROM DUAL;
-- SELECT ROUND(11.1896, 2) FROM DUAL; # 뒤에 소수점 몇 자리까지 표시할 것인지 지정 가능.
-- SELECT amount, ROUND(amount, -2) FROM sample341; # 정수 자리로 침범해서 간다. -2이므로, 10의 자리에서 반올림.

# sum, count, 등 함수 있는데, 집계함수에서 배울게요.

