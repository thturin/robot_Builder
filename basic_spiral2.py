import turtle as t, random, colorsys

s = t.Screen()
s.setup(0.5,0.5)
s.bgcolor('black')
t.pencolor('white')
t.speed(0) #0 ius the fastest speed you can enter
counter = 0
deg=15
d=0
while True: # turtle will draw the same square for forever
    for i in range (4): #draw the square
        t.forward(100)
        t.right(90)
    #once the square is drawn, modify the angle by n degrees
    t.right(deg)
    counter+=1
    print(counter)
    if counter >=390/deg: #the counter variable creates a full 360 degree circle
        t.forward(50)  #moving onto new square spiral
        counter=0
        d+=1 #this is a counter for the graphic to end it will create 12 spirals
        if d>=12:
            break



