import turtle

t=turtle.Turtle()
t2=turtle.Turtle()
turtle.colormode(255)
s=turtle.Screen()

s.setup(0.75,0.75)

s.bgcolor('black')
t.speed(50)
t2.speed(50)

def flower():
    color = 255
    for i in range(300):
        color = color - 1


        t.circle(190-i,90) #draw a quarter of a circle with a radius of 190-i
        t.left(90)
        t.circle(190-i,90)
        t.left(36)

        t.pencolor((color,color,0))


        t2.pencolor(0, color, 0)
        t2.circle(300-i,90)
        t2.left(90)
        t2.circle(300-i,90)
        t2.left(18) #18 * 5 = 90

        print (i)


flower()



