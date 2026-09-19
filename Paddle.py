#a ball and paddle game where the ball bounces up and down and moves back and forth based off of the speed variable and the paddle follows your mouse cursor
#when the ball hits the paddle it should bounce up and change direction sometimes
import pgzrun
import random
HEIGHT = 600
WIDTH = 800
cy = 300
cx = 400
r = 50
d1 = 1
d2 = 0
speed = 2
speed1 = 2
speed2 = 550
sx = 400
sy = 550
move = 0
move1 = 0
def on_mouse_move(pos):
    global d1, d2, speed1, speed2,sx,sy
    sx = (pos[0]-75)
def draw():
    screen.clear()
    screen.draw.filled_circle((cx, cy), r, "white")
    screen.draw.filled_rect(Rect(sx, sy, 150, 50), "white")
def update():
    global cx,cy,r,d1,d2,speed,speed1,speed2,move,move1
    if d1 == 0:
        speed2 = speed * speed1
        speed1 = speed1 * 1.1
        cy = speed2
        if cy >= HEIGHT + (r * 2):
            d1 = 2
            move = 0
        if cy > 450 and sx < cx < (sx + 150):
            d1 = 1
            move = 1
            move1 = random.randrange((0-speed),(speed))
    if d1 == 1:
        speed2 = speed * speed1
        speed1 = speed1 / 1.1
        cy = speed2
        if speed1 <= 1:
            d1 = 0
    if move == 1:
        cx += speed*move1
    if cx < r:
        cx = WIDTH -r
        cy -= 100
    if cx > WIDTH - r:
        cx = r
        cy -= 100
    draw()
pgzrun.go()
