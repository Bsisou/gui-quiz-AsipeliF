from tkinter import *
from PIL import Image, ImageTk

name_list = []
global question_answers
asked = []

question_answers = {
    1:['Modern Warfare 3', 'Call of Duty', 'Fortnite', 'Apex Legends',3]
}

#Picks a random question
def randomioser():
    global qnum
    qnum = random.radiant(1,4)
    if qnum not in asked:
        asked.appen(qnum)

#This class is the mainpage
class Startpage:
    def __init__(self, game):

        #Label 
        self.heading=Label(game, text="Enter your name", font="arial", fg="white", bg="black")
        self.heading.place(x=170, y=150) 
        #Entry box
        self.entry_username=Entry(game)
        self.entry_username.place(x=160, y=200)
        #Button
        self.btn = Button(game,text="Continue", command=self.continue_button)
        self.btn.pack(side = 'top')
        self.btn.place(x=200, y=250)
        
    #Destroys window
    def continue_button(self):
        self.username = self.entry_username.get()
        game.destroy()
        
#main game window
game = Tk() 
game.title("Games")
game.geometry("500x500")
#Adding the background image
bg = PhotoImage(file="Game.png")
bglabel=Label(game, image=bg)
bglabel.place(x=0, y=0)
Startpage(game)
game.mainloop()

class Quizpage:
    def __init__(self, game1):
        self.heading=Label(game1, text="Quiz", font="arial", fg="white", bg="black")
        self.heading.place(x=200, y=200)

#Question game window
game1 = Tk()
game1.title("Question")
game1.geometry("500x500")
#Adding the background image
bg1 = PhotoImage(file="Game(1).png")
bglabel1=Label(game1, image=bg1)
bglabel1.place(x=0, y=0)
Quizpage(game1)
#creating the frames
game1.mainloop()
   
