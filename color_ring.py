import turtle as t
import colorsys as c

s=t.Screen()
s.setup(.75,.75)
t.bgcolor('black')
t.setpos(-90,80)
t.tracer(100)
t.pensize(1)
hue=0.0

#t.hideturtle()
t.speed('slowest')
########################

for i in range (500):
    color = c.hsv_to_rgb(hue,1,1)  #(h,s,v)
    #hsv describes a color in terms of hue, given as degrees, combined with a saturation and a value, both represented as percentages
    t.pencolor(color)
    t.forward(200)
    t.right(91)
    t.circle(50-i)
    hue +=0.009

t.exitonclick()