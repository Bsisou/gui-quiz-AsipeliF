from tkinter import *
from PIL import Image, ImageTk

#This class is the label
class Startpage:
    def __init__(self, game):

        self.heading=Label(game, text="Enter your name", font="arial", fg="white", bg="black")
        self.heading.place(x=170, y=150)   
        self.entry_username=Entry(game)
        self.entry_username.place(x=160, y=200)

        

#main game window
game = Tk() 
game.title("Games")
game.geometry("500x450")
bg = PhotoImage(file="Game.png")
bglabel=Label(game, image=bg)
bglabel.place(x=0, y=0)
#creating the frames
Startpage(game)
game.mainloop()
   
