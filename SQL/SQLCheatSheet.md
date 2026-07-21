# Comprehensive MySQL Cheat Sheet

> Covers MySQL 8.x syntax and features from beginner to advanced.

---

# Table of Contents

1. Basic Data Retrieval
2. Filtering Data
3. Sorting & Limiting
4. Aliases
5. Aggregate Functions
6. GROUP BY & HAVING
7. String Functions
8. Numeric Functions
9. Date & Time Functions
10. NULL Handling
11. Conditional Logic
12. Joins
13. Set Operations
14. Subqueries
15. Common Table Expressions (CTE)
16. Window Functions
17. Views
18. Indexes
19. Constraints
20. Database Operations
21. Table Operations
22. Data Types
23. INSERT
24. UPDATE
25. DELETE
26. TRUNCATE vs DELETE vs DROP
27. Transactions
28. Stored Procedures
29. Functions
30. Triggers
31. Events
32. User & Privileges
33. JSON Functions
34. Performance Tips
35. Useful Operators
36. Common SQL Execution Order
37. Cheat Sheet Summary

---

# 1. Basic Data Retrieval

The most basic SQL statement.

```sql
SELECT * FROM users;
```

Select specific columns.

```sql
SELECT first_name, last_name
FROM users;
```

Remove duplicates.

```sql
SELECT DISTINCT city
FROM users;
```

Rename columns.

```sql
SELECT first_name AS FirstName
FROM users;
```

Perform calculations.

```sql
SELECT price * quantity AS total
FROM orders;
```

---

# 2. Filtering Data (WHERE)

Comparison Operators

```sql
=
!=
<>
>
<
>=
<=
```

Examples

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

AND

```sql
WHERE age > 18
AND city = 'Manila';
```

OR

```sql
WHERE city='Manila'
OR city='Cebu';
```

NOT

```sql
WHERE NOT city='Manila';
```

BETWEEN

```sql
WHERE age BETWEEN 18 AND 30;
```

IN

```sql
WHERE department IN ('IT','HR','Finance');
```

LIKE Wildcards

```text
%  Any number of characters

_  Exactly one character
```

Examples

```sql
LIKE 'A%'
LIKE '%son'
LIKE '_a%'
LIKE '%John%'
```

NULL

```sql
WHERE email IS NULL;

WHERE email IS NOT NULL;
```

EXISTS

```sql
SELECT *
FROM customers
WHERE EXISTS (
    SELECT *
    FROM orders
    WHERE customers.id = orders.customer_id
);
```

---

# 3. Sorting & Limiting

Ascending

```sql
ORDER BY salary ASC;
```

Descending

```sql
ORDER BY salary DESC;
```

Multiple columns

```sql
ORDER BY department, salary DESC;
```

Limit

```sql
LIMIT 10;
```

Offset

```sql
LIMIT 10 OFFSET 20;
```

Equivalent

```sql
LIMIT 20,10;
```

---

# 4. Aliases

Columns

```sql
SELECT salary AS MonthlySalary
FROM employees;
```

Tables

```sql
SELECT e.name
FROM employees e;
```

---

# 5. Aggregate Functions

Count rows

```sql
COUNT(*)
```

Count non-null

```sql
COUNT(column)
```

Sum

```sql
SUM(column)
```

Average

```sql
AVG(column)
```

Maximum

```sql
MAX(column)
```

Minimum

```sql
MIN(column)
```

Example

```sql
SELECT
COUNT(*) AS Employees,
AVG(salary) AS AverageSalary,
MAX(salary) AS HighestSalary
FROM employees;
```

---

# 6. GROUP BY & HAVING

Group rows.

```sql
SELECT department,
COUNT(*)
FROM employees
GROUP BY department;
```

Filter groups.

