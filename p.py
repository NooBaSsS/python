import turtle as t
import random
t.colormode(255)
t.speed(0)
while True:
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    sides = random.randint(3, 16)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(red, green, blue)
    t.begin_fill()
    for i in range(sides):
        t.fd(360 / sides * 2)
        t.rt(360 / sides)
    t.end_fill()
t.done()