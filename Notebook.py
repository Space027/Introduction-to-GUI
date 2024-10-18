from tkinter import *
from tkinter.filedialog import *

sc=Tk()
sc.geometry('400x400')
sc.title('Notebook')
sc.configure(bg='purple')

def openfile():
    opefil=askopenfile(title='Open File')

op=Button(sc,text='OPEN',bg='black',fg='white',width=16,command=openfile)
op.grid(row=0,column=0,pady=10,padx=10)
de=Button(sc,text='DELETE',bg='black',fg='white',width=15)
de.grid(row=0,column=1)
sa=Button(sc,text='SAVE',bg='black',fg='white',width=16)
sa.grid(row=0,column=3,pady=10,padx=10)

ent=Entry(sc)
ent.grid(row=1,column=0,padx=10)

sc.mainloop()
