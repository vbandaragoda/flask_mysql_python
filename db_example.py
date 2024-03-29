import mysql.connector
from collections import namedtuple

Student = namedtuple("Student"," id name dob grade address parent_name")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql_python"
)

cur = mydb.cursor()
sql = "INSERT INTO student (name,dob,grade,address,parent_name) VALUES(%s,%s,%s,%s,%s)"
values = ("Namal", '2010-10-21', 6, "Colombo 4", "ABC")
cur.execute(sql, values)
mydb.commit()
result = cur.fetchall()
print(result)

sql = "SELECT * FROM student"
cur.execute(sql)
result = cur.fetchall()
for re in result:
    st = Student(*re)
    print(st)
    print(st.name)