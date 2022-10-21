import turtle as t
import math
t.speed(0)
def draw_house(walls_x, walls_y, walls_width, walls_height, walls_color, door_width, door_height, door_color, roof_height, roof_color):
    """
    walls_x - левый нажний угол стен
    walls_y - левый нажний угол стен
    walls_width - ширина стен
    walls_height - высота стен
    walls_color - цвет стен (hex)
    door_width - ширина двери
    door_height - высота двери
    door_color - цвет двери "hex"
    door_x - левый нижний угол двери
    door_y - левый нижний угол двери
    roof_height - высота крыши
    roof_color - цвет крыши
    """
    door_x = walls_x + (walls_width / 2 - door_width / 2)
    door_y = walls_y
    roof_x = walls_x
    roof_y = walls_y + walls_height
    roof_side = math.sqrt(roof_height ** 2 + (walls_width / 2) ** 2)
    roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))
    draw_walls(walls_x, walls_y, walls_width, walls_height, walls_color)
    draw_door(door_x, door_y, door_width, door_height, door_color)
    draw_roof(roof_x, roof_y, roof_side, roof_angle, roof_color)

def draw_walls(walls_x, walls_y, walls_width, walls_height, walls_color):
    t.penup()
    t.goto(walls_x, walls_y)
    t.pendown()
    t.fillcolor(walls_color)
    t.begin_fill()
    for i in range(2):
        t.fd(walls_width)
        t.lt(90)
        t.fd(walls_height)
        t.lt(90)
    t.end_fill()
def draw_door(door_x, door_y, door_width, door_height, door_color):
    t.penup()
    t.goto(door_x, door_y)
    t.pendown()
    t.fillcolor(door_color)
    t.begin_fill()
    for i in range(2):
        t.fd(door_width)
        t.lt(90)
        t.fd(door_height)
        t.lt(90)
    t.end_fill()
def draw_roof(roof_x, roof_y, roof_side, roof_angle, roof_color):
    t.penup()
    t.goto(roof_x, roof_y)
    t.pendown()
    t.fillcolor(roof_color)
    t.begin_fill()
    t.lt(roof_angle)
    t.fd(roof_side)
    t.rt(roof_angle * 2)
    t.fd(roof_side)
    t.end_fill()
draw_house(-100, 0, 200, 150, "#ff0000", 70, 90, "#000000", 50, "#004400")
t.done()