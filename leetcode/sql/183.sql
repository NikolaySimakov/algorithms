-- Leetcode 183
SELECT name AS Customers FROM Customers WHERE NOT EXISTS(SELECT customerId FROM Orders WHERE customerId = Customers.id);