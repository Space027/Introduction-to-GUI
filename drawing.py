from tkinter import *
from tkinter.colorchooser import askcolor

class Drawing():
    size=3
    defaultcolour='black'
    def __init__(self):   
        self.sc=Tk()
        self.sc.geometry('600x500')
        self.sc.title('Canvas')
        self.sc.config(bg='light gray') 
        self.ca=Canvas(self.sc,width=600,height=500,bg='white')   
        self.ca.grid(row=1,column=0,columnspan=7)
        self.b1=Button(self.sc,text='Pen',command=self.penning)
        self.b2=Button(self.sc,text='Brush',command=self.brushing)
        self.b3=Button(self.sc,text='Colour',command=self.colouring)
        self.b4=Button(self.sc,text='Rubber',command=self.rubbing)
        self.sli=Scale(self.sc,from_=0,to_=10,orient=HORIZONTAL)
        self.b1.grid(row=0,column=1,pady=15)
        self.b2.grid(row=0,column=2)
        self.b3.grid(row=0,column=3)
        self.b4.grid(row=0,column=4)
        self.sli.grid(row=0,column=5)
        self.setup()
        self.sc.mainloop()
    def reset(self,event):
        self.oldx=None
        self.oldy=None
    def setup(self):
        self.oldx=None
        self.oldy=None
        self.thickness=self.sli.get()
        self.colour=self.defaultcolour
        self.eraser_on=False
        self.active_button=self.b1
        self.ca.bind('<B1-Motion>',self.paint)
        self.ca.bind('<ButtonRelease-1>',self.reset)
    def paint(self,event):
        self.thickness=self.sli.get()
        if self.eraser_on==True:
            self.paintcolour='white'
        else:
            self.paintcolour=self.colour
        if self.oldx and self.oldy:
            self.ca.create_line(self.oldx,self.oldy,event.x,event.y,width=self.thickness,fill=self.paintcolour,capstyle=ROUND,smooth=TRUE,splinesteps=36)
        self.oldx=event.x
        self.oldy=event.y
    def activate_button(self,selected_button):
        self.active_button.config(relief=RAISED)
        selected_button.config(relief=SUNKEN)
        self.active_button=selected_button
    def penning(self):
        self.activate_button(self.b1)
        self.eraser_on=False
    def brushing(self):
        self.activate_button(self.b2)
        self.eraser_on=False
    def rubbing(self):
        self.activate_button(self.b4)
        self.eraser_on=True
    def colouring(self):
        self.colour=askcolor(color=self.colour)[1]

Drawing()

