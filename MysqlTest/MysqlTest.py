import pymysql

conn = pymysql.connect(
    host="localhost",
    user='root',
    port=3306,
    password="",
    database="spider",
    charset="utf8"
)

cur = conn.cursor()
sql = "insert into game(name,type,date) values ('小蜜蜂','益智','2004-01-06')"
i = cur.execute(sql)

print(i)

conn.commit()

cur.close()
conn.close()