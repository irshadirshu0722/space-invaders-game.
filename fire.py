from turtle import Turtle

class Bullet(Turtle):
    def __init__(self,x,y):
        super().__init__()

        self.shape("bullet.gif")
        self.penup()
        self.speed("fastest")
        self.goto(x, y)






    def moveup(self):
        x,y = self.pos()
        self.goto(x,y+20)






