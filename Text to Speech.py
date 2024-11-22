from tkinter import *
from gtts import gTTS
import os

sc=Tk()
sc.geometry('600x400')
sc.title('Text to Speech')
sc.configure(bg='light gray')

title=Label(sc,text='Text to Speech',font=('Times New Roman',35),bg='light gray')
title.grid(row=0,column=0,padx=150)

ent=Entry(sc,width=30)
ent.grid(row=1,column=0,pady=100)

def textspeech():
    obj=gTTS(ent.get(),lang='en',slow=False)
    obj.save('spee.wav')
    os.system('spee.wav')


button=Button(sc,text='Convert',bg='light green',command=textspeech)
button.place(x=50,y=155)

sc.mainloop()