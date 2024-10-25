from tkinter import *
from tkinter.filedialog import *

sc=Tk()
sc.geometry('400x350')
sc.title('Notebook')
sc.configure(bg='purple')

def openfile():
    opefil=askopenfile(title='Open File')
    if opefil!=NONE:
        data=opefil.readlines()
        lbox.delete(0,END)
        for i in data:
            lbox.insert(END,i.strip())

def insert():
    entry=ent.get()
    lbox.insert(END,entry)
    ent.delete(0,END)

def dele():
    items=lbox.curselection()
    for i in reversed(items):
        lbox.delete(i)

def save():
    savfile=asksaveasfile(title='Save as:')
    if savfile!=NONE:
        l=lbox.get(0,END)
        for i in l:
            print(i.strip(),file=savfile)
        lbox.delete(0,END)

op=Button(sc,text='OPEN',bg='black',fg='white',width=16,command=openfile)
op.grid(row=0,column=0,pady=10,padx=10)
de=Button(sc,text='DELETE',bg='black',fg='white',width=15,command=dele)
de.grid(row=0,column=1)
sa=Button(sc,text='SAVE',bg='black',fg='white',width=16,command=save)
sa.grid(row=0,column=2,pady=10,padx=10)
ad=Button(sc,text='ADD',bg='black',fg='white',width=16,command=insert)
ad.grid(row=1,column=2)

ent=Entry(sc,width=37)
ent.grid(row=1,column=0,padx=10,pady=10,columnspan=2)

lbox=Listbox(sc,width=60,selectmode=MULTIPLE)
lbox.grid(row=2,column=0,pady=10,columnspan=3)

fruits=['orange','apple','kiwi','mango','cranberry','lime','lemon']

for i in fruits:
    lbox.insert(END,i)

sc.mainloop()
