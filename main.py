import cx_Oracle

conn = cx_Oracle.connect("SYS","B8KF4tdlXXi5cYNGTXUx","lockalhost/orcl")
cur = conn.cursor()

cur.execute('''
SELECT company, COUNT(bar_id) AS count
    FROM Chocolate
GROUP BY company
ORDER BY count DESC;
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
    COUNT(Chocolate.bar_id) AS count
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
