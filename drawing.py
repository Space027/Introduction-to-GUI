from tkinter import *

sc=Tk()
sc.geometry('600x500')
sc.title('Canvas')
sc.config(bg='light gray')

size=3
colour=('')

b1=Button(sc,text='Pen')
b2=Button(sc,text='Brush')
b3=Button(sc,text='Colour')
b4=Button(sc,text='Rubber')
sli=Scale(sc,from_=0,to_=10,orient=HORIZONTAL)
b1.grid(row=0,column=1,pady=15)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)
b4.grid(row=0,column=4)
sli.grid(row=0,column=5)

ca=Canvas(sc,width=600,height=500)   
ca.grid(row=1,column=0,columnspan=7)

sc.mainloop()

