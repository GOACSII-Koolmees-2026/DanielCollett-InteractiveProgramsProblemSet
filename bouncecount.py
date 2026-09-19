import pgzrun
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
count = 0
color = "black"
def on_mouse_down():
    global d1, d2, speed1, speed2, color
    color = "white"
def on_mouse_up():
    global d1, d2, speed1, speed2, color
    color = "black"
def draw():
    screen.clear()
    screen.draw.filled_circle((cx, cy), r, "white")
    screen.draw.text(str(count), (50, 30), color=color)
def update():
    global cx,cy,r,d1,d2,speed,speed1,speed2,count,color
    if d1 == 0:
        speed2 = speed * speed1
        speed1 = speed1 * 1.1
        cy = speed2
        if cy >= HEIGHT - r:
            d1 = 1
            count += 1
    if d1 == 1:
        speed2 = speed * speed1
        speed1 = speed1 / 1.1
        cy = speed2
        if speed1 <= 1:
            d1 = 0
    draw()
pgzrun.go()