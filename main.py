import cx_Oracle

conn = cx_Oracle.connect("SYS","B8KF4tdlXXi5cYNGTXUx","lockalhost/orcl")
cur = conn.cursor()

cur.execute('''
SELECT ROUND(AVG(rating),3) AS rating
, TRIM(company) AS company
FROM Chocolate
INNER JOIN Company
ON Chocolate.company= Company.company 
GROUP BY Company
ORDER BY  rating DESC;
''')

rows = cur.fetchall()
print(rows)

cur.execute('''
SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Chocolate,
    (SELECT COUNT(bar_name) AS count
FROM Chocolate)t   
GROUP BY  company,
     t.count; 
''')

rows = cur.fetchall()
print(rows)

cur.execute('''   SELECT Bean.bean_type,
    COUNT(Chocolate.diamond_index) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC;
''')

rows = cur.fetchall()
print(rows)
conn.commit()
cur.close()
conn.close()
