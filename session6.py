import turtle
from math import sin,cos,pi,tau

t = turtle.Turtle()

def polyline(t,n,length,angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)


def polygon(t, n, l):
    angle = 360 / n
    polyline(t,n,l,angle)

def arc(t, r, angle):
    arc_length = 2* pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t,r,360)

def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        t.left(180-angle)

def flower(t,r,n,angle):
    for i in range(n):
        petal(t,r,angle)
        t.left(360/n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

#flower(t,300,20,20)
move(t, 100)
t.left(90)
#circle(t, 100)
flower(t,200,4,90)