from tkinter import *
import speech_recognition as sr
import tkinter.messagebox
import os

sc=Tk()
sc.geometry('600x400')
sc.title('Speech to Text')
sc.configure(bg='light gray')

title=Label(sc,text='Speech to Text',font=('Times New Roman',35),bg='light gray')
title.grid(row=0,column=0,padx=150)

lab=Label(sc,width=30,bg='light gray',text='')
lab.grid(row=1,column=0,pady=100)

def speechtext():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        tkinter.messagebox.showinfo('Information','Microphone is now in use.')
        audio=r.listen(source)
        tex=r.recognize_google(audio)
        lab.config(text=tex)


button=Button(sc,text='Convert',bg='light green',command=speechtext)
button.place(x=135,y=155)
button2=Button(sc,text='Save',bg='light green')
button2.place(x=400,y=155)

sc.mainloop()