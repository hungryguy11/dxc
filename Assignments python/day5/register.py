from tkinter import *
import pymysql


def sel():
    data = ["Python", "Angular", "Java"]
    res = ""
    i = 0
    for l in li:
        if l.get():
            res += data[i]
        i += 1

    print(fn.get())
    print(passw.get())
    if var.get() == 1:
        print("M")
    else:
        print("F")
    print(res)
    db = pymysql.connect("localhost", "root", "", "Employee")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    # data = cursor.execute("Select * from user")
    # data = cursor.execute(
    #     '''CREATE TABLE FORM(FNAME CHAR(20) NOT NULL, PASSWORD CHAR(20), GENDER CHAR(2), CHECKBOX CHAR(100) )''')

    name = fn.get()
    password = passw.get()
    gender = var.get()

    data = cursor.execute(
        '''INSERT INTO FORM (FNAME,PASSWORD,GENDER,CHECKBOX) VALUES('{0}','{1}','{2}','{3}')'''.format(name, password, gender, res))
    db.commit()


db = pymysql.connect("localhost", "root", "", "Employee")
tkit = Tk()
fn = StringVar()
L1 = Entry(tkit, text="First Name", textvariable=fn)
L1.pack(side=TOP)
passw = StringVar()
L2 = Entry(tkit, text="password", textvariable=passw)
L2.pack(side=TOP)

var = IntVar()
R1 = Radiobutton(tkit, text="Male", variable=var, value=1,
                 )
R1.pack()
R2 = Radiobutton(tkit, text="Female", variable=var, value=2
                 )
R2.pack()

li = [IntVar(), IntVar(), IntVar()]
label = Label(tkit)

C1 = Checkbutton(tkit, text="Python", variable=li[0],
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C2 = Checkbutton(tkit, text="Angular", variable=li[1],
                 onvalue=1, offvalue=0, height=5,
                 width=5)
C3 = Checkbutton(tkit, text="React", variable=li[2],
                 onvalue=1, offvalue=0, height=5,
                 width=5)
C1.pack()
C2.pack()
C3.pack()
E1 = Button(tkit, bd=5, text='Submit', command=sel)
E1.pack(side=BOTTOM)

label.pack()

tkit.mainloop()

db.close()
