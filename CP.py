from tkinter import*
from math import*
import subprocess
w=Tk()
w.title("Health Calci")
w.geometry('1920x1080')
f=('ARIAL',20)
radio = IntVar()
menu= StringVar()
menu.set("Select Pysical activity level")
def suggest():
    subprocess.call(["python", "cp1.py"])
def call():
    if radio.get()==1:
        result=66.5 + (13.75 * float(e3.get())) + (5.003 * float(e2.get())) - (6.75 * float(e1.get()))
        l3.config(text="Result="+str(result)+"Kcal")
    if radio.get()==2:
        result=655.1 + (9.563 * float(e3.get())) + (1.850 * float(e2.get())) - (4.676 * float(e1.get()))
        l3.config(text="Result="+str(result)+"Kcal")
    """Advanced"""
    if (radio.get()==1 or radio.get()==2 and menu.get()=="Sedentary (little or no exercise)"):
        result=(66.5 + (13.75 * float(e3.get())) + (5.003 * float(e2.get())) - (6.75 * float(e1.get())))*1.2
        l3.config(text="Result="+str(result))
    if (radio.get()==1 or radio.get()==2 and menu.get()=="Lightly active (light exercise/sports 1-3 days/week)"):
        result=(66.5 + (13.75 * float(e3.get())) + (5.003 * float(e2.get())) - (6.75 * float(e1.get())))*1.375
        l3.config(text="Result="+str(result))
    if (radio.get()==1 or radio.get()==2 and menu.get()=="Moderately active (moderate exercise/sports 3-5 days/week)"):
        result=(66.5 + (13.75 * float(e3.get())) + (5.003 * float(e2.get())) - (6.75 * float(e1.get())))*1.55
        l3.config(text="Result="+str(result))
    if (radio.get()==1 or radio.get()==2 and menu.get()=="Very active (hard exercise/sports 6-7 days a week)"):
        result=(66.5 + (13.75 * float(e3.get())) + (5.003 * float(e2.get())) - (6.75 * float(e1.get())))*1.725
        l3.config(text="Result="+str(result))
    if (radio.get()==1 or radio.get()==2 and menu.get()=="If you are extra active (very hard exercise/sports & a physical job)"):
        result=(66.5 + (13.75 * float(e3.get())) + (5.003 * float(e2.get())) - (6.75 * float(e1.get())))*1.9
        l3.config(text="Result="+str(result))
    b2=Button(f1,text="Suggestion",font=f,fg="blue",bd=5,command=suggest)
    b2.grid(row=9,column=1,padx=5,pady=5)
        
f1=Frame(w,width=20,highlightcolor='black',highlightthickness=20)
f1.grid(row=0,column=1,padx=250,pady=10)
"""Labels"""
l1=Label(f1,text="height (in 'Cm')",font=f)
l1.grid(row=2,column=0,padx=100,pady=15)
l2=Label(f1,text="weight (in 'kg')",font=f)
l2.grid(row=3,column=0,padx=100,pady=20)
l3=Label(f1,text="result",font=f)
l3.grid(row=8,column=1,padx=100,pady=20)
l4=Label(f1,text="Age",font=f)
l4.grid(row=1,column=0,padx=50,pady=20)
l5=Label(f1,text="Gender",font=f)
l5.grid(row=0,column=0,padx=50,pady=20)
l6=Label(f1,text="PAL(Optional)",font=f)
l6.grid(row=6,column=0,padx=50,pady=20)
"""Entries"""
e1=Entry(f1,font=f,fg="red")
e1.grid(row=1,column=1,padx=5,pady=5)
e2=Entry(f1,font=f,fg="red")
e2.grid(row=2,column=1,padx=5,pady=5)
e3=Entry(f1,font=f,fg="red")
e3.grid(row=3,column=1,padx=5,pady=5)
"""Buttons"""
b1=Button(f1,text="calculate",font=f,fg="blue",bd=5,command=call).grid(row=7,column=1,padx=5,pady=5)
"""Radio Buttons"""
R1 = Radiobutton(f1, text="Male", variable=radio, value=1,font=f).grid(row=0,column=1,padx=0,pady=5)
R2 = Radiobutton(f1, text="Female", variable=radio, value=2,font=f).grid(row=0,column=2,padx=0,pady=5)
"""Drop Down Menu"""
drop= OptionMenu(f1, menu,"Sedentary (little or no exercise)", "Lightly active (light exercise/sports 1-3 days/week)",
                 "Moderately active (moderate exercise/sports 3-5 days/week)","Very active (hard exercise/sports 6-7 days a week)",
                 "If you are extra active (very hard exercise/sports & a physical job)")
drop.grid(row=6,column=1,padx=5,pady=5)
w.mainloop()
