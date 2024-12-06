from tkinter import *
import tkinter.messagebox
import random

sc=Tk()
sc.geometry('300x300')
sc.configure(bg='black')

questions=5
word=''
jumbledword=''
score=0

words=['umbrella','banana','pineapple','coriander','keyboard','coding','spaghetti','geometry','thunderstorm','antidote','medicine']

def ranword():
    global word
    global jumbledword
    jumbledword=''
    numbers=random.sample(range(len(words)),5)
    word=words[numbers[0]]
    index=random.sample(range(len(word)),len(word))
    for i in index: 
        jumbledword=word[i]+jumbledword
    ana.config(text=jumbledword)

tile=Label(sc,text='Jumbled Word Game',font=('Calibri',20),bg='black',fg='white')
tile.grid(row=0,column=1,padx=30)
ana=Label(sc,bg='black',fg='white',font=('Calibri',20))
ana.grid(row=1,column=1,pady=40)
ranword()
ent=Entry(sc,width=20)
ent.grid(row=3,column=1)


def che():
    global word
    global score
    if ent.get()==word:
        score+=1
        tkinter.messagebox.showinfo(':)','Well Done! \nYou got it right! \n You have a score of '+ str(score) + '!')
        again=tkinter.messagebox.askyesno('Well Done!', 'Do you want to play again?')

        
    else:
        tkinter.messagebox.showerror(':(','Bad Luck... \nYou got it wrong.')
        again=tkinter.messagebox.askyesno('Bad Luck...', 'Do you want to play again?')
    if again==True:
        ranword()
        ent.delete(0,tkinter.END)
    else:
        sc.destroy()

def rese():
    ranword()
    ent.delete(0,tkinter.END) 

check=Button(sc,text='Check',bg='lime',command=che)
check.grid(row=4,column=1,pady=20)
reset=Button(sc,text='Reset',bg='yellow',command=rese)
reset.grid(row=5,column=1)

sc.mainloop()