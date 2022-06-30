import turtle as t
import random

def buttonclick(x,y):
    print("You clicked at this coordinate({0},{1})".format(x,y))

s = t.Screen()
s.colormode(255)
s.setup(width=0.5,height=0.5) #half of the screens dimensions
t.onscreenclick(buttonclick,1)
t.listen()
print('The canvas size is {0} x {1} '.format(s.window_width(),s.window_height()))

t.speed('fast')
t.bgcolor('black')
t.pencolor('white')
t.goto(0,100)
#t.pendown()
a=0
b=0
while True:
    t.forward(a) #distance
    t.right(b) # angle
    a+=2
    b+=1
    t.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    if b==210:
        break

