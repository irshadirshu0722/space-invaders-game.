

from turtle import Turtle
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()


    def gameoverhit(self):
        self.goto(-500, 0)
        self.color("red")

        self.write("Game Over :  You failed(Stone hit spaceship) " ,font=("Arial",40))
    def gameoverbulletover(self):
        self.goto(-500, 0)
        self.color("red")

        self.write("Game Over :  You failed(Bullet is not available) " ,font=("Arial",40))

    def won(self):
        self.goto(-250, 0)
        self.color("green")

        self.write("Game Over :  You won " ,font=("Arial",40))

