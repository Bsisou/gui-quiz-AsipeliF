from tkinter import *
from PIL import Image, ImageTk


class Quiz:
    def __init__(self, parent):

    
        self.bg_image = Image.open("Game.png") 
      
        self.bg_image = self.bg_image.resize((450, 350), Image.LANCZOS) 
      
        self.bg_image = ImageTk.PhotoImage(self.bg_image) 
        
        self.quiz_frame=Frame(parent, bg = background_color)
        self.quiz_frame.grid()         
        
        self.image_label= Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1) 

        self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font=("Tw Cen MT","18","bold")
        self.heading_label.grid(row=0) 

        
        self.user_label=Label(self.quiz_frame, text="Username below: ", font=("Tw Cen MT","16")
        self.user_label.grid(row=1) 

        
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)

       
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="green", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)        


    def name_collection(self):
        name=self.entry_box.get()
        self.quiz_frame.destroy()

if __name__ == "__main__":
    game = Tk()
    game.title("Games") 
    quiz_instance = Quiz(game) 
    game.mainloop()
