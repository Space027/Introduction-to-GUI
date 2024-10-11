from tkinter import *
import time

sc=Tk()
sc.geometry('190x170')
sc.title('Timer Countdown')
sc.configure(bg='light gray')

hr=IntVar()
mi=IntVar()
se=IntVar()

hr.set('0 0 0')
mi.set('0 0 0')
se.set('0 0 0')

hrs=Entry(sc,width=5,textvariable=hr)
min=Entry(sc,width=5,textvariable=mi)
sec=Entry(sc,width=5,textvariable=se)
hrs.grid(row=0,column=0,padx=15,pady=15)
min.grid(row=0,column=1)
sec.grid(row=0,column=2,padx=15)

def start():
    global hr
    global mi
    global se
    totaltime=int(hr.get())*3600
    totaltime=totaltime+int(mi.get())*60
    totaltime=totaltime+int(se.get())
    totaltime=totaltime-1
    print(totaltime)
    if totaltime==0:
        time.sleep(90)
    else:
        time.sleep(1)
        hr=totaltime//3600
        mi=(totaltime%3600)//60
        se=totaltime%60
        sc.update()
        start()
        

bu1=Button(sc,bg='lime',text='SET TIME',command=start)
bu1.grid(row=1,column=1,pady=30)


sc.mainloop()