from tkinter import *

sc=Tk()
sc.geometry('400x350')
sc.title('colour picker')

def insert():
    sc.configure(bg=ent.get())
    entry=ent.get()
    lbox.insert(END,entry)
    ent.delete(0,END)

def select():
    col=lbox.curselection()
    sc.configure(bg=lbox.get(col))



lbox=Listbox(sc,width=60,selectmode=SINGLE)
lbox.grid(row=3,column=0,pady=10,columnspan=3)

ent=Entry(sc,width=37)
ent.grid(row=1,column=0,padx=10,pady=10,columnspan=2)

ad=Button(sc,text='ADD',bg='black',fg='white',width=16,command=insert)
ad.grid(row=1,column=2)
bgchange=Button(sc,text='change backround',command=select)
bgchange.grid(row=2,column=1)

lists=['red','yellow','green','purple','blue']

for i in lists:
    lbox.insert(END,i)

sc.mainloop()
