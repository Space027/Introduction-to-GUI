from tkinter import *
import tkinter.messagebox
import random

sc=Tk()
sc.geometry('500x400')
sc.title('Guess the Number!')
sc.configure(bg='light gray')

compchoice=random.randint(1,10)

title=Label(sc,text='GUESS THE NUMBER!',bg='light gray',fg='crimson',font=('Calibri', 25, 'bold'))
title.pack()

q1=Label(sc,text='What is your name?',bg='light gray',font=('Calibri', 12, 'italic'))
q1.place(x=10,y=100)

ans1=Entry(sc)
ans1.place(x=10,y=125)

q2=Label(sc,text='Guess the Number:',bg='light gray',font=('Calibri', 12, 'italic'))
q2.place(x=10,y=200)

ans2=Entry(sc)
ans2.place(x=10,y=225)

def guess():
    global compchoice
    answer=int(ans2.get())
    if answer==compchoice:
        end.configure(text='Well Done. You guessed my number!')
        tkinter.messagebox.showinfo('messagebox','Well Done. You guessed my number!')
    if answer>compchoice:
        tkinter.messagebox.showinfo('messagebox','LOWER!')
    if answer<compchoice:
        tkinter.messagebox.showinfo('messagebox','HIGHER!')

ansbutton=Button(sc,text="Sure?",bg='navy',fg='white',command=guess)
ansbutton.place(x=400,y=212)

end=Label(sc,text='',bg='light gray',font=('Calibri', 15, 'italic'))

sc.mainloop()