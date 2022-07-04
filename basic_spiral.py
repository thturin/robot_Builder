import turtle as t
import colorsys as c
import random

"""
Upgrades 

have the program change shapes 
if square -->
if circle -->
"""

def draw_circle(size,angle,shift):
    t.pencolor(c.hsv_to_rgb(random.randint(1,360)/360,1,1))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size+5,angle+1,shift+1) #the function calls itself -> recursive function

#1 setup
s = t.Screen()
s.setup(.5,.5)
t.bgcolor('black')
t.speed(5)
t.pensize(1)
t.pencolor('red')


draw_circle(10,0,1)