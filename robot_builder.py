
"""Project No. Robot Builder """

#1 import turtle module and name it t
import turtle as t

#2 create a rectangle function
def rectangle(horizontal, vertical, color):
    t.pendown() # start drawing
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    #one interation of this for loop below will make hald of a rectangle L -shape
    for i in range (1,3):  #will run twice 1,2
        t.forward(horizontal) #will go however far you set horizontal var to
        t.right(90) #parameter is an angle so we are turning clockwise 90 deg
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()



#3 set the background
t.speed('slow')
t.bgcolor('Dodger blue')

#4 draw the feet
t.penup() ######
t.goto(-100,-150)  #III quadrant
rectangle(50,20,'blue')
t.goto(-30,-150) # III quadrant
rectangle(50,20,'blue')

#5 draw the legs
t.goto(-25,-50) #III quadrant
rectangle(15, 100, 'grey')
t.goto(-55,-50) #III quadrant
rectangle(-15, 100, 'grey')

#6 draw the legs
t.goto(-90,100)
rectangle(100,150,'red')

#7 draw the arms
t.goto(-150,70) #IV quadrant upper right arm
rectangle(60, 15, 'grey')
t.goto(-150, 110) #lower right arm
rectangle(15, 40, 'grey')
t.goto(10, 70) #I quadrant upper left  arm
rectangle(60, 15, 'grey')
t.goto(55, 110) #lower left arrm
rectangle(15, 40, 'grey')

# 8 draw the neck
t.goto(-50, 120)
rectangle(15, 20, 'grey')

#9 head
t.goto(-85,170)
rectangle(80,50,'red')