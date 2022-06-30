from tkinter import *
import mysql.connector
x=mysql.connector.connect(host="localhost",user="root",passwd="13579ASCII_20",database="visual")
y=x.cursor()
teacherpage=Tk()
teacherpage.geometry('800x800')
def class1():
    global classname
    classname="class1"
    teacherpage.destroy()
    overview(classname)
def class2():
    global classname
    classname="class2"
    teacherpage.destroy()
    overview(classname)
def class3():
    global classname
    classname="class3"
    teacherpage.destroy()
    overview(classname)
def class4():
    global classname
    classname="class4"
    teacherpage.destroy()
    overview(classname)
def class5():
    global classname
    classname="class5"
    teacherpage.destroy()
    overview(classname)
def class6():
    global classname
    classname="class6"
    teacherpage.destroy()
    overview(classname)
def class7():
    global classname
    classname="class7"
    teacherpage.destroy()
    overview(classname)
def class8():
    global classname
    classname="class8"
    teacherpage.destroy()
    overview(classname)
def class9():
    global classname
    classname="class9"
    teacherpage.destroy()
    overview(classname)
def class10():
    global classname
    classname="class10"
    teacherpage.destroy()
    overview(classname)
def class11():
    global classname
    classname="class11"
    teacherpage.destroy()
    overview(classname)
def class12():
    global classname
    classname="class12"
    teacherpage.destroy()
    overview(classname)

def display():
    l=[]
    t=("rno","name","caste","genter","pt1","pt2","pt3","pt4","annual exam")
    l.append(t)
    window=Tk()
    window.geometry('800x800')
    y.execute("select * from {}".format(classname))                            #the displaying function
    for i in y.fetchall():
        l.append(i)
    total_row=len(l)
    total_column=len(l[0])
    for i in range(total_row):
        for j in range(total_column):
            e=Entry(window,width=5,fg="blue",font=('Arial',16,'bold'))
            e.grid(row=i,column=j)
            e.insert(0,l[i][j])
    window.mainloop()
def add():
    def entry():
        
        y.execute("insert into {} values({},'{}','{}','{}',{},{},{},{},{})".format(classname,entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()))
        x.commit()
    window=Tk()
    window.geometry('800x800')
    rno=Label(window,text="RNO").grid(row=0,column=0)
    Name=Label(window,text="Name").grid(row=1,column=0)
    Caste=Label(window,text="CASTE").grid(row=2,column=0)
    Gender=Label(window,text="GENDER").grid(row=3,column=0)
    pt1=Label(window,text="PT1").grid(row=4,column=0)
    pt2=Label(window,text="PT2").grid(row=5,column=0)
    pt3=Label(window,text="PT3").grid(row=6,column=0)
    pt4=Label(window,text="PT4").grid(row=7,column=0)
    annualexam=Label(window,text="ANNUALEXAM").grid(row=8,column=0)                                                  # the adding functiom
    entry1=Entry(window, bd =5)
    entry2=Entry(window, bd =5)
    entry3=Entry(window, bd =5)
    entry4=Entry(window, bd =5)
    entry5=Entry(window, bd =5)
    entry6=Entry(window, bd =5)
    entry7=Entry(window, bd =5)
    entry8=Entry(window, bd =5)
    entry9=Entry(window, bd =5)
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)
    entry3.grid(row=2,column=1)
    entry4.grid(row=3,column=1)
    entry5.grid(row=4,column=1)
    entry6.grid(row=5,column=1)
    entry7.grid(row=6,column=1)
    entry8.grid(row=7,column=1)
    entry9.grid(row=8,column=1)
  
    submit=Button(window,text="submit",command=entry).grid(row=9,column=0)
    def backp():                                                               #back
        window.destroy()
    back=Button(window,text="BACK",command=backp).grid(row=9,column=1)
    window.mainloop()
def modify():
    def search():
        y.execute("update {} set {}={} where name='{}' and rno={} ".format(classname,entry4.get(),entry5.get(),entry2.get(),entry1.get()))
    window=Tk()
    window.geometry('800x800')
    header=Label(window,text="ENTER EITHER THE RNO , NAME AND CLASS TO SEARCH STUDENT")
    rno=Label(window,text="RNO").grid(row=0,column=0)                                                  #modify
    entry1=Entry(window, bd =5)
    name=Label(window,text="NAME").grid(row=1,column=0)
    entry2=Entry(window, bd =5)
    what1=Label(window,text="Enter the which want to update ").grid(row=2,column=0)
    entry4=Entry(window, bd =5)
    set=Label(window,text="SET VALUE").grid(row=3,column=0)
    entry5=Entry(window, bd =5)
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)
    entry4.grid(row=2,column=1)
    entry5.grid(row=3,column=1)
    
    def backp():                                                               #back
        window.destroy()
    back=Button(window,text="BACK",command=backp).grid(row=5,column=1)
    search=Button(window,text="UPDATE",command=search).grid(row=5,column=2)
def delet():
    def delete():
        y.execute("delete from {} where rno={} and name='{}' ".format(classname,entry1.get(),entry2.get()))
    window=Tk()
    window.geometry('800x800')                                                                 #delete the data
    header=Label(window,text="ENTER THE RNO AND NAME OF THE STUDENT").grid(row=0,column=4)
    rno=Label(window,text="enter the rno").grid(row=0,column=0)
    entry1=Entry(window, bd =5)
    name=Label(window,text="NAME").grid(row=1,column=0)
    entry2=Entry(window, bd =5)
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)
    def backp():                                                               #back
        window.destroy()
    back=Button(window,text="BACK",command=backp).grid(row=5,column=1)
    DELETE2=Button(window,text="DELETE",command=delete).grid(row=5,column=2)
def reset():
     y.execute("delete from {}" ).format(classname)
def overview(classname):
    window=Tk()
    window.geometry('800x800')
    but1=Button(window,text="DISPLAY",width=20,height=3,command=display).pack()
    but2=Button(window,text="INSERT",width=20,height=3,command=add).pack()
    but3=Button(window,text="MODIFY",width=20,height=3,command=modify).pack()
    but4=Button(window,text="DELETE",width=20,height=3,command=delet).pack()                             #all buttons code
    but6=Button(window,text="RESET",width=20,height=3,command=reset).pack()
    window.mainloop()
label=Label(teacherpage,text="WHICH CLASS ARE YOU").pack()
but1=Button(teacherpage,text="CLASS1",width=20,height=3,command=class1).pack()
but2=Button(teacherpage,text="CLASS2",width=20,height=3,command=class2).pack()
but3=Button(teacherpage,text="CLASS3",width=20,height=3,command=class3).pack()
but4=Button(teacherpage,text="CLASS4",width=20,height=3,command=class4).pack()
but5=Button(teacherpage,text="CLASS5",width=20,height=3,command=class5).pack()
but6=Button(teacherpage,text="CLASS6",width=20,height=3,command=class6).pack()
but7=Button(teacherpage,text="CLASS7",width=20,height=3,command=class7).pack()
but8=Button(teacherpage,text="CLASS8",width=20,height=3,command=class8).pack()
but9=Button(teacherpage,text="CLASS9",width=20,height=3,command=class9).pack()
but10=Button(teacherpage,text="CLASS10",width=20,height=3,command=class10).pack()
but11=Button(teacherpage,text="CLASS11",width=20,height=3,command=class11).pack()
but12=Button(teacherpage,text="CLASS12",width=20,height=3,command=class12).pack()
teacherpage.mainloop()    
