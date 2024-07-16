from tkinter import*
import subprocess
w=Tk()
w.title("Health Calci")
w.geometry('1920x1080')
f=("ARIAL",8)
def open():
     subprocess.call(["python", "bmi.py"])
def open1():
     subprocess.call(["python", "BFP.py"])
def open2():
     subprocess.call(["python", "CP.py"])
des1=Label(w,text="Select your Calculator",font=('Landliebe',25)).grid(row=0,column=1,padx=100,pady=100)
bmibutton=Button(w,text="Body Mass Index",bd=15,command=open,font=f).grid(row=1,column=0,padx=200,pady=100)
bfpbutton=Button(w,text="Body Fat Calculator",bd=15,command=open1,font=f).grid(row=1,column=1,padx=200,pady=100)
cpbutton=Button(w,text="Calorie Predictor",bd=15,command=open2,font=f).grid(row=1,column=2,padx=200,pady=100)
w.mainloop()
