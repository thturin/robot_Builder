import turtle as t

s = t.Screen()
def buttonclick(x,y):
    print("You clicked at this coordinate({0},{1})".format(x,y))


s.setup(width=0.5,height=0.5) #half of the screens dimensions
t.onscreenclick(buttonclick,1)
t.listen()

screen = t.getscreen()
w = screen.window_width()
l = screen.window_height()
print( l,w)
t.speed('fast')
t.bgcolor('black')
t.pencolor('white')
#t.penup()
t.goto(w/2,l/2)
#t.pendown()
a=0
b=0
while True:
    t.forward(a) #distance
    t.right(b) # angle
    a+=2
    b+=1
    if b==210:
        break