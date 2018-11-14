import sqlite3

conn=sqlite3.connect("Ages.sqlite")
cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Ages(name VARCHAR(128), age INTEGER)''')

cur.execute('''DELETE FROM Ages''');
cur.execute('''INSERT INTO Ages (name, age) VALUES ("Marta", 25)''');
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Rhuairidh', 14)''');
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Kelice', 17)''');
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Finnan', 27)''');
 
cur.execute('''SELECT hex(name||age) AS X FROM Ages ORDER BY X''')

row=cur.fetchone()[0]
print(row)
