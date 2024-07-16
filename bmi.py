from tkinter import*
import subprocess
w=Tk()
w.title("Health Calci")
w.geometry('1920x1080')
f=('ARIAL',20)
def suggest():
    subprocess.call(["python", "temp.py"])
def call():
    result=float(e2.get())/(float(e1.get())**2)
    l3.config(text="Result="+str(result))
    b2=Button(f1,text="Suggestion",font=f,fg="black",bd=5,command=suggest)
    b2.grid(row=4,column=1,padx=5,pady=5)
    return
    
f1=Frame(w,width=100,highlightbackground='black',highlightthickness=15)
f1.grid(row=0,column=0,padx=450,pady=100)
l1=Label(f1,text="height (in 'm') =",font=f)
e1=Entry(f1,font=f,fg="red")
l2=Label(f1,text="weight in kg",font=f)
e2=Entry(f1,font=f,fg="red")
l3=Label(f1,text="result",font=f)
l1.grid(row=0,column=0,padx=50,pady=40)
l2.grid(row=1,column=0,padx=50,pady=40)
e1.grid(row=0,column=1,padx=50,pady=40)
e2.grid(row=1,column=1,padx=50,pady=40)
l3.grid(row=3,column=1,padx=50,pady=40)
b1=Button(f1,text="calculate",font=f,fg="blue",bd=5,command=call)
b1.grid(row=2,column=1,padx=50,pady=40)
w.mainloop()