```sql
SELECT department,
AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

Difference

WHERE filters rows.

HAVING filters grouped results.

---

# 7. String Functions

Concatenate

```sql
CONCAT(first_name,' ',last_name)
```

Uppercase

```sql
UPPER(name)
```

Lowercase

```sql
LOWER(name)
```

Length

```sql
LENGTH(name)
```

Substring

```sql
SUBSTRING(name,1,5)
```

Replace

```sql
REPLACE(name,'John','Jack')
```

Trim spaces

```sql
TRIM(name)
```

Left

```sql
LEFT(name,3)
```

Right

```sql
RIGHT(name,4)
```

Reverse

```sql
REVERSE(name)
```

Repeat

```sql
REPEAT(name,3)
```

Locate

```sql
LOCATE('a',name)
```

---

# 8. Numeric Functions

Round

```sql
ROUND(price,2)
```

Ceiling

```sql
CEIL(price)
```

Floor

```sql
FLOOR(price)
```

Absolute

```sql
ABS(value)
```

Square Root

```sql
SQRT(value)
```

Power

```sql
POWER(value,2)
```

Random

```sql
RAND()
```

Modulus

```sql
MOD(10,3)
```

---

# 9. Date & Time Functions

Current Date

```sql
CURDATE()
```

Current Time

```sql
CURTIME()
```

Current Timestamp

```sql
NOW()
```

Extract

```sql
YEAR(date)

MONTH(date)

DAY(date)

HOUR(date)
```

Difference

```sql
DATEDIFF(date1,date2)
```

Add Date

```sql
DATE_ADD(date,INTERVAL 7 DAY)
```

Subtract Date

```sql
DATE_SUB(date,INTERVAL 1 MONTH)
```

Format

```sql
DATE_FORMAT(date,'%M %d, %Y')
```

---

# 10. NULL Handling

IFNULL

```sql
IFNULL(phone,'No Phone')
```

COALESCE

Returns first non-null.

```sql
COALESCE(home_phone,mobile_phone,office_phone)
```

NULLIF

```sql
NULLIF(a,b)
```

---

# 11. Conditional Logic

CASE

```sql
SELECT name,

CASE
WHEN score>=90 THEN 'A'
WHEN score>=80 THEN 'B'
WHEN score>=70 THEN 'C'
ELSE 'F'
END AS Grade

FROM students;
```

IF()

```sql
IF(score>=60,'Pass','Fail')
```

---

# 12. Joins

## INNER JOIN

Matching rows only.

```sql
SELECT *
FROM orders
INNER JOIN customers
ON orders.customer_id=customers.id;
```

## LEFT JOIN

All rows from left table.

```sql
LEFT JOIN
```

## RIGHT JOIN

All rows from right table.

```sql
RIGHT JOIN
```

## CROSS JOIN

Every combination.

```sql
SELECT *
FROM colors
CROSS JOIN sizes;
```

## SELF JOIN

Join table to itself.

```sql
SELECT
A.name,
B.name
FROM employees A
JOIN employees B
ON A.manager_id=B.employee_id;
```

---

# 13. Set Operations

UNION

Removes duplicates.

```sql
UNION
```

UNION ALL

Keeps duplicates.

```sql
UNION ALL
```

---

# 14. Subqueries

Scalar

```sql
SELECT *
FROM employees
WHERE salary>(
SELECT AVG(salary)
FROM employees);
```

IN

```sql
WHERE id IN(
SELECT customer_id
FROM orders
);
```

EXISTS

```sql
WHERE EXISTS(...)
```

---

# 15. Common Table Expressions (CTE)

```sql
WITH HighSalary AS
(
SELECT *
FROM employees
WHERE salary>50000
)

SELECT *
FROM HighSalary;
```

Recursive CTE

```sql
WITH RECURSIVE numbers AS
(
SELECT 1

UNION ALL

SELECT n+1
FROM numbers
WHERE n<10
)

SELECT *
FROM numbers;
```

---

# 16. Window Functions

ROW_NUMBER

```sql
ROW_NUMBER()
OVER(ORDER BY salary DESC)
```

RANK

```sql
RANK()
```

DENSE_RANK

```sql
DENSE_RANK()
```

Running Total

```sql
SUM(salary)
OVER(ORDER BY hire_date)
```

Partition

```sql
AVG(salary)
OVER(PARTITION BY department)
```

---

# 17. Views

Create

```sql
CREATE VIEW employee_view AS

