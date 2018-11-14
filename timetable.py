import json,re, sqlite3

fname='data.json'
data=open(fname).read()
js=json.loads(data)

conn=sqlite3.connect("table.sqlite")
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Groups;
DROP TABLE IF EXISTS ClassRoom;
DROP TABLE IF EXISTS WeekDay;
DROP TABLE IF EXISTS Hour;
DROP TABLE IF EXISTS Deal;

CREATE TABLE Faculty (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT,
course_id INTEGER
);

CREATE TABLE Course (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT,
abbr TEXT,
type TEXT,
length INTEGER
);

CREATE TABLE Groups (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT ,
type TEXT ,
capacity INTEGER
);

CREATE TABLE ClassRoom (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT ,
type TEXT ,
capacity INTEGER
);

CREATE TABLE WeekDay (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT UNIQUE,
hours_id INTEGER ,
full INTEGER
);

CREATE TABLE Hour (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE Deal (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT  UNIQUE,
faculty_id INTEGER,
course_id INTEGER,
group_id INTEGER,
week_day_id INTEGER,
hours_id INTEGER,
busy INTEGER
);

''')

faculty=[[0],[0],[0],[0],[0]]
groups=[[0],[0],[0],[0],[0]]
classrooms=[[0],[0],[0],[0],[0]]

for person in js["faculty"]:
    cur.execute('''INSERT INTO  Faculty(name) VALUES (?)''',(person,))
    conn.commit()



for course in js["courses"]:
    name=course["name"]
    abbr=course["abbr"]
    typeOf=course["type"]
    length=course["length"]

    cur.execute('''INSERT INTO  Course(name,abbr,type,length) VALUES (?,?,?,?)''',(name,abbr,typeOf,length))
    conn.commit()


for group in js["groups"]:
    name=group["name"]
    capacity=group["capacity"]
    typeOf=group["type"]
    try:
        cur.execute('''INSERT  INTO  Groups (name,capacity,type) VALUES (?,?,?)''',(name,capacity,typeOf))
        conn.commit()
    except:
        pass

for class_room in js["class_rooms"]:
    name=class_room["name"]
    capacity=class_room["capacity"]
    typeOf=class_room["type"]
    try:
        cur.execute('''INSERT  INTO  ClassRoom(name,capacity,type) VALUES (?,?,?)''',(name,capacity,typeOf))
        conn.commit()
    except:
        pass

for day in js["week_day"]:
    try:
        cur.execute('''INSERT OR IGNORE INTO  WeekDay(name) VALUES (?)''',(day,))
        conn.commit()
    except:
        pass

for hourX in js["hours"]:
    try:
        cur.execute('''INSERT OR IGNORE INTO  Hour(name) VALUES (?)''',(hourX,))
        conn.commit()
    except:
        pass

cur.execute('''SELECT id FROM Course''')
course_ids=cur.fetchall()
cur.execute('''SELECT id FROM Faculty''')
faculty_ids=cur.fetchall()
print("Courses:")
for i in range(len(course_ids)): print(course_ids[i+2])
print("Faculty:",faculty_ids)
# cur.execute('''UPDATE  Faculty SET course_id=? WHERE id=?''',(course_ids+2,faculty_ids))

# flag=cur.fetchone()
# while (flag==0 or !flag):


cur.close()
