/*
집합 연산
1. 테이블 교차 결합 : 카타시안곱
2. 테이블 내부 결합 : inner join
3. 테이블 외부 결합 : outer join
*/

-- SELECT * FROM sample72_x; # ABC 세 개의 레코드, 컬럼명 x.
-- SELECT * FROM sample72_y; # ABC 세 개의 레코드, 컬럼명 y.

# 카타시안 곱:  모든 가능한 경우의 수를 조합해서 컬럼을 이어준다.
-- SELECT * FROM sample72_x, sample72_y; # 카타시안 곱.

# 상품2, 메이커 확인
-- SHOW CREATE TABLE 메이커;
-- SHOW CREATE TABLE 상품2;

# 내부 결합 : 상품코드가 같은 것만 가져온다.
-- SELECT * FROM 메이커 AS m, 상품2 AS p WHERE m.`메이커코드` = p.`메이커코드`;

# inner join 명령 이용
SELECT *
FROM sample.`메이커` AS m
INNER JOIN sample.`상품2` AS p
ON m.`메이커코드` = p.`메이커코드`;

# 외부 결합

# 스칼라 서브쿼리


#### 연습문제 ####
# 1. 런던에 위치한 공급자(Supplier)가 생산한 상품 목록 조회 : 도시명, 공금자명, 상품명, 상품가격.
-- DESC suppliers;
-- DESC products;
SELECT *
FROM products 
JOIN suppliers ON products.SupplierID = suppliers.SupplierID;


# 2. 분류가 seafood인 상품 목록(모든 컬럼) 조회: 분류, 상품 모든 컬럼.
# 일대 다 관계: 하나의 category는 여러 개의 product를 가질 수 있지만, 하나의 product는 여러 개의 category를 가질 수 없다.
# join 쓰면 분류가 어떻게 되는지?
-- DESC categories;
-- DESC products;

# 아래처럼 하면 1row 검색됨. 무엇을 잘못하였는가?!
-- SELECT *
-- FROM (SELECT * FROM categories WHERE categories.CategoryName = 'seafood') AS seafood
-- JOIN categories ON categories.CategoryID = seafood.CategoryID;

# cartesian product 이용
SELECT *
FROM products, categories
WHERE products.CategoryID = categories.CategoryID
		AND
		categories.CategoryName = 'Seafood';

# join 이용
SELECT *
FROM products 
		JOIN categories ON products.CategoryID = categories.CategoryID
WHERE categories.CategoryName = 'Seafood';

# 3. 공급자(supplier) 국가별, 카테고리별 상품 건수, 평균 가격: 국가명, 카테고리명, 상품건수, 평균가격.
# 국가가 어디 있는지 찾는다.
-- DESC suppliers;
SELECT country, categoryname, COUNT(productid), AVG(unitprice)
FROM suppliers
		JOIN products ON suppliers.SupplierID = products.SupplierID
		JOIN categories ON products.CategoryID = categories.CategoryID -- 관계가 있는 세 개의 테이블을 모두 join. 새로 테이블을 만들었기 때문에 집계 함수 사용 가능.
GROUP BY country, categoryname;		

# 4. 상품 카테고리별, 국가별, 도시별 주문 건수 2건 이상인 목록: 카테고리명, 국가명, 도시명, 주문건수.
SELECT categoryname, country, city, COUNT(orders.orderID)
FROM customers
	JOIN orders ON orders.CustomerID = customers.CustomerID
	JOIN orderdetails ON orderdetails.OrderID = orders.OrderID
	JOIN products ON products.CategoryID = orderdetails.ProductID
	JOIN categories ON products.CategoryID = categories.CategoryID
GROUP BY categoryName, country, city
HAVING COUNT(orders.orderID) >= 2;

# 강사님 정답
-- 주문, 상품 간 다대다 관계 : orderID와 productID로 특정지어야 한다??
SELECT categories.categoryname, orders.ShipCountry, orders.ShipCity, COUNT(orders.OrderID)
FROM products
	JOIN categories ON products.CategoryID = categories.CategoryID
	JOIN orderdetails ON orderdetails.ProductID = products.ProductID
	JOIN orders ON orders.OrderID = orderdetails.OrderID
GROUP BY categories.CategoryName, orders.shipCity, orders.ShipCountry
HAVING COUNT(orderdetails.OrderID) >= 2;
	
	
# 5. 주문자, 주문정보, 직원정보, 배송자정보 통합 조회: 고객 컬럼 전체, 주문정보 컬럼 전체, 배송자 정보 컬럼 전체(4개 테이블 조회).
SELECT customers.CustomerID, employees.EmployeeID, orders.OrderID, suppliers.SupplierID
FROM customers
	JOIN orders ON orders.CustomerID = customers.CustomerID
	JOIN employees ON employees.EmployeeID = orders.EmployeeID
	JOIN orderdetails ON orderdetails.OrderID = orders.OrderID
	JOIN products ON products.ProductID = orderdetails.ProductID
	JOIN suppliers ON suppliers.SupplierID = products.SupplierID;



-- SELECT *
-- FROM customers
-- 	JOIN orders ON orders.CustomerID = customers.CustomerID
-- 	JOIN employees ON employees.employeeID = orders.EmployeeID; --직원 정보
-- 	--JOIN orderdetails ON orderdetails.OrderID = ;