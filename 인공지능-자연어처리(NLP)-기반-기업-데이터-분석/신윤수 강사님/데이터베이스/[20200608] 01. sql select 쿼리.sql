-- DESC SAMPLE21; #데이터 스키마 조회

/*
SELECT 문: 데이터 조회
- select : 한 개 이상의 컬럼 조회 가능.
- where : 조건에 맞는 행 검색을 위해 지정.
	- !=, <> : 비교연산자, 같지 않음.'
	- is NULL : NULL 검색.
- from : 대상 테이블.
- order by : 정렬.
	- limit : 결과 행 제한. MySQL, PostgreSQL에서만 지원.
	- offset : 어디서부터 가져올 지 결과행 제한 위치.
*/

SELECT * FROM SAMPLE21; #전체 컬럼
SELECT NAME FROM SAMPLE21; #특정 컬럼
SELECT NAME, BIRTHDAY FROM SAMPLE21;

SELECT * FROM sample34;
SELECT sample34.quantity FROM sample.sample34; # DB 내 객체는 name space.


SELECT * FROM sample21 WHERE NO=3;
SELECT birthday, name FROM sample21 WHERE NAME='홍길동';
SELECT * FROM sample21 WHERE NO>1;
SELECT * FROM sample21 WHERE NO<>1; #no가 1이 아닌 레코드
SELECT * FROM sample21 WHERE no != 2;

-- SELECT * 
-- FROM sample21
-- WHERE NO != 1; #개행해도 괜찮음.

-- SELECT * FROM sample21 WHERE birthday IS NULL; #null값 검색
-- SELECT * FROM sample21 WHERE birthday IS NOT NULL; #null이 아닌 값 검색


-- SELECT * FROM sample24;
-- SELECT * FROM sample24 WHERE a=1 OR b=2;
-- SELECT * FROM sample24 WHERE b=2 AND a=2;

-- SELECT * FROM sample24 WHERE b=0 OR 2; 
##2는 True이므로 비교 연산자가 논리 연산자보다 우선되어 다 가져옴.
-- SELECT * FROM sample24 WHERE b IN (0, 2);
-- SELECT *
-- FROM sample24
-- WHERE (a=1 OR a=2) AND (b IN (0, 2));
##보통 AND가 OR보다 우선순위가 높다. 그러나 동시에 쓸 때는 괄호로 우선순위 명시하자.

-- SELECT * FROM sample25;
-- SELECT * FROM sample25 WHERE TEXT LIKE 'sql%'; #sql로 시작하는 문장
-- SELECT * FROM sample25 WHERE TEXT LIKE '%sql%'; #sql이 포함된 문장

#이스케이프 코드
-- SELECT *
-- FROM sample25
-- WHERE TEXT LIKE '%\%%'; # % 기호가 들어 있는 문장 검색

-- SELECT *
-- FROM sample25
-- WHERE TEXT LIKE '%''%'; # 따옴표 두 개 하면 이스케이프 가능

# NULL 정렬: DBMS마다 다름.
# mysql: 제일 위에
-- SELECT * FROM sample31 ORDER BY age;
-- SELECT * FROM sample31 ORDER BY address DESC;
-- SELECT * FROM sample31 ORDER BY age DESC;
-- SELECT * FROM sample31 ORDER BY age DESC, address ASC;

# limit: 결과 행 제한
-- SELECT * FROM sample33; # 전제 확인
-- SELECT * FROM sample33 LIMIT 3; # 상위 3개 제한.
# order by 후 limit 걸면 정렬 순서대로 온다.
-- SELECT * FROM sample33 ORDER BY NO DESC LIMIT 3;
# offset : 데이터 가져오는 걸 시작할 위치.
-- SELECT * FROM sample33 ORDER BY NO DESC LIMIT 3 OFFSET 3;
-- SELECT * FROM sample33 OFFSET 3; # 이건 안 된다!

# 

































