import cx_Oracle

import chart_studio
chart_studio.tools.set_credentials_file(username='Evelinabodnar', api_key='S6Cu2THhk1VIBPXEKZVf')
conn = cx_Oracle.connect("SYS","B8KF4tdlXXi5cYNGTXUx","lockalhost/orcl")
cur = conn.cursor()

cur.execute('''
SELECT company, COUNT(bar_id) AS count
    FROM Chocolate
GROUP BY company
ORDER BY count DESC
''')
rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)

import plotly.graph_objects as go
import chart_studio.plotly as py
bar = [go.Bar(x=y, y=x)]
layout = go.Layout(
    title='Rating of different chocolates',
    xaxis=dict(
        title='Chocolate',
        titlefont=dict(
            family='Courier New, monospace',
            size=16,
            color='#7f7f70'
        )
    ),
    yaxis=dict(
        title='Rating per chocolate',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=16,
            color='#7f7f70'
        )
    )
)
fig = go.Figure(data=bar, layout=layout)


bar_rating_url=py.plot(fig,filename='Rating of different chocolates', auto_open=False)

cur.execute('''
SELECT company, ROUND(COUNT(bar_name)*100/t.count, 2) AS persent
FROM Chocolate,
    (SELECT COUNT(bar_name) AS count
FROM Chocolate)t   
GROUP BY  company,
     t.count
''')


rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)
pie = go.Figure(data=[go.Pie(labels=y, values=x )])
pie_choc_url=py.plot(pie, filename='percentage of chocolate company ',auto_open=False)

cur.execute('''   SELECT Bean.bean_type,
    COUNT(Chocolate.bean_type) AS count
    FROM Chocolate 
    INNER JOIN Bean ON Chocolate.bean_type = Bean.bean_type
GROUP BY Bean.bean_type
ORDER BY count DESC
''')

rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)

scatter = go.Figure([go.Scatter(x=y, y=x)])

scatter_beans_url=py.plot(scatter, filename = '
dependence on the type of beans on the percentage of chocolate, auto_open=False)

import re
import chart_studio.dashboard_objs as dashboard
def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

my_dboard = dashboard.Dashboard()
bar_rating= fileId_from_url(bar_rating_url)
pie_choc= fileId_from_url(pie_choc_url)
scatter_beans= fileId_from_url(scatter_beans_url)



box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':bar_rating,
    'title': 'Company and quantity of chocolatess'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':pie_choc,
    'title': 'percentage of chocolate company '
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':scatter_beans ,
    'title': 'dependence on the type of beans on the percentage of chocolate'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'db_Evelina')

conn.commit()
cur.close()
conn.close()
