CREATE DATABASE IF NOT EXISTS hackerrank_practice;

DROP TABLE IF EXISTS hackerrank_practice.CITY;

CREATE TABLE hackerrank_practice.CITY (
    ID INT,
    NAME VARCHAR(17),
    COUNTRYCODE VARCHAR(3),
    DISTRICT VARCHAR(20),
    POPULATION INT
);

INSERT INTO hackerrank_practice.CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION)
VALUES 
    (1, 'Los Angeles', 'USA', 'California', 3900000),
    (2, 'New York', 'USA', 'New York', 8400000),
    (3, 'Tokyo', 'JPN', 'Tokyo', 13960000),
    (4, 'Smallville', 'USA', 'Kansas', 45000);

-- Your actual solution query!
SELECT * FROM CITY