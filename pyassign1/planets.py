"""planets.py: It could imitate the motions of
               the inner 6 planets of the solar
               system.(circle orbits, radius
               based on real sizes)

__author__ = "Wangtie"
__pkuid__  = "1800011811"
__email__  = "1800011811@pku.edu.cn"
"""

import turtle
import math
r_earth = 30  # alter this to put the orbits in screen#
t0 = turtle.Turtle()
t0.color('yellow')
t0.shape('circle')
t0.stamp()
# the sun #

t1 = turtle.Turtle()
t1.color('blue')
t1.shape('circle')
t1.shapesize(0.19, 0.19)
t1.penup()
t1.goto(0, -0.38 * r_earth)
t1.pendown()
# mercury #

t2 = turtle.Turtle()
t2.color('orange')
t2.shape('circle')
t2.shapesize(0.3, 0.3)
t2.penup()
t2.goto(0, -0.52 * r_earth)
t2.pendown()
# venus #

t3 = turtle.Turtle()
t3.color('green')
t3.shape('circle')
t3.shapesize(0.5, 0.5)
t3.penup()
t3.goto(0, -1 * r_earth)
t3.pendown()
# earth #

t4 = turtle.Turtle()
t4.color('red')
t4.shape('circle')
t4.shapesize(0.26, 0.26)
t4.penup()
t4.goto(0, -1.52 * r_earth)
t4.pendown()
# mars #

t5 = turtle.Turtle()
t5.color('brown')
t5.shape('circle')
t5.shapesize(5.5, 5.5)
t5.penup()
t5.goto(0, -5.2 * r_earth)
t5.pendown()
# jupiter #

t6 = turtle.Turtle()
t6.color('gray')
t6.shape('circle')
t6.shapesize(4.72, 4.72)
t6.penup()
t6.goto(0, -9.54 * r_earth)
t6.pendown()
# saturn #

for m in range(200):
    b = 15  # speed modifier of circling#
    t1.speed(0)
    t2.speed(0)
    t3.speed(0)
    t4.speed(0)
    t5.speed(0)
    t6.speed(0)
    t1.circle(0.38 * r_earth, b * (1/0.23))
    t2.circle(0.52 * r_earth, b * (1/0.37))
    t3.circle(r_earth, b * 1)
    t4.circle(1.52 * r_earth, b * (1/1.87))
    t5.circle(5.2 * r_earth, b * (1/11.86))
    t6.circle(9.54 * r_earth, b * (1/29.47))
