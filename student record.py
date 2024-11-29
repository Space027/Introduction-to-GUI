from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox

sc=Tk()
sc.geometry('600x500')
sc.title('Student Record')
sc.configure(bg='green')

dicton={}



def lboxadd():
    keys=dicton.keys()
    lbox.delete(0,END)
    for key in keys:
        lbox.insert(END,key)

title=Label(sc,text='Student Record:',font=('Times New Roman',15),bg='green')
title.grid(row=0,column=0,columnspan=2)
nam=Label(sc,text='Name:')
nam.grid(row=1,column=0,padx=10)
num=Label(sc,text='Number:')
num.grid(row=1,column=2,pady=10)
sc=Label(sc,text='Science Mark:')
sc.grid(row=2,column=0)
ema=Label(sc,text='Maths Mark:')
ema.grid(row=2,column=2,pady=10)
bir=Label(sc,text='Percentage:')
bir.grid(row=3,column=0)

nament=Entry(sc)
nament.grid(row=1,column=1)
addent=Entry(sc)
addent.grid(row=1,column=3)
mobent=Entry(sc)
mobent.grid(row=2,column=1)
emaent=Entry(sc)
emaent.grid(row=2,column=3)
birent=Entry(sc)
birent.grid(row=3,column=1,pady=10)

def openfile():
    global dicton
    opefil=askopenfile(title='Open File')
    if opefil!=None:
        dicton=eval(opefil.read())
        lboxadd()


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
    tkinter.messagebox.showinfo(text,'Number: '+tex[0]+'\n'+'Science Mark: '+tex[1]+'\n'+'Maths Mark: '+tex[2]+'\n'+'Percentage: '+tex[3])

def delete():
    ind=lbox.curselection()
    name=lbox.get(ind)
    del dicton[name]
    lbox.delete(ind)

def edit():
    indi=lbox.curselection()
    ind=lbox.get(indi)
    i=dicton[ind]
    print(i)
    nament.insert(0,ind)
    addent.insert(0,i[0])
    mobent.insert(0,i[1])
    emaent.insert(0,i[2])
    birent.insert(0,i[3])

def save():
    savfile=asksaveasfile(title='Save as:')
    if savfile!=NONE:
        print(dicton,file=savfile)
        lbox.delete(0,END)

op=Button(sc,text='Open', bg='yellow',command=openfile)
op.grid(row=6,column=4,padx=20)
sh=Button(sc,text='Show',bg='yellow',command=show)
sh.grid(row=6,column=2,padx=20)
ed=Button(sc,text='Edit',bg='yellow',command=edit)
ed.grid(row=6,column=0)
de=Button(sc,text='Delete',bg='yellow',command=delete)
de.grid(row=6,column=1)
ad=Button(sc,text='Add/Update',bg='yellow',command=adding)
ad.grid(row=6,column=3)
sa=Button(sc,text='Save',width=40,bg='light green',command=save)
sa.grid(row=7,column=0,columnspan=4,pady=15)

lbox=Listbox(sc,width=60,height=10)
lbox.grid(row=8,column=0,padx=10,columnspan=2)

sc.mainloop()