import sqlite3 as q

conn = q.connect('src/db/dados.db')
c = conn.cursor()

print(c.execute('SELECT * FROM DADOS').fetchall()[0])

