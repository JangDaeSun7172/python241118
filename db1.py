import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(r'C:\work\sample.db')

cur = conn.cursor()

# 테이블 생성(테이블 스키마 - 구조)
cur.execute("create table if not exists phonebook (name text, phone text);")
cur.execute("insert into phonebook values ('홍길동', '010-1234-5678');")
name = '이순신'
phone = '010-1234-5679'
cur.execute("insert into phonebook values (?, ?);", (name, phone))
datalist = [('강감찬', '010-1234-5680'), ('김유신', '010-1234-5681')]
cur.executemany("insert into phonebook values (?, ?);", datalist)
cur.execute("select * from phonebook;")

# for row in cur:
#     #print(row)
#     print(row[0], row[1])

# print('fetchone()')
# print(cur.fetchone())
# print('fetchmany(2)')
# print(cur.fetchmany(2))
# print('fetchall()')
# cur.execute("select * from phonebook;")
print(cur.fetchall())

conn.commit()

conn.close()
