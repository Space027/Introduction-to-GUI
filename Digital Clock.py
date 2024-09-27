from tkinter import *
import time

sc=Tk()
sc.geometry('450x50')
sc.title('Digital Clock')

def tim():
    now=time.time()
    string=time.strftime('%H:%M:%S:%p:.%f','now')
    clo.configure(text=string)
    clo.after(1,tim)

clo=Label(bg='black',text='',font=('Times New Roman',30),fg='white')
clo.pack()
tim()

sc.mainloop()