from tkinter import *
from PIL import Image, ImageTk

#This class is the label
class Startpage:
    def __init__(self, game):

        #Label 
        self.heading=Label(game, text="Enter your name", font="arial", fg="white", bg="black")
        self.heading.place(x=170, y=150)   
        self.entry_username=Entry(game)
        self.entry_username.place(x=160, y=200)
        self.btn = Button(game,text="Continue", command=self.continue_button)
        self.btn.pack(side = 'top')
        self.btn.place(x=200, y=250)
        

    def continue_button(self):
        self.username = self.entry_username.get()
        game.destroy()

class Questpage:
    def __init__(self, game1):
        self.heading=Label(game1, text="What games is this", font="arial", fg="white", bg="black")



       
#main game window
game = Tk() 
game.title("Games")
game.geometry("500x500")
bg = PhotoImage(file="Game.png")
bglabel=Label(game, image=bg)
bglabel.place(x=0, y=0)

#Question game window
game1 = Tk()
game1.title("Question")

#creating the frames
Startpage(game)
game.mainloop()
   
