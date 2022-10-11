import turtle as t
import math
t.color("gray")
t.shape("turtle")
walls_width = 300
walls_hight = 100
door_width = 40
door_height = 50
roof_height = 150
roof_side = math.sqrt(roof_height ** 2 + (walls_width / 2) ** 2)
roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))
print(roof_angle)
t.speed(0)
for i in range(2):
    t.fd(walls_width)
    t.left(90)
    t.fd(walls_hight)
    t.left(90)
t.fd(walls_width / 2 - door_width / 2)
for i in range(2):
    t.fd(door_width)
    t.left(90)
    t.fd(door_height)
    t.left(90)
t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_hight)
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.done()