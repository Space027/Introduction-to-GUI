from tkinter import *

sc=Tk()
sc.geometry('600x400')
sc.configure(bg='light gray')
sc.title("Rock Paper Scissors")

choiceses=['rock','paper','scissors']

title=Label(sc,bg='light gray',text='Rock, Paper, Scissors',font=('Times New Roman bold',30),fg='dark red')
mes=Label(sc,bg='light gray',text='testssasasas',font=('Times New Roman bold',15),fg='green')
title.grid(row=0,column=0,columnspan=3,padx=110,pady=5)
mes.grid(row=1,column=0,columnspan=3)

choices=Label(sc,bg='light gray',text='Take your pick: ',font=('Times New Roman bold',15),fg='gray')
choices.grid(row=2,column=0,columnspan=3,pady=10)

rock=Button(sc,bg='cyan',text='Rock')
rock.grid(row=3,column=0)
paper=Button(sc,bg='lime',text='Paper')
paper.grid(row=3,column=1)
scissors=Button(sc,bg='red',text='Scissors')
scissors.grid(row=3,column=2)

def calcies():
    

def r():
    return choiceses[0]
def p():
    return choiceses[1]
def s():
    return choiceses[2]


scores=Label(sc,bg='light gray',text='Results:',font=('Times New Roman bold',15),fg='gray')
scores.grid(row=4,column=1,pady=15)

player=Label(sc,bg='light gray',text='Player chose: ',fg='gray')
player.grid(row=5,column=0)
comp=Label(sc,bg='light gray',text='Computer chose: ',fg='gray')
comp.grid(row=6,column=0)

pl=Label(sc,bg='light gray',text='Player Score:  ',fg='gray')
pl.grid(row=5,column=2)
co=Label(sc,bg='light gray',text='Computer Score: ',fg='gray')
co.grid(row=6,column=2)

sc.mainloop()