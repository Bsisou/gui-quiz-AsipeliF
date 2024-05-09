from PIL import Image,ImageTk
from tkinter import*


root=Tk()
bg = PhotoImage(file="Game.png")
bglabel=Label(root,image=bg)
bglabel.place(x=0,y=0)
root.title("Games")
root.geometry("500x500")
root.mainloop()