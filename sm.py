import turtle as t
t.speed(0)
t.color("#6699FF")
t.fillcolor("#6699FF")
r = 50
for i in range(3):
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.fd(r * 2)
    t.setheading(0)
    t.pendown()
    r /= 2
t.done()