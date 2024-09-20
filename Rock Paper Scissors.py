from tkinter import *
import random

sc=Tk()
sc.geometry('600x400')
sc.configure(bg='light gray')
sc.title("Rock Paper Scissors")

playerscore=0
computerscore=0

def playerwin():
    global playerscore
    playerscore+=1
    mes.configure(text="PLAYER WINS!")
    pl.configure(text="Player Score: "+ str(playerscore))
def compwin():
    global computerscore
    computerscore+=1
    mes.configure(text="COMPUTER WINS!")
    co.configure(text="Computer Score: "+ str(computerscore))
def tie():
    mes.configure(text="IT IS A TIE!")

choiceses=['Rock','Paper','Scissors']

def com(user_choice):
    comp_choice=random.choice(choiceses)
    comp.configure(text="Computer chose: "+ comp_choice)
    player.configure(text="Player chose: "+ user_choice)
    if comp_choice=='Rock' and user_choice=='Scissors':
        compwin()
    if comp_choice=='Scissors' and user_choice=='Rock':
        playerwin()
    if comp_choice=='Paper' and user_choice=='Rock':
        compwin()
    if comp_choice=='Rock' and user_choice=='Paper':
        playerwin()
    if comp_choice=='Scissors' and user_choice=='Paper':
        compwin()
    if comp_choice=='Paper' and user_choice=='Scissors':
        playerwin()
    if comp_choice==user_choice:
        tie()

title=Label(sc,bg='light gray',text='Rock, Paper, Scissors',font=('Times New Roman bold',30),fg='dark red')
mes=Label(sc,bg='light gray',text='testssasasas',font=('Times New Roman bold',15),fg='green')
title.grid(row=0,column=0,columnspan=3,padx=110,pady=5)
mes.grid(row=1,column=0,columnspan=3)

choices=Label(sc,bg='light gray',text='Take your pick: ',font=('Times New Roman bold',15),fg='gray')
choices.grid(row=2,column=0,columnspan=3,pady=10)

rock=Button(sc,bg='cyan',text='Rock',command= lambda: com('Rock'))
rock.grid(row=3,column=0)
paper=Button(sc,bg='lime',text='Paper',command= lambda: com('Paper'))
paper.grid(row=3,column=1)
scissors=Button(sc,bg='red',text='Scissors',command= lambda: com('Scissors'))
scissors.grid(row=3,column=2)

scores=Label(sc,bg='light gray',text='Results:',font=('Times New Roman bold',15),fg='gray')
scores.grid(row=4,column=1,pady=15)

player=Label(sc,bg='light gray',text='Player chose: ',fg='gray')
player.grid(row=5,column=1)
comp=Label(sc,bg='light gray',text='Computer chose: ',fg='gray')
comp.grid(row=6,column=1)
space=Label(sc,bg="light gray",text='',fg='light gray')
space.grid(row=7,column=1)
pl=Label(sc,bg='light gray',text='Player Score:  ',fg='gray')
pl.grid(row=8,column=1)
co=Label(sc,bg='light gray',text='Computer Score: ',fg='gray')
co.grid(row=9,column=1)

sc.mainloop()