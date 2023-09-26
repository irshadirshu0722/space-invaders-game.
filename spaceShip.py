from turtle import Turtle
class Spaceship(Turtle):
    def __init__(self):
        super().__init__()



        self.shape("spaceship.gif")
        self.shapesize(30,30)
        self.penup()
        self.speed("fastest")
        self.goto(0,-400)
    def moveLeft(self):
        x,y=self.pos()
        self.goto(x-20,y)
    def moveRight(self):
        x,y=self.pos()
        self.goto(x+20,y)



