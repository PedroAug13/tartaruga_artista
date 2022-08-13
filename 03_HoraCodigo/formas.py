import turtle

turtle = turtle.Turtle()

# definindo as funções
def triangulo():
    for _ in range(3):
        turtle.forward(120)
        turtle.right(120)

def desenhe_forma():
    for _ in range(3):
        turtle.forward(75)
        turtle.right(120)

def quadrado():
    for _ in range(4):
        turtle.forward(25)
        turtle.right(90)

def octogono():
    for _ in range(8):
        turtle.forward(25)
        turtle.right(45)

def pule(pixels):
    turtle.penup()
    turtle.forward(pixels)
    turtle.pendown()

# Aqui é o código principal
for _ in range(6):
    for _ in range(2):
        for _ in range(1):
            triangulo()
            pule(75)
        pule(-25)
        turtle.right(60)
        pule(25)
        turtle.right(120)
    pule(-25)
    turtle.left(60)
    pule(50)
    turtle.right(60)
