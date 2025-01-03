from tkinter import *
import tkinter.messagebox

sc=Tk()
sc.geometry('155x210')
sc.title('Noughts and Crosses PVP')

l=['','','','','','','','','']
win=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
num=[0,1,2,3,4,5,6,7,8]

currentplayer='X'

def clicked(selected_button,index): 
    global currentplayer
    if currentplayer=='X':
        if l[index]=='':
            selected_button.config(text='X')
            l[index]=currentplayer
            winner()  
            num.remove(index)
            currentplayer='O'
    if currentplayer=='O':
        if l[index]=='':
            selected_button.config(text='O')
            l[index]=currentplayer
            winner()
            num.remove(index)
            currentplayer='X'
    if len(num)==0:
            tkinter.messagebox.showinfo(':/','It is a draw...')
            return
    winner()
        

l1=Label(sc,text='(X) User: ')
l2=Label(sc,text='(O) User 2: ')

def winner():
    for i in win:
        if l[i[0]]=='X'and l[i[1]]=='X'and l[i[2]]=='X':
            tkinter.messagebox.showinfo(':)','Well Done! \nPlayer 1 Wins!')
        if l[i[0]]=='O'and l[i[1]]=='O'and l[i[2]]=='O':
            tkinter.messagebox.showinfo(':)','Well Done! \nPlayer 2 Wins!')
        
        

b1=Button(sc,width=6,height=3,command=lambda:clicked(b1,0))
b2=Button(sc,width=6,height=3,command=lambda:clicked(b2,1))
b3=Button(sc,width=6,height=3,command=lambda:clicked(b3,2))
b4=Button(sc,width=6,height=3,command=lambda:clicked(b4,3))
b5=Button(sc,width=6,height=3,command=lambda:clicked(b5,4))
b6=Button(sc,width=6,height=3,command=lambda:clicked(b6,5))
b7=Button(sc,width=6,height=3,command=lambda:clicked(b7,6))
b8=Button(sc,width=6,height=3,command=lambda:clicked(b8,7))
b9=Button(sc,width=6,height=3,command=lambda:clicked(b9,8))

bu=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

l1.grid(row=0,column=0,columnspan=3)
l2.grid(row=1,column=0,columnspan=3)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)



sc.mainloop()