# SQL 연습문제           
# join을 걸어서 하려고 하지 말고, 한 번에 다 선언해 놓고 진행하자!

# 1. 런던에 위치한 공급자(supplier)가 생산한 상품 목록 조회: 도시명, 공급자명, 상품명, 상품가격
# Q) 아니 뭔데 둘이 실행결과가 다른가요?
SELECT City, ContactName, ProductName, UnitPrice
FROM products AS P
	JOIN suppliers AS S ON S.SupplierID = P.SupplierID
WHERE S.City = 'London';
-- 
SELECT city, contactname, productname, unitprice
FROM suppliers s, products p
WHERE s.SupplierID = p.SupplierID AND s.city = 'london';

# 2. 분류가 Seafood인 상품 목록(모든 컬럼 조회) : 분류, 상품 모든 컬럼.
SELECT *
FROM products p
	JOIN categories c ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'seafood';

SELECT *
FROM products p, categories c
WHERE p.CategoryID = c.CategoryID AND c.CategoryName = 'seafood';


# 3. 공급자(supplier) 국가별, 카테고리별 상품 건수, 평균가격 : 국가명, 카테고리명, 상품건수, 평균가격.
SELECT country, categoryname, COUNT(productid) AS cnt_products, AVG(unitprice) AS avg_price
FROM products AS P
	JOIN suppliers AS S ON S.SupplierID = P.SupplierID
	JOIN categories AS C ON C.CategoryID = P.CategoryID
GROUP BY country, categoryname;

SELECT country, categoryname, COUNT(productid) AS cnt_products, AVG(unitprice) as avg_price
FROM products p, suppliers s, categories c
WHERE p.SupplierID = s.SupplierID AND c.CategoryID = p.CategoryID
GROUP BY country, categoryname;


# 4. 상품 카테고리별, 국가별, 도시별 주문건수 2건 이상인 목록 : 카테고리명, 국가명, 도시명, 주문 건수.
-- 주문건수: orders?
-- invalid use of group function 오류 많았다!

SELECT categoryname AS 카테고리, shipcountry AS 국가명, shipcity AS 도시명, COUNT(O.orderID) AS 주문건수
FROM orders AS O
	JOIN orderdetails AS OD ON O.OrderID = OD.OrderID
	JOIN products AS P ON P.ProductID = OD.ProductID
	JOIN categories AS C ON C.CategoryID = P.CategoryID
GROUP BY categoryname, shipcountry, shipcity
having COUNT(O.orderID) >= 2;

SELECT categoryname AS 카테고리, shipcountry AS 국가명, shipcity AS 도시명, COUNT(o.orderID) AS 주문건수 
FROM orders o, orderdetails od, products p, categories c
WHERE o.OrderID = od.OrderID AND od.ProductID = p.ProductID AND p.CategoryID = c.CategoryID  -- invalid use of group function AND COUNT(o.orderID) >= 2
GROUP BY categoryname, shipcountry, shipcity
HAVING COUNT(o.orderID) >= 2;


# 5. 주문자, 주문정보, 직원정보, 배송자정보 통합 조회: 고객 컬럼 전체, 주문 정보 컬럼 전체(order, orderdetail), 배송자 정보 컬럼 전체.
SELECT *
FROM customers AS C
	JOIN orders AS O ON O.customerid = C.customerid
	JOIN orderdetails AS OD ON OD.orderid = O.OrderID
	JOIN employees AS E ON E.EmployeeID = O.EmployeeId;
-- 
SELECT *
FROM customers c, orders o, orderdetails od, employees e
WHERE c.CustomerID = o.CustomerID AND o.OrderID = od.OrderID AND o.EmployeeID = e.EmployeeID;

# 6. 판매량 상위 3위까지 공급자 목록: 공급자 명, 판매량, 판매금액
-- 판매량이 어디에 있는가? quantity??
SELECT contactname AS 공급자명, sum(OD.quantity) AS 판매량, sum(OD.quantity*OD.unitprice) AS 판매금액
FROM orderdetails AS OD
	JOIN orders AS O ON OD.OrderID = O.OrderID
	JOIN products AS P ON P.ProductID = OD.ProductID
	JOIN suppliers AS S ON S.SupplierID = P.SupplierID
GROUP BY contactname
ORDER BY SUM(OD.quantity) DESC
LIMIT 3;
-- 
SELECT contactname AS 공급자명, SUM(od.quantity) AS 판매량, SUM(od.quantity*od.unitprice) AS 판매금액
FROM orders o, orderdetails od, products p, suppliers s
WHERE o.OrderID = od.OrderID AND od.ProductID = p.ProductID AND p.SupplierID = s.SupplierID
GROUP BY contactname
ORDER BY SUM(od.quantity) DESC
LIMIT 3;

# 7. 상품 분류별, 고객 지역별 판매량 순위: 순위, 카테고리명, 고객지역명, 판매량 -- 판매량 합인가????????
# 순위...
SET @rownum:=0;
SELECT categoryname, shipcity, sum(quantity) -- SUM(quantity) AS 판매량 순위
FROM products AS P
	JOIN categories AS C ON P.CategoryID = C.CategoryID
	JOIN orderdetails AS OD ON OD.ProductID = P.ProductID
	JOIN orders AS O ON OD.OrderID = O.OrderID
GROUP BY categoryname, shipcity
ORDER BY sum(quantity)desc;

SELECT categoryname, shipcity, SUM(quantity)
FROM products p, categories c, orders o, orderdetails od
WHERE p.CategoryID = c.CategoryID AND od.ProductID = p.ProductID AND o.OrderID = od.OrderID
GROUP BY categoryname, shipcity;

# 8. 고객 국가가 USA이고, 상품별 판매량(quantity 수량 합계) 순위: 국가명, 상품명, 판매량, 판매금액
# 순위....



# 9. supplier의 국가가 germany인 상품 카테고리별 상품 수: 국가명, 카테고리명, 상품수
SELECT country, c.categoryName, COUNT(*)
FROM products AS p
	JOIN suppliers AS s ON s.SupplierID = p.SupplierID
	JOIN categories AS c ON c.CategoryID = p.CategoryID
WHERE s.Country = 'germany'
GROUP BY p.categoryID, c.categoryName;

# 9. supplier의 국가가 germany인 상품 카테고리별 상품 수: 국가명, 카테고리명, 상품수
SELECT *
FROM suppliers s, products p, categories c	
WHERE s.supplierId = p.supplierId AND p.CategoryID = c.CategoryID AND s.Country = 'germany';
-- GROUP BY c.CategoryName;
-- ------------------------------------------------

SELECT country, categoryname, quantity
FROM suppliers s, orders o, categories c, products p, orderdetails o2
WHERE s.supplierId = p.supplierId AND p.CategoryID = c.CategoryID AND o2.ProductID = p.ProductID AND o.OrderID = o2.OrderID AND s.Country = 'germany'
GROUP BY c.CategoryName;
-- 
-- # 10. 월별 판매량 및 판매금액 : 연도, 월, 판매량, 판매금액
SELECT YEAR(o.orderdate) AS 연도, MONTH(o.OrderDate) AS 월, quantity AS 판매량, quantity*unitprice AS 판매금액 -- quantity, unitprice
FROM orders o, orderdetails od
WHERE o.OrderID = od.OrderID
GROUP BY MONTH(o.orderdate); -- group by year, month인지?

SELECT SUM(Quantity), SUM(Quantity)*unitprice, LEFT(orderDate,7) 
FROM orderdetails a 
	INNER JOIN orders b ON a.OrderID = b.OrderID
GROUP BY LEFT(orderDate,7);