SELECT company, COUNT(bar_id) AS count
    FROM Chocolate
GROUP BY company
ORDER BY count DESC;

--Çàïèò 2. Âèâåñòè êîë³ð òà % ä³àìàíò³â ç òàêèì êîëüîðîì.

SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Chocolate,
    (SELECT COUNT(bar_name) AS count
FROM Chocolate)t   
GROUP BY  company,
     t.count; 
       
--Çàïèò 3. Äèíàì³êà çàëåæíîñò³ ïðîçîðîñò³ ä³àìàíòó â³ä ê³ëüêîñò³ ä³àìàíò³â, ÿê³ ìàþòü òàêó ïðîçîð³ñòü.

SELECT Bean.bean_type,
    COUNT(Chocolate.bar_id) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC
