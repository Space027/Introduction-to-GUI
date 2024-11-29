from tkinter import *
import tkinter.messagebox
import random

sc=Tk()
sc.geometry('300x300')
sc.configure(bg='black')

questions=5

words=['umbrella','banana','pineapple','coriander','keyboard','coding','spaghetti','geometry','thunderstorm','antidote','medicine']

numbers=random.sample(range(len(words)),5)
word=words[numbers[0]]
print(word)
index=random.sample(range(len(word)),len(word))
for i in index:
    print(word[i])

tile=Label(sc,text='Jumbled Word Game',font=('Calibri',20),bg='black',fg='white')
tile.grid(row=0,column=1,padx=30)
ana=Label(sc,text='edr',bg='black',fg='white',font=('Calibri',20))
ana.grid(row=1,column=1,pady=40)

ent=Entry(sc,width=20)
ent.grid(row=3,column=1)

check=Button(sc,text='Check',bg='lime')
check.grid(row=4,column=1,pady=20)
reset=Button(sc,text='Reset',bg='yellow')
reset.grid(row=5,column=1)

sc.mainloop()