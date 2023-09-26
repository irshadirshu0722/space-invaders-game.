
from spaceShip import Spaceship
from fire import Bullet
from turtle import Turtle,Screen
from PIL import Image
from time import sleep
from stock import Stock
from gameOver import GameOver
from totalbulletboard import BulletBoard
screen = Screen()
screen.title("space invaders game.")


image_path = 'stone.gif'
original_image = Image.open(image_path)
new_size = (50, 50)  # Adjust the size as needed
resized_image = original_image.resize(new_size)
resized_image_path = 'stonedup.gif'
resized_image.save(resized_image_path)


screen.setup(1400,900)
screen.addshape("spaceship.gif")
screen.addshape("bullet.gif")
screen.addshape("hitdup.gif")
screen.addshape("stockdup.gif")
screen.addshape("stonedup.gif")

screen.tracer(0)

ship = Spaceship()
stock = Stock()
gameover = GameOver()
totalbullet = BulletBoard()
screen.listen()

bullets = []

key_states = {'Left' : False,'Right': False, 'Up': False}
hitstones=[]
hitstonedic={}

def firebullet():
    if key_states["Right"] and key_states["Up"]:
        addBullet()
        ship.moveRight()
        totalbullet.decriment()
    elif key_states["Left"] and key_states["Up"]:
        addBullet()
        ship.moveLeft()
        totalbullet.decriment()
    elif key_states["Left"]:
        ship.moveLeft()
    elif key_states["Right"]:
        ship.moveRight()
    else:
        addBullet()
        totalbullet.decriment()



def key_press(key):
    if key in key_states:
        key_states[key] = True
        firebullet()


def key_release(key):
    if key in key_states:
        key_states[key] = False



def addBullet():
    x,y=ship.pos()
    bullet = Bullet(x,y+50)
    bullets.append(bullet)



screen.onkeypress(lambda :key_press("Left"),"Left")
screen.onkeypress(lambda :key_press("Right"),"Right")
screen.onkeypress(lambda :key_press("Up"),"Up")


screen.onkeyrelease(lambda :key_release("Right"),"Right")
screen.onkeyrelease(lambda :key_release("Left"),"Left")
screen.onkeyrelease(lambda :key_release("Up"),"Up")




is_gameon=True
move_status = 0
is_stock_hit=False

while is_gameon:
    screen.update()
    sleep(0.05)

    if is_stock_hit:
        gameover.gameoverhit()
        is_gameon=False

    for i,bullet in enumerate(bullets):
        bullet.moveup()
        if bullet.pos()[1] >500:
            bullets.pop(i)

    if len(stock.stocks)==0:
        gameover.won()
        is_gameon = False

    if totalbullet.no_of_bullet<=0:
        gameover.gameoverbulletover()

        is_gameon = False
    for hitstone in hitstones:
        if hitstone in hitstonedic:
            hitstonedic[hitstone]+=1
            if hitstonedic[hitstone]==2:
                hitstone.hideturtle()
                hitstones.remove(hitstone)


    for st in stock.stocks:
        for bullet in bullets:

            # print("enter",bullet.distance(st))
            if bullet.distance(st)<30:
                st.shape("hitdup.gif")

                hitstones.append(st)
                hitstonedic[st]=0
                stock.stocks.remove(st)
                bullet.hideturtle()
                bullets.remove(bullet)

    move_status+=1
    if move_status%100==0:
        for st in stock.stocks:
            stock.movedown(st)
            if st.pos()[1]<-350:
                is_stock_hit=True

















screen.mainloop()