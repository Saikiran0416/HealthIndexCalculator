from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
w= Tk()
w.title("Health Calci")

# Define the geometry of the window
w.geometry("1920x1080")


# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("bfp.png"))
img2 = ImageTk.PhotoImage(Image.open("bfp2.png"))
img3 = ImageTk.PhotoImage(Image.open("bfp3.png"))
img4= ImageTk.PhotoImage(Image.open("bfp5.png"))
img5 = ImageTk.PhotoImage(Image.open("bfpworkout.png"))
img6=ImageTk.PhotoImage(Image.open("bfp4.png"))
# Create a Label Widget to display the text or Image
label = Label(w, image = img)
label2= Label(w,image = img2)
label3= Label(w,image = img3)
label4= Label(w,image = img4)
label5= Label(w,image = img5)
label6= Label(w,image = img6)
label.grid(row=0,column=0,)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
label4.grid(row=1,column=1)
label5.grid(row=0,column=2)
label6.grid(row=1,column=3)

w.mainloop()
