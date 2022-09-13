import turtle
from turtle import onscreenclick, mainloop, onkey, listen
turtle = turtle.Turtle()

def line(start,end):
    turtle.penup()
    turtle.goto(start[0],start[1])
    turtle.pendown()
    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    lenght = max(diff_x, diff_y)
    turtle.forward(lenght)

def triangle(start, end):
    turtle.penup()
    turtle.goto(start[0],start[1])
    turtle.pendown()   
    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    width = max(diff_x,diff_y)
    # Draws the figure
    for _ in range(3):
        turtle.forward(width)
        turtle.right(120)

def star(start, end):
    turtle.penup()
    turtle.goto(start[0],start[1])
    turtle.pendown()   
    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    point_size = max(diff_x,diff_y)
    # Draws the figure
    for _ in range(9):
        turtle.forward(point_size)
        turtle.left(130)
        turtle.forward(point_size)
        turtle.right(90)

def circle(start,end):
    turtle.penup()
    turtle.goto(start[0],start[1])
    turtle.pendown()   
    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    radius = max(diff_x,diff_y)
    # Draws the figure
    turtle.circle(radius)

def square(start,end):
    turtle.penup()
    turtle.goto(start[0],start[1])
    turtle.pendown()   
    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    width = max(diff_x,diff_y)
    # Draws the figure
    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)

def rectangle(start, end):
    turtle.penup()
    turtle.goto(start[0],start[1])
    turtle.pendown()   
    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])
    width = max(diff_x,diff_y)
    # Draws the figure
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(width / 2)
        turtle.left(90)

start = None
shape = square

def tap(x,y):
    global start
    if start == None:
        start = x,y
    else:
        end = x,y
        shape(start,end)
        start = None

def change_shape(next_shape):
    global shape
    shape = next_shape

onscreenclick(tap)
onkey(lambda: change_shape(square), "s")
onkey(lambda: change_shape(circle), "c")
onkey(lambda: change_shape(rectangle), "r")
onkey(lambda: change_shape(triangle), "t")
onkey(lambda: change_shape(line), "l")
listen()
mainloop()
