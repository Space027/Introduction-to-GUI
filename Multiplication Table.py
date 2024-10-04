from tkinter import *
import tkinter.ttk

sc=Tk()
sc.geometry('450x650')
sc.configure(bg='light gray')
sc.title('Multiplication Table')

numbers=[]

title=Label(sc,bg='light gray',text='Multiplication Table',font=('Calibri', 20, 'bold'))
title.grid(row=0,column=1,pady=20,padx=5)

lab=Label(sc,bg='light gray',text='Number & Range:')
lab.grid(row=1,column=0,padx=5)
inp=tkinter.ttk.Combobox(sc)
for i in range(1,101,1):
    numbers.append(i)
inp['values']=numbers
inp.grid(row=1,column=1)

multiples=IntVar()

rad1=tkinter.ttk.Radiobutton(sc,text='10',variable=multiples,value=10)
rad1.grid(row=1,column=2,padx=10)
rad2=tkinter.ttk.Radiobutton(sc,text='20',variable=multiples,value=20)
rad2.grid(row=2,column=2)
rad3=tkinter.ttk.Radiobutton(sc,text='30',variable=multiples,value=30)
rad3.grid(row=3,column=2)

def gen():
    number=inp.get()
    number=int(number)
    m=multiples.get()
    table=''
    for i in range(1,m+1,1):
        ans=str(number*i)
        table=table+str(str(number)+ " x " + str(i) + " = " + ans+'\n')
    answers.configure(text=table)    

genbutton=Button(sc,bg='light green',text='Generate!',command=gen)
genbutton.grid(row=2,column=1,pady=5)

#print(str(number)+ " x " + str(i) + " = " + ans)

answers=Label(sc,bg='light gray')
answers.grid(row=4,column=1,pady=10)

sc.mainloop()