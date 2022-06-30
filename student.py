from tkinter import *
window=Tk()
window.geometry('800x800')
import mysql.connector
x=mysql.connector.connect(host="localhost",user="root",passwd="13579ASCII_20",database="visual")
y=x.cursor()
rno=Label(window,text="RNO").grid(row=0,column=0)
Name=Label(window,text="Name").grid(row=1,column=0)
Class=Label(window,text="CLASS").grid(row=2,column=0)
entry1=Entry(window, bd =5)
entry2=Entry(window, bd =5)
entry3=Entry(window, bd =5)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
def backp():                                                               #back
    window.destroy()
    import main
def search():
    window=Tk()
    window.geometry('800x800')
    l=[]
    y.execute("select * from {} where name='{}' and rno={}".format(entry3.get(),entry2.get(),entry1.get()))
    for i in y.fetchall():
        l.append(i)
    print(l)
    total_row=len(l)
    total_column=len(l[0])
    for i in range(total_row):
        for j in range(total_column):
            e=Entry(window,width=5,fg="blue",font=('Arial',16,'bold'))
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
    window.mainloop()
back=Button(window,text="BACK",command=backp).grid(row=3,column=0)
search=Button(window,text="SEARCH",command=search).grid(row=3,column=1)
window.mainloop()