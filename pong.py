from tkinter import *

sc=Tk()
sc.geometry('600x600')
sc.title('Pong')

ca=Canvas(sc,width=600,height=600,bg='black')
ca.grid(row=0,column=0)
ca.create_line(300,0,300,600,width=10,fill='white')
ca.create_oval(200,200,400,400,outline='white')

sc.mainloop()