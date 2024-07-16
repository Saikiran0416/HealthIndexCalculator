from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
w= Tk()
w.title("Health Calci")

# Define the geometry of the window
w.geometry("1920x1080")


# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("cp1.png"))
img2 = ImageTk.PhotoImage(Image.open("cp6.png"))
img3 = ImageTk.PhotoImage(Image.open("cp3.png"))
img4= ImageTk.PhotoImage(Image.open("cp4.png"))
img5 = ImageTk.PhotoImage(Image.open("cp5.png"))
img6=ImageTk.PhotoImage(Image.open("cp2.png"))
# Create a Label Widget to display the text or Image
label = Label(w, image = img)
label2= Label(w,image = img2)
label3= Label(w,image = img3)
label4= Label(w,image = img4)
label5= Label(w,image = img5)
label6= Label(w,image = img6)
label.grid(row=0,column=0,padx=20,pady=10)
label2.grid(row=0,column=1,padx=20,pady=10)
label3.grid(row=1,column=0,padx=20,pady=10)
label4.grid(row=1,column=1,padx=20,pady=10)
label5.grid(row=0,column=2,padx=20,pady=10)
label6.grid(row=1,column=3,pady=10)

w.mainloop()
