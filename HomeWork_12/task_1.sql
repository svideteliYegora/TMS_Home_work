CREATE DATABASE homework_12;

USE homework_12;

CREATE TABLE pc (
code int,
model varchar(50),
speed smallint,
ram smallint,
hd real,
cd varchar(50),
price float
);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (0001, "Lenovo 80xl", 2.2, 2, 900, "12x", 400);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (0002, "Asus 78lx", 3.0, 4, 1500, "15x", 700);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (0003, "Dell 90dx", 3.5, 16, 2000, "18x", 1000);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (0004, "HP 78vs", 1.7, 2, 1000, "12x", 350);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (0005, "Lenovo 87lv", 2.8, 8, 1000, "18x", 600);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (0006, "Lenovo 12mx", 3.2, 14, 2000, "24x", 800);

SELECT * FROM pc WHERE price < 400;

SELECT model, speed, hd FROM pc WHERE ram <= 16 AND ram >= 8;

SELECT price FROM pc WHERE hd < 1000;

UPDATE pc SET price = price * 2 WHERE price > 400;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM pc WHERE code = 0001;

SELECT * FROM pc;
