from tkinter import *
import tkinter.ttk

sc=Tk()
sc.geometry('600x400')
sc.title('Pizza Hut')
sc.configure(bg='light gray')

menu=['Cheesy Glory']
menu.append('Pepperoni Feast')
menu.append('Veg Extravaganza')
menu.append('Chicken Supreme')
menu.append('Doner Delight')
menu.append('Hawaiian')
menu.append('Vegan Margarhita')
menu.append('The G.O.A.T')
menu.append('Nduja Nibble')
menu.append('Garlic Bread')
menu.append('Cheesy Garlic Bread')

numbers=[]

til=Label(sc,text='Welcome to the Pizza Hut website!',bg='light gray',font=('Ariel',10,'bold'))
til.grid(row=0,column=1,padx=70,pady=15)

sel1=Label(sc,text='Select Your Pizza:',bg='light gray')
sel1.grid(row=1,column=0,padx=15,pady=20)

sel2=Label(sc,text='Enter Quantity:',bg='light gray')
sel2.grid(row=2,column=0)

size=StringVar()

S=tkinter.ttk.Radiobutton(sc,text='S',variable=size,value='small')
S.grid(row=1,column=2,padx=30)
M=tkinter.ttk.Radiobutton(sc,text='M',variable=size,value='medium')
M.grid(row=2,column=2)
L=tkinter.ttk.Radiobutton(sc,text='L',variable=size,value='large')
L.grid(row=3,column=2,pady=20)

inp=tkinter.ttk.Combobox(sc)
inp['values']=menu
inp.grid(row=1,column=1)

inp2=tkinter.ttk.Combobox(sc)
for i in range(1,16,1):
    numbers.append(i)
inp2['values']=numbers
inp2.grid(row=2,column=1)

text=Label(sc,text='',bg='light gray')
text.grid(row=5,column=1,pady=30)

def finished():
    num=inp2.get()
    type=inp.get()
    si=size.get()
    text.configure(text='You ordered ' + str(num) + ' ' + str(si) + ' ' + str(type) + ' pizzas.')

ord=Button(text='Order',bg='lime',command=finished)
ord.grid(row=4,column=1)

sc.mainloop()