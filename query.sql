SELECT ROUND(AVG(rating),3) AS rating
, TRIM(company) AS company
FROM Chocolate
INNER JOIN �ompany
ON Chocolate.company= �ompany.company 
GROUP BY �ompany
ORDER BY  rating DESC;

--����� 2. ������� ���� �� % ������� � ����� ��������.

SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Chocolate,
    (SELECT COUNT(bar_name) AS count
FROM Chocolate)t   
GROUP BY  company,
     t.count; 
       
--����� 3. ������� ��������� ��������� ������� �� ������� �������, �� ����� ���� ���������.

SELECT Bean.bean_type,
    COUNT(Chocolate.diamond_index) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC;