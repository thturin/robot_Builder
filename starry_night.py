import turtle as t
import colorsys as c
import random

"""hacks and tweaks
draw a constellation, stars and planets goto not random

"""

s = t.Screen()
print(s.screensize())
l = t.window_height()
w = t.window_width()
s.setup(.5,.5)
t.bgcolor('black')
t.speed(0)
star_population=500



def draw_star(points,angle,size): #draw the star
    t.penup()#don't show linewhen moving to star position
    t.goto(random.randint(w*(-1),w),random.randint(l*(-1),l)) #find a random position that is the range of full width and length
    t.pendown() #now draw
    t.color(c.hsv_to_rgb(random.randint(1, 360) / 360, 1, 1))  # hue color
    t.begin_fill() #begin to fill the shape that is being draw now
    for i in range(points): #create the star
        t.forward(size)
        t.right(angle)
    t.end_fill() #end the filling of the drawing now

def draw_planet(col,x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


################################################main function############################################################
for i in range(star_population): #this is where the star function is called
    points = random.randint(7,10)
    angle = 180 - (180 / points) #the angle depends on the number of points the start has, the more points, the smaller the angle
    size=random.randint(1,50)
    draw_star(points,angle,size)
    if(i%5==0): #every 5 loops, draw a planet
        draw_planet(c.hsv_to_rgb(random.randint(1, 360) / 360, 1, 1),random.randint(w*(-1),w),random.randint(l*(-1),l))