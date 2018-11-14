import json
import sqlite3

conn=sqlite3.connect("try.sqlite")
cur=conn.cursor()

cur.executescript('''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;


CREATE TABLE User (
id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE Course (
id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT  UNIQUE,
title TEXT UNIQUE
);

CREATE TABLE Member (
user_id INTEGER,
course_id INTEGER,
role INTEGER ,
PRIMARY KEY (user_id, course_id)
);

''')

filename=input("Enter the file name: ")
if (len(filename)<1): filename="roster_data.json"
data=open(filename).read()
jsdata=json.loads(data)

datax=list()

for piece in jsdata:
    name=piece[0]
    title=piece[1]
    role=piece[2]
    print(name, title)
    #print('Inserting... ')
    cur.execute('''INSERT OR IGNORE INTO User(name) VALUES (?)  ''', (name,))
    cur.execute('''SELECT id FROM User WHERE name= ?  ''', (name,))
    user_id=cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES (?)  ''', (title,))
    cur.execute('''SELECT id FROM Course WHERE title= ?  ''', (title,))
    course_id=cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member(user_id, course_id) VALUES (?,?) ''', (user_id, course_id))

    # cur.execute('''SELECT user_id FROM Member WHERE course_id=?''', (course_id,))
    # member_user_id=cur.fetchone()[0]
    #
    # cur.execute('''SELECT course_id FROM Member WHERE user_id=?''', (user_id,))
    # member_course_id=cur.fetchone()[0]

    cur.execute('''UPDATE Member SET role=? WHERE user_id=? AND course_id=?''',(role,user_id,course_id))
    cur.executescript('''
    SELECT hex(User.name || Course.title || Member.role ) AS X FROM
       User JOIN Member JOIN Course
       ON User.id = Member.user_id AND Member.course_id = Course.id
       ORDER BY X
    ''')

    print(cur.fetchone())

conn.commit()
cur.close()
