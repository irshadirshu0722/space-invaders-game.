
from turtle import Turtle
class Stock:
    def __init__(self):
        self.stocks=[]
        self.createStock()
    def createStock(self):
        x=-600
        y=400
        for i in range(6):
            for j in range(13):
                new_stock = Turtle()
                new_stock.shape("stonedup.gif")
                new_stock.penup()
                new_stock.speed("fastest")
                new_stock.goto(x,y)
                self.stocks.append(new_stock)
                x+=100
            y-=100
            x=-600
    def movedown(self,stock):
        x,y=stock.pos()

        stock.goto(x,y-100)


