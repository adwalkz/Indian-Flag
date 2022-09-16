import turtle

def rectangle(t):
    for i in range(2):
        t.fd(200)
        t.lt(90)
        t.fd(50)
        t.lt(90)


tur=turtle.Turtle()

tur.ht()

win=turtle.Screen()
win.bgcolor("cyan")

tur.speed(10)

tur.pu()
tur.lt(90)
tur.fd(100)
tur.rt(90)
tur.pd()

tur.begin_fill()
tur.color("black","orange")
rectangle(tur)
tur.end_fill()

tur.pu()
tur.rt(90)
tur.fd(50)
tur.rt(270)
tur.pd()

tur.begin_fill()
tur.color("black","white")
rectangle(tur)
tur.end_fill()

tur.pu()
tur.rt(90)
tur.fd(50)
tur.rt(270)
tur.pd()

tur.begin_fill()
tur.color("black","green")
rectangle(tur)
tur.end_fill()

tur.begin_fill()
tur.color("black","brown")

tur.rt(90)
tur.fd(200)
tur.rt(90)
tur.fd(10)
tur.rt(90)
tur.fd(350)
tur.rt(90)
tur.fd(10)
tur.rt(90)
tur.fd(350)

tur.rt(90)
tur.fd(80)
tur.rt(90)
tur.fd(40)
tur.rt(90)
tur.fd(160)
tur.rt(90)
tur.fd(40)
tur.rt(90)
tur.fd(80)

tur.end_fill()

tur.pu()
tur.rt(90)
tur.fd(255)
tur.rt(90)
tur.fd(100)
tur.pd()


tur.color("blue")

tur.circle(20)

tur.lt(90)
tur.fd(40)

tur.rt(180)
tur.fd(20)

tur.rt(90)
tur.fd(20)

tur.rt(180)
tur.fd(40)

tur.rt(180)
tur.fd(20)
tur.lt(45)
tur.fd(20)

tur.rt(180)
tur.fd(40)

tur.rt(180)
tur.fd(20)
tur.rt(75)
tur.fd(20)

tur.rt(180)
tur.fd(40)

tur.up()
tur.rt(180)
tur.fd(140)
tur.rt(80)
tur.fd(20)

tur.color("black","yellow")
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.lt(100)
tur.pd()

tur.color("white")

for i in range(120):
    tur.fd(3.3)
    tur.lt(1.7)

for i in range(180):
    tur.fd(1)
    tur.rt(1.2)
