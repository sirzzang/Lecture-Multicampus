-- View more_than_2orders
CREATE VIEW `more_than_2orders` AS
SELECT categories.categoryname, orders.ShipCountry, orders.ShipCity, COUNT(orders.OrderID)
FROM products
	JOIN categories ON products.CategoryID = categories.CategoryID
	JOIN orderdetails ON orderdetails.ProductID = products.ProductID
	JOIN orders ON orders.OrderID = orderdetails.OrderID
GROUP BY categories.CategoryName, orders.shipCity, orders.ShipCountry
HAVING COUNT(orderdetails.OrderID) >= 2;

-- View 조회
SELECT *
FROM more_than_2orders;