SELECT *
FROM employees;
```

Delete

```sql
DROP VIEW employee_view;
```

---

# 18. Indexes

Create

```sql
CREATE INDEX idx_name
ON employees(last_name);
```

Unique Index

```sql
CREATE UNIQUE INDEX idx_email
ON users(email);
```

Drop

```sql
DROP INDEX idx_name
ON employees;
```

---

# 19. Constraints

Primary Key

```sql
PRIMARY KEY
```

Foreign Key

```sql
FOREIGN KEY
```

Unique

```sql
UNIQUE
```

Check

```sql
CHECK(age>=18)
```

Default

```sql
DEFAULT 0
```

Not Null

```sql
NOT NULL
```

Auto Increment

```sql
AUTO_INCREMENT
```

---

# 20. Database Operations

Create

```sql
CREATE DATABASE company;
```

Show

```sql
SHOW DATABASES;
```

Use

```sql
USE company;
```

Delete

```sql
DROP DATABASE company;
```

---

# 21. Table Operations

Create

```sql
CREATE TABLE employees
(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
salary DECIMAL(10,2)
);
```

Rename

```sql
RENAME TABLE employees TO staff;
```

Show Tables

```sql
SHOW TABLES;
```

Describe

```sql
DESCRIBE employees;
```

Drop

```sql
DROP TABLE employees;
```

---

# 22. Data Types

Numeric

```text
INT
BIGINT
SMALLINT
TINYINT
FLOAT
DOUBLE
DECIMAL
```

String

```text
CHAR
VARCHAR
TEXT
LONGTEXT
```

Date

```text
DATE
TIME
DATETIME
TIMESTAMP
YEAR
```

Boolean

```text
BOOLEAN
BOOL
```

Binary

```text
BLOB
```

JSON

```text
JSON
```

---

# 23. INSERT

Single

```sql
INSERT INTO employees(name,salary)

VALUES('John',50000);
```

Multiple

```sql
INSERT INTO employees(name,salary)

VALUES
('John',50000),
('Jane',60000);
```

Insert From Select

```sql
INSERT INTO backup

SELECT *
FROM employees;
```

---

# 24. UPDATE

```sql
UPDATE employees

SET salary=60000

WHERE id=1;
```

Multiple columns

```sql
UPDATE employees

SET salary=60000,
department='IT'

WHERE id=1;
```

---

# 25. DELETE

Delete specific rows.

```sql
DELETE
FROM employees
WHERE id=1;
```

Delete all rows.

```sql
DELETE FROM employees;
```

---

# 26. TRUNCATE vs DELETE vs DROP

DELETE

- Removes selected rows
- Can rollback
- Keeps table

TRUNCATE

- Removes all rows
- Faster
- Resets AUTO_INCREMENT

DROP

- Deletes table completely

---

# 27. Transactions

Start

```sql
START TRANSACTION;
```

Commit

```sql
COMMIT;
```

Rollback

```sql
ROLLBACK;
```

Savepoint

```sql
SAVEPOINT save1;
```

Rollback to Savepoint

```sql
ROLLBACK TO save1;
```

---

# 28. Stored Procedures

Create

```sql
DELIMITER $$

CREATE PROCEDURE GetEmployees()

BEGIN

SELECT *
FROM employees;

END $$

DELIMITER ;
```

Execute

```sql
CALL GetEmployees();
```

Delete

```sql
DROP PROCEDURE GetEmployees;
```

---

# 29. Functions

```sql
CREATE FUNCTION SquareNumber(x INT)

RETURNS INT

RETURN x*x;
```

Call

```sql
SELECT SquareNumber(5);
```

---

# 30. Triggers

Before Insert

```sql
CREATE TRIGGER before_insert

BEFORE INSERT

ON employees

FOR EACH ROW

