from tkinter import*
from math import*
import subprocess
w=Tk()
w.title("Health Calci")
w.geometry('1920x1080')
f=('Mervale Script',20)
radio = IntVar()
def suggest():
    subprocess.call(["python", "bfp1.py"])
def call():
    if ((radio.get()==1)and(int(e1.get())>=18)):
        result=1.20*(float(e3.get())/(float(e2.get())**2))+0.23*float(e1.get())-16.2
        l3.config(text="Result="+str(result))
    if ((radio.get()==1)and(int(e1.get())<18)):
        result=1.51*(float(e3.get())/(float(e2.get())**2))-0.70*float(e1.get())-2.2
        l3.config(text="Result="+str(result))
    if ((radio.get()==2)and(int(e1.get())>=18)):
        result=1.20*(float(e3.get())/(float(e2.get())**2))+0.23*float(e1.get())-5.4
        l3.config(text="Result="+str(result))
    if ((radio.get()==2)and(int(e1.get())<18)):
        result=1.51*(float(e3.get())/(float(e2.get())**2))-0.70*float(e1.get())+1.4
        l3.config(text="Result="+str(result))
    b2=Button(w,text="Suggestion",font=f,fg="blue",bd=5,command=suggest)
    b2.grid(row=8,column=1,padx=5,pady=5)
        

"""Labels"""
l1=Label(w,text="Height (in 'm')",font=f)
l1.grid(row=2,column=0,padx=200,pady=25)
l2=Label(w,text="Weight (in 'kg')",font=f)
l2.grid(row=3,column=0,padx=200,pady=25)
l3=Label(w,text="Result",font=f)
l3.grid(row=7,column=1,padx=200,pady=25)
l4=Label(w,text="Age",font=f)
l4.grid(row=1,column=0,padx=200,pady=25)
l5=Label(w,text="Neck (in 'cm')",font=f)
l5.grid(row=4,column=0,padx=200,pady=25)
l6=Label(w,text="Waist (in 'cm')",font=f)
l6.grid(row=5,column=0,padx=200,pady=25)
l7=Label(w,text="Gender",font=f)
l7.grid(row=0,column=0,padx=200,pady=25)
"""Entries"""
e1=Entry(w,font=f,fg="red")
e1.grid(row=1,column=1,padx=5,pady=5)
e2=Entry(w,font=f,fg="red")
e2.grid(row=2,column=1,padx=5,pady=5)
e3=Entry(w,font=f,fg="red")
e3.grid(row=3,column=1,padx=5,pady=5)
e4=Entry(w,font=f,fg="red")
e4.grid(row=4,column=1,padx=5,pady=5)
e5=Entry(w,font=f,fg="red")
e5.grid(row=5,column=1,padx=5,pady=5)
"""Buttons"""
b1=Button(w,text="calculate",font=f,fg="blue",bd=5,command=call).grid(row=6,column=1,padx=5,pady=5)
"""Radio Buttons"""
R1 = Radiobutton(w, text="Male", variable=radio, value=1,font=f).grid(row=0,column=1,padx=0,pady=5)
R2 = Radiobutton(w, text="Female", variable=radio, value=2,font=f).grid(row=0,column=2,padx=0,pady=5)
w.mainloop()
