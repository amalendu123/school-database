from tkinter import *
window=Tk()
window.geometry('800x800')
import mysql.connector
x=mysql.connector.connect(host="localhost",user="root",passwd="13579ASCII_20",database="visual")
y=x.cursor()
def clear():
    y.execute("DROP TABLE class1")
    y.execute("DROP TABLE class2")
    y.execute("DROP TABLE class3")
    y.execute("DROP TABLE class4")
    y.execute("DROP TABLE class5")
    y.execute("DROP TABLE class6")
    y.execute("DROP TABLE class7")
    y.execute("DROP TABLE class8")
    y.execute("DROP TABLE class9")
    y.execute("DROP TABLE class10")
    y.execute("DROP TABLE class11")
    y.execute("DROP TABLE class12")
def create():
    y.execute("create table class1(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class2(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class3(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class4(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class5(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class6(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class7(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class8(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class9(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class10(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class11(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    y.execute("create table class12(rno int,name varchar(20),caste varchar(5),gender varchar(10),pt1 int,pt2 int,pt3 int,pt4 int, annualexam int)")
    

def nextpage():
    window.destroy()
    import teacher
def nextpage1():
    window.destroy()
    import student
    

label=Label(window,text="Welcome to School database ARE you?").pack()
but=Button(window,text="TEACHER",width=20,height=10,command=nextpage)
but1=Button(window,text="STUDENT",width=20,height=10,command=nextpage1)
cl=Button(window,text="CLEAR ALL DATA",command=clear).pack()
stru=Button(window,text="CREATE",command=create).pack()
but.pack()
but1.pack()
window.mainloop()