/*
집계 함수
1. 종류
	- count : 레코드의 개수 집계
	- sum : 레코드의 합
	- avg : 레코드의 평균
	- min : 최솟값
	- max : 최댓값

2. 그룹핑
	- 집계 함수의 활용 범위를 넓힘.
	- group by: 전체 데이터에 대해 집단 그룹핑. where보다 먼저 실행되므로, 그룹핑 후 집계함수를 사용해야 함.
	- having: 그룹핑된 데이터에 대해 조건을 지정.

	
3. 



*/

-- SELECT * FROM sample51;

# count
-- SELECT COUNT(*) FROM sample51; # 전체 레코드 개수
-- SELECT COUNT(*) FROM sample51 WHERE NAME='A';
-- SELECT COUNT(NAME) FROM sample51;

# 중복 제거
-- SELECT DISTINCT NAME FROM sample51;
-- SELECT COUNT(DISTINCT NAME) FROM sample51;
-- SELECT COUNT(all NAME), COUNT(DISTINCT NAME), COUNT(*) FROM sample51;

# sum, avg, min, max
-- SELECT SUM(quantity), AVG(quantity), MIN(quantity), MAX(quantity) FROM sample51;
-- SELECT SUM(quantity), AVG(quantity), MIN(quantity), MAX(quantity) FROM sample51 WHERE NAME='A'; # 이름이 A인 조건 추가

# sample data 추가
-- DESC sample51;
-- INSERT INTO sample51
-- VALUES (6, 'B', 5), (7, 'D', 10), (8, 'B', 13);
-- SELECT * FROM sample51; # 데이터 추가 확인

# 그룹핑하여 집계
-- SELECT NAME, SUM(quantity) AS SUM, AVG(quantity) AS AVG FROM sample51 GROUP BY NAME;
-- SELECT NAME, SUM(quantity) AS SUM FROM sample51 GROUP BY NAME HAVING SUM(quantity) > 5; # having구를 이용해 quantity의 합이 5보다 큰 것들만 출력
-- SELECT NAME, quantity, COUNT(NAME) FROM sample51 GROUP BY NAME, quantity; # name, quantity의 순서쌍에 대해서 집계함수 적용.

# sample data 추가
-- INSERT INTO sample51 VALUES (10, 'A', 1), (11, 'A', 3);
-- SELECT NAME, quantity, COUNT(NAME), SUM(quantity) FROM sample51 GROUP BY NAME, quantity;


/*
서브쿼리
: select 명령에 의한 데이터 질의, 하부 부수적 질의.

<종류>
1. 스칼라 쿼리 : 값이 하나로 나오는 쿼리.
2. 그 외
	- 복수의 행, 하나의 열.
	- 하나의 행, 복수의 열.
	- 복수의 행, 복수의 열.
	
<상관쿼리>
- EXISTS : where절에서 존재하면
- NOT EXISTS : where절에서 존재하지 않으면,
*/

# 최솟값 제거를 위한 서브쿼리
-- SELECT MIN(quantity) FROM sample51; # 최솟값을 찾는다.
-- SELECT * FROM sample51 WHERE quantity = (SELECT MIN(quantity) FROM sample51); # 나온 데이터를 통해 조회한다.

# MariaDB에서는 delete가 오류가 난다. 10.3 버전부터 가능!
-- DELETE FROM sample51 WHERE quantity = (SELECT MIN(quantity) FROM sample51); # 에러: target table specified twice.

# alias를 통해 해결해야 한다.
-- DELETE FROM sample51
-- WHERE quantity = (
-- 						SELECT *
-- 						FROM (
-- 								SELECT s.quantity 
-- 								FROM sample51 s
-- 								WHERE quantity=MIN(quantity))	as s); --> 서브쿼리에 where ㄴㄴ해~
								
DELETE FROM sample51
WHERE quantity = 
			(
				SELECT * 
				FROM (
							SELECT MAX(quantity) 
							FROM sample51) AS MAX_delete);
SELECT * FROM sample51;						

# 클라이언트 변수 활용
SET @a = (SELECT MIN(a) FROM sample54); # 변수에 저장
DELETE FROM sample54 WHERE a=@a;
SELECT * FROM sample54;	


# select문에서의 서브쿼리, 별칭 사용.
SELECT
	(SELECT COUNT(*) FROM sample51) AS sq1,
	(SELECT COUNT(*) FROM sample54) AS sq2;

# 중첩 구조
SELECT * FROM sample35;
SELECT * FROM (SELECT * FROM sample51) sq;

# 상관 서브쿼리: exists
SELECT * FROM sample551;
SELECT * FROM sample552; # no2 : 3, 5
UPDATE sample551 SET a='있음' WHERE EXISTS(SELECT * FROM sample552 WHERE NO2=NO);
SELECT * FROM sample551;

# not exists
UPDATE sample551
SET a = '없음'
WHERE NOT EXISTS(SELECT * FROM sample552 WHERE NO2=NO);
SELECT * FROM sample551;

# in 키워드
SELECT *
FROM sample551
WHERE NO IN (
					SELECT NO2
					FROM sample552
				);
				
/*
집합연산
- 각 컬럼의 데이터 타입과 행, 열의 개수가 같아야 함.
*/


# 1. 합집합 : union(중복 제거), union all(중복 포함)
SELECT * FROM sample71_a;
SELECT * FROM sample71_b;
SELECT * FROM sample71_a UNION SELECT * FROM sample71_b;
SELECT * FROM sample71_a UNION all SELECT * FROM sample71_b;















