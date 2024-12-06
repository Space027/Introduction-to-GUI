from tkinter import *
import random

sc=Tk()
sc.geometry('400x400')
sc.title('Noughts and Crosses')

b1=Button(sc,width=10,height=10)
b2=Button(sc,width=10,height=10)
b3=Button(sc,width=10,height=10)
b4=Button(sc,width=10,height=10)
b5=Button(sc,width=10,height=10)
b6=Button(sc,width=10,height=10)
b7=Button(sc,width=10,height=10)
b8=Button(sc,width=10,height=10)
b9=Button(sc,width=10,height=10)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

sc.mainloop()