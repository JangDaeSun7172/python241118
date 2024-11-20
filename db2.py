import sqlite3

conn = sqlite3.connect(r'C:\work\sample1.db')

cur = conn.cursor()

cur.execute("select * from employee;")

print(cur.fetchall())

conn.commit()

conn.close()
