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

class Ball():
    def __init__(self):
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
        if self.pos[0]<0:
            self.x=random.randint(2,4)
            self.score2+=1
        if self.pos[1]>550:
            self.y=random.randint(-4,-2)
        if self.pos[1]<0:
            self.y=random.randint(2,4)

balll=Ball()

while True:
    balll.draw()
    sc.update_idletasks()
    sc.update()
    time.sleep(0.01)
sc.mainloop()