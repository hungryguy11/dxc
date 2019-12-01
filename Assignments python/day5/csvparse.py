import csv
import pymysql
reader = csv.reader(open('C:\\Users\\croy20\\Documents\\Python\\DXCtraing\\Examples\\11SampleModules\\csvDemo\\demo.csv','r'),delimiter=',')
print(reader)
for data in reader:
    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # data = cursor.execute("Select * from user")
    # data = cursor.execute('''CREATE TABLE User(FNAME CHAR(20) NOT NULL, LNAME CHAR(20) )''')
    s = data[0]
    t = data[1]
    data = cursor.execute('''INSERT INTO User (FNAME,LNAME) VALUES ('{0}','{1}')'''.format(s, t))
    db.commit()
    resp = cursor.fetchall()
    print(resp)
    db.close()