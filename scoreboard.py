from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.level = 1
        self.refresh()

    #Removing former scoreboard and writing a new one
    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}",align=ALIGNMENT, font=FONT)

    #Adding score
    def level_up(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=FONT)
