-- Реализовать следующий SQL-запрос: соединить данные двух таблиц так,
-- чтобы данные пересекались по криттерию Cat и Catnumb.  (Выполнить все JOIN)


SELECT * FROM table1 INNER JOIN table2 ON table1.cat = table2.catnumb;
-- INNER JOIN

SELECT * FROM table1 LEFT JOIN table2 ON table1.cat = table2.catnumb;
-- LEFT JOIN
SELECT * FROM table1 LEFT JOIN table2 ON table1.cat = table2.catnumb WHERE table2.catnumb IS NULL;
-- LEFT JOIN ... WHERE ...

SELECT * FROM table1 RIGHT JOIN table2 ON table1.cat = table2.catnumb;
-- RIGHT JOIN
SELECT * FROM table1 RIGHT JOIN table2 ON table1.cat = table2.catnumb WHERE table1.cat IS NULL;
-- RIGHT JOIN ... WHERE ...

SELECT * FROM table1 LEFT JOIN table2 ON table1.cat = table2.catnumb
UNION
SELECT * FROM table1 RIGHT JOIN table2 ON table1.cat = table2.catnumb;
-- FULL OUTER JOIN

SELECT * FROM table1 LEFT JOIN table2 ON table1.cat = table2.catnumb WHERE table2.catnumb IS NULL
UNION
SELECT * FROM table1 RIGHT JOIN table2 ON table1.cat = table2.catnumb WHERE table1.cat IS NULL;
-- FULL OUTER JOIN ... WHERE ...