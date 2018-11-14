import sqlite3
import re

conn=sqlite3.connect("counts.sqlite")
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER) ''')

fname=input('Enter location: ')
if (len(fname)<1): fname="mbox-short.txt"
fh=open(fname)
for line in fh:
    line.strip()
    if not line.startswith('From: '): continue
    piece=line.split()
    email=piece[1]
    org=re.findall( "@(.+)" , email)
    org="".join(org)
    print(org)
    cur.execute('SELECT count FROM Counts WHERE org=?', (org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE org= ?', (org,))

    conn.commit()

cur.execute('''SELECT org, count FROM Counts ORDER BY count DESC''')
row = cur.fetchone()
maximum=tuple()
maximum=row
print(str(maximum))
