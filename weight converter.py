from tkinter import *

#stones=kgx0.1575
#pounds=kgx2.204623
#ounces=kgx35.273961





screen=Tk()
screen.geometry('700x230')
screen.title("Weight Converter")

label=Label(screen,text="Enter weight in kilograms:",font=('Calibri',15))
label.grid(row=0,column=0)

entry=Entry(screen)
entry.grid(row=0,column=1, padx=70, pady=5)

def thing():
    kg=float(entry.get())
    stones=str(kg*0.1575)
    pounds=str(kg*2.204623)
    ounces=str(kg*35.273961)
    s.configure(text=stones)
    lb.configure(text=pounds)
    oz.configure(text=ounces)


button=Button(screen, bg="yellow",text="Convert",command=thing)
button.grid(row=0,column=2, padx=60)

st=Label(screen,text="Stones:")
po=Label(screen,text="Pounds:")
ou=Label(screen,text="Ounces:")
st.grid(row=1,column=0, pady=40)
po.grid(row=1,column=1, pady=40)
ou.grid(row=1,column=2, pady=40)

s=Label(screen,text="")
lb=Label(screen,text="")
oz=Label(screen,text="")
s.grid(row=2,column=0)
lb.grid(row=2,column=1)
oz.grid(row=2,column=2)






screen.mainloop()