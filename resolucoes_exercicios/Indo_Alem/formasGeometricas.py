import turtle
turtle = turtle.Turtle()

def movimenta(comprimento):
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(comprimento)
    turtle.pendown()

def reta(comprimento):
    turtle.forward(comprimento)

def triangulo(comprimento):
    for _ in range(3):
        turtle.forward(comprimento)
        turtle.right(120)

def quadrado(comprimento):
    for _ in range(4):
        turtle.forward(comprimento)
        turtle.left(90)

def retangulo(comprimento):
    for _ in range(2):
        turtle.forward(comprimento / 2)
        turtle.left(90)
        turtle.forward(comprimento)
        turtle.left(90)

def estrela(comprimento):
    for _ in range(9):
        turtle.forward(comprimento)
        turtle.left(130)
        turtle.forward(comprimento)
        turtle.right(90)

def circulo(raio):
    turtle.circle(raio)

