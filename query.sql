SELECT company, COUNT(bar_id) AS count
    FROM Chocolate
GROUP BY company
ORDER BY count DESC;


SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Chocolate,
    (SELECT COUNT(bar_name) AS count
FROM Chocolate)t   
GROUP BY  company,
     t.count; 


SELECT Bean.bean_type,
    COUNT(Chocolate.bar_id) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC
