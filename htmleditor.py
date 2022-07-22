from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("650x700")
root.title("Html Editor")   
root.configure(background='gray10')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))

label_filename = Label(root,text="File Name",bg="gray19",fg="white")
label_filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename = Entry(root,bg="gray19",fg="white")
input_filename.place(relx=0.45,rely=0.03,anchor=CENTER)

text_area = Text(root,height=38,width=80,bg="gray19",fg="white")
text_area.place(relx=0.5,rely=0.55,anchor=CENTER) 


root.mainloop()