import pgzrun
HEIGHT = 600
WIDTH = 800
x = 400
y = 300
r = 10
size = 3
speed = 2
def on_key_down():
    global x,y,r,size
    size = 0
def on_key_up():
    global x,y,r,size
    size = 1
def draw():
    screen.clear()
    screen.draw.filled_circle((x, y), r, "white")
def update():
    global x,y,r,size
    if size == 1:
        if r > 10:
            r -= speed
    if size == 0:
        if r < 150:
            r += speed
    draw()
pgzrun.go()