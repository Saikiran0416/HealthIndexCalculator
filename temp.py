from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
w= Tk()
w.title("Health Calci")

# Define the geometry of the window
w.geometry("1920x1080")


# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("bmi.jfif"))
img2 = ImageTk.PhotoImage(Image.open("maintainance.jpg"))
img3 = ImageTk.PhotoImage(Image.open("normal.jfif"))
img4= ImageTk.PhotoImage(Image.open("w gain.jpg"))
img5 = ImageTk.PhotoImage(Image.open("w loss.jpg"))
img6=ImageTk.PhotoImage(Image.open("3.jfif"))
# Create a Label Widget to display the text or Image
label = Label(w, image = img)
label2= Label(w,image = img2)
label3= Label(w,image = img3)
label4= Label(w,image = img4)
label5= Label(w,image = img5)
label6= Label(w,image = img6)
label.grid(row=0,column=0,padx=60,pady=40)
label2.grid(row=0,column=1,padx=60,pady=40)
label3.grid(row=1,column=0,padx=60,pady=40)
label4.grid(row=1,column=1,padx=60,pady=40)
label5.grid(row=0,column=2,padx=60,pady=40)
label6.grid(row=1,column=3,padx=2,pady=2)

w.mainloop()
