



from turtle import Turtle
class BulletBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.no_of_bullet = 150
        self.hideturtle()
        self.penup()
        self.goto(x=570,y=-420)
        self.updatebullet()


    def updatebullet(self):
        self.clear()
        self.write(f"{self.no_of_bullet}" ,font=("Arial",40))
    def decriment(self):
        print("enter")
        if self.no_of_bullet==0:
            return
        self.no_of_bullet-=1
        self.updatebullet()

