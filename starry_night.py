import turtle as t
import colorsys as c
import random
s = t.Screen()
print(s.screensize())
l = t.window_height()
w = t.window_width()
s.setup(.5,.5)
t.bgcolor('black')
t.pencolor('white')
t.speed(20)
size = 30



def draw_star(points,angle):
    t.pencolor(c.hsv_to_rgb(random.randint(1,360)/360,1,1))
    t.penup()
    t.goto(random.randint(w*-1,w),random.randint(l*-1,l))
    t.pendown()
    for i in range(points):
        t.forward(size)
        t.right(angle)


for i in range(500):
    points = random.randint(4,10)
    angle = 180 - (180 / points)
    draw_star(points,angle)