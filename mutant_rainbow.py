import random, turtle as t, colorsys as c

#t.Screen().colormode(255) if you turn this on, some issue happens with color

def get_line_length():
    choice = input('Enter line length (long, medium , short): ')
    if choice == 'long':
        line_length=250
    elif choice == 'medium':
        line_length = 200
    else:
        line_length=100
    return line_length

def get_line_width():
    choice = input('Enter line width (superthick, thick, thin): ')
    if choice == 'superthick':
        line_width = 40
    elif choice == 'thick':
        line_width = 25
    else:
        line_width=10
    return line_width


def inside_window():
    left_limit = (-t.window_width()/2) + 100
    right_limit = (t.window_width()/2) - 100
    top_limit = (t.window_height()/2)-100
    bottom_limit = (-t.window_height()/2)+100
    (x,y) = t.pos() #program retrieves current (x,y) coordinates of turtle object
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit #inside is a boolean operator it will be either true or false depending on (x,y)'s position
    return inside #the function will return a boolean value

def move_turtle(line_length):

    t.pencolor(c.hsv_to_rgb(random.randint(1,360)/360,1,1))

    if inside_window(): #if the function inside_window() returns a true value ie. the turtle is inside the paramter we specified
        angle = random.randint(0,180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)  #if the function returns a false statement, the turtle is outside or has hit the perimeter of the screen and will go backwards

line_length = get_line_length()
line_width = get_line_width()
t.bgcolor('black')
t.speed(0)
t.pensize(line_width)

while True:
    move_turtle(line_length)

