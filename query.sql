SELECT ROUND(AVG(rating),3) AS rating
, TRIM(company) AS company
FROM Chocolate
INNER JOIN Сompany
ON Chocolate.company= Сompany.company 
GROUP BY Сompany
ORDER BY  rating DESC;

--Запит 2. Вивести колір та % діамантів з таким кольором.

SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Chocolate,
    (SELECT COUNT(bar_name) AS count
FROM Chocolate)t   
GROUP BY  company,
     t.count; 
       
--Запит 3. Динаміка залежності прозорості діаманту від кількості діамантів, які мають таку прозорість.

SELECT Bean.bean_type,
    COUNT(Chocolate.diamond_index) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC;