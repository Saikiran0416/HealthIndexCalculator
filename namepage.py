from tkinter import*
import subprocess
from tkinter import messagebox
w=Tk()
w.title("Health Calci")
w.geometry('1920x1080')
f=("Lucida Handwriting",50)
f1=Frame(w,width=200,highlightbackground='black',highlightthickness=5)
f1.pack(side=TOP,padx=100,pady=100)
nametitle=Label(f1,text="NAME",font=f).pack(side=TOP,pady=50)
nameentry=Entry(f1,width=50)
nameentry.pack(side=TOP,padx=200)
def open():
     messagebox.showinfo("information","WELCOME "+nameentry.get())
     subprocess.call(["python", "calci page.py"])
confirmbutton=Button(f1,text="Confirm",bd=15,command=open,font=('ARIAL',25))
confirmbutton.pack(side=TOP,pady=150)

w.mainloop()
