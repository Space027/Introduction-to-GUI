from tkinter import *
import random
import time


sc=Tk()
sc.geometry('600x600')
sc.title('Pong')

ca=Canvas(sc,width=600,height=600,bg='black')
ca.grid(row=0,column=0)
ca.create_line(300,0,300,600,width=5,fill='white')
ca.create_oval(200,200,400,400,outline='white')
scor=ca.create_text(300,20,font=('Times New Roman',20,'bold'),text='0 : 0',fill='white')

class Ball():
    def __init__(self,p1,p2):
        self.player1=p1
        self.player2=p2
        self.colour='red'
        self.bal=ca.create_oval(275,275,325,325,width=0,fill=self.colour)
        self.direction=[-1,-2,-3,-4,-5,1,2,3,4,5]
        random.shuffle(self.direction)
        self.x=self.direction[0]
        self.y=self.direction[1]
        self.score1=0
        self.score2=0
    def draw(self):
        ca.move(self.bal,self.x,self.y)
        self.pos=ca.coords(self.bal)
        if self.pos[0]>550:
            self.x=random.randint(-4,-2)
            self.score1+=1
            self.update()
        if self.pos[0]<0:
            self.x=random.randint(2,4)
            self.score2+=1
            self.update()
        if self.pos[1]>550:
            self.y=random.randint(-4,-2)
        if self.pos[1]<0:
            self.y=random.randint(2,4)     
    def update(self):
        scor.config(text=str(self.score1)+' : '+str(self.score2))
    def hitpadel(self):
        self.bpos=ca.coords(self.bal)
        self.p1pos=ca.coords(self.player1.pad1)
        self.p2pos=ca.coords(self.player2.pad2)
        if self.bpos[3]>=self.p1pos[1] and self.bpos[1]<=self.p1pos[3]:
            if self.bpos[0]<=self.p1pos[2] and self.bpos[0]>=self.p1pos[0]:
                self.x=4
        if self.bpos[3]>=self.p2pos[1] and self.bpos[1]<=self.p2pos[3]:
            if self.bpos[2]>=self.p2pos[0] and self.bpos[2]<=self.p2pos[2]:
                self.x=-4



class Padel1():
    def __init__(self):
        self.colour='white'
        self.pad1=ca.create_rectangle(20,20,30,100,fill=self.colour)
        self.x=0
        self.y=0
        ca.bind_all('w',self.up)
        ca.bind_all('s',self.down)
    def up(self,event):
        self.y=-3
    def down(self,event):
        self.y=+3
    def draw(self):
        ca.move(self.pad1,self.x,self.y)
        self.pos=ca.coords(self.pad1)
        if self.pos[1]>550:
            self.y=-3
        if self.pos[1]<0:
            self.y=3

class Padel2():
    def __init__(self):
        self.colour='white'
        self.pad2=ca.create_rectangle(570,20,580,100,fill=self.colour)
        self.x=0
        self.y=0
        ca.bind_all('<KeyPress-Up>',self.up)
        ca.bind_all('<KeyPress-Down>',self.down)
    def up(self,event):
        self.y=-3
    def down(self,event):
        self.y=+3
    def draw(self):
        ca.move(self.pad2,self.x,self.y)
        self.pos=ca.coords(self.pad2)
        if self.pos[1]>550:
            self.y=-3
        if self.pos[1]<0:
            self.y=3

pad1=Padel1()
pad2=Padel2()
balll=Ball(pad1,pad2)


while True:
    balll.draw()
    pad1.draw()
    pad2.draw()
    balll.hitpadel()
    sc.update_idletasks()
    sc.update()
    time.sleep(0.01)
sc.mainloop()