SET NEW.created_at=NOW();
```

Drop

```sql
DROP TRIGGER before_insert;
```

---

# 31. Events

Enable scheduler

```sql
SET GLOBAL event_scheduler=ON;
```

Create Event

```sql
CREATE EVENT cleanup

ON SCHEDULE EVERY 1 DAY

DO

DELETE FROM logs

WHERE created_at<
NOW()-INTERVAL 30 DAY;
```

---

# 32. User & Privileges

Create User

```sql
CREATE USER 'john'@'localhost'
IDENTIFIED BY 'password';
```

Grant

```sql
GRANT ALL PRIVILEGES

ON company.*

TO 'john'@'localhost';
```

Reload

```sql
FLUSH PRIVILEGES;
```

Revoke

```sql
REVOKE INSERT

ON company.*

FROM 'john'@'localhost';
```

Delete User

```sql
DROP USER 'john'@'localhost';
```

---

# 33. JSON Functions

Extract

```sql
JSON_EXTRACT(data,'$.name')
```

Shorthand

```sql
data->'$.name'
```

Unquoted

```sql
data->>'$.name'
```

Object

```sql
JSON_OBJECT('name','John','age',25)
```

Array

```sql
JSON_ARRAY(1,2,3)
```

Contains

```sql
JSON_CONTAINS(data,'"Admin"','$.roles')
```

---

# 34. Performance Tips

✔ Use indexes on frequently searched columns.

✔ Avoid SELECT *

✔ Filter early with WHERE.

✔ Use LIMIT when testing.

✔ Normalize your database.

✔ Use EXPLAIN to analyze queries.

```sql
EXPLAIN
SELECT *
FROM employees
WHERE salary>50000;
```

---

# 35. Useful Operators

Arithmetic

```text
+
-
*
/
/%
```

Comparison

```text
=
!=
<>
<
>
<=
>=
```

Logical

```text
AND
OR
NOT
```

Bitwise

```text
&
|
^
<<
>>
```

---

# 36. SQL Execution Order

Actual execution order:

```text
FROM

JOIN

ON

WHERE

GROUP BY

HAVING

SELECT

DISTINCT

ORDER BY

LIMIT
```

---

# 37. Cheat Sheet Summary

## DQL (Data Query Language)

```sql
SELECT
```

---

## DML (Data Manipulation Language)

```sql
INSERT

UPDATE

DELETE
```

---

## DDL (Data Definition Language)

```sql
CREATE

ALTER

DROP

TRUNCATE

RENAME
```

---

## DCL (Data Control Language)

```sql
GRANT

REVOKE
```

---

## TCL (Transaction Control Language)

```sql
START TRANSACTION

COMMIT

ROLLBACK

SAVEPOINT
```

---

# Most Common Interview Queries

Top 5 highest salaries

```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

Second Highest Salary

```sql
SELECT DISTINCT salary

FROM employees

ORDER BY salary DESC

LIMIT 1 OFFSET 1;
```

Duplicate Values

```sql
SELECT email,
COUNT(*)

FROM users

GROUP BY email

HAVING COUNT(*)>1;
```

Employees without Departments

```sql
SELECT *

FROM employees e

LEFT JOIN departments d

ON e.department_id=d.id

WHERE d.id IS NULL;
```

Nth Highest Salary

```sql
SELECT DISTINCT salary

FROM employees

ORDER BY salary DESC

LIMIT 1 OFFSET n-1;
```

Running Total

```sql
SELECT
salary,

SUM(salary)
OVER(ORDER BY id)

FROM employees;
```

Average Salary per Department

```sql
SELECT
department,

AVG(salary)

FROM employees

GROUP BY department;
```

---

# Quick Reference

```text
SELECT      Retrieve data
INSERT      Add data
UPDATE      Modify data
DELETE      Remove data
CREATE      Create objects
ALTER       Modify objects
DROP        Delete objects
TRUNCATE    Empty table
GRANT       Give permissions
REVOKE      Remove permissions
COMMIT      Save transaction
ROLLBACK    Undo transaction
```