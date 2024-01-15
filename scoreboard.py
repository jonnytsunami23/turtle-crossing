from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210,240)
        self.level = 0
        self.write(f"Level : {self.level}", align="center", font=FONT)


    def update_score(self):
        self.clear()
        self.level +=1
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)