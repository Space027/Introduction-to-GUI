from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox

sc=Tk()
sc.geometry('450x500')
sc.title('Address Book')

dicton={}

lbox=Listbox(sc,width=30,height=20)
lbox.grid(row=1,column=0,rowspan=5,padx=10,columnspan=2)

def lboxadd():
    keys=dicton.keys()
    lbox.delete(0,END)
    for key in keys:
        lbox.insert(END,key)

title=Label(sc,text='My Address Book:',font=('Times New Roman',15))
title.grid(row=0,column=0,columnspan=2)
nam=Label(sc,text='Name:')
nam.grid(row=1,column=2,padx=10)
add=Label(sc,text='Address:')
add.grid(row=2,column=2,pady=10)
mob=Label(sc,text='Mobile:')
mob.grid(row=3,column=2)
ema=Label(sc,text='Email:')
ema.grid(row=4,column=2,pady=10)
bir=Label(sc,text='Birthday:')
bir.grid(row=5,column=2)

nament=Entry(sc)
nament.grid(row=1,column=3)
addent=Entry(sc)
addent.grid(row=2,column=3)
mobent=Entry(sc)
mobent.grid(row=3,column=3)
emaent=Entry(sc)
emaent.grid(row=4,column=3)
birent=Entry(sc)
birent.grid(row=5,column=3)

def openfile():
    opefil=askopenfile(title='Open File')

def adding():
    n=nament.get()
    a=addent.get()
    m=mobent.get()
    e=emaent.get()
    b=birent.get()    
    global dicton
    dicton[n]=[a,m,e,b]
    lboxadd()
    nament.delete(0,END)
    addent.delete(0,END)
    mobent.delete(0,END)
    emaent.delete(0,END)
    birent.delete(0,END)

def show():
    ind=lbox.curselection()
    text=lbox.get(ind)
    tex=dicton[text]
    print(tex)
    tkinter.messagebox.showinfo(text,'Address: '+tex[0]+'\n'+'Mobile: '+tex[1]+'\n'+'Email: '+tex[2]+'\n'+'Birthday: '+tex[3])

op=Button(sc,text='Open', bg='yellow',command=openfile)
op.grid(row=0,column=2,padx=20)
sh=Button(sc,text='Show',bg='yellow',command=show)
sh.grid(row=6,column=2,padx=20)
ed=Button(sc,text='Edit',bg='yellow')
ed.grid(row=6,column=0)
de=Button(sc,text='Delete',bg='yellow')
de.grid(row=6,column=1)
ad=Button(sc,text='Add/Update',bg='yellow',command=adding)
ad.grid(row=6,column=3)
sa=Button(sc,text='Save',width=40,bg='light green')
sa.grid(row=7,column=0,columnspan=4,pady=15)

sc.mainloop()