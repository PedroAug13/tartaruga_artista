from turtle import Turtle, onkey, listen, mainloop

turtle = Turtle()
turtle.shape("circle")

def up():
    y_atual = turtle.ycor()
    novo_y = y_atual + 5
    turtle.sety(novo_y)

def down():
    y_atual = turtle.ycor()
    novo_y = y_atual - 5
    turtle.sety(novo_y)

def right():
    x_atual = turtle.xcor()
    novo_x = x_atual + 5
    turtle.setx(novo_x)

def left():
    x_atual = turtle.xcor()
    novo_x = x_atual - 5
    turtle.setx(novo_x)

onkey(up,"Up")
onkey(down,"Down")
onkey(left,"Left")
onkey(right,"Right")
listen()
mainloop()
