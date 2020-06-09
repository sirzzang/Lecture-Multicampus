/*
집계 함수
*/

-- SELECT * FROM sample51;

# 총 레코드의 개수 집계
-- SELECT COUNT(*) FROM sample51; # 전체 레코드 개수
-- SELECT COUNT(*) FROM sample51 WHERE NAME='A';
-- SELECT COUNT(NAME) FROM sample51;

# 중복 제거
-- SELECT DISTINCT NAME FROM sample51;
-- SELECT COUNT(DISTINCT NAME) FROM sample51;
SELECT COUNT(all NAME), COUNT(DISTINCT NAME), COUNT(*) FROM sample51;