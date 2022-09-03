import turtle
turtle = turtle.Turtle()
"""
for _ in range(360):
    turtle.forward(1)
    turtle.left(1)


turtle.circle(100)
turtle.goto(90,90)

turtle.circle(radius=100,extent=180)


# Desafio 1

turtle.home()
turtle.clear()

turtle.circle(radius=100,steps=3)
turtle.circle(radius=200,steps=4)

# Desafio 2
for _ in range(3):
    turtle.foward(100)
    turtle.right(120)

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
"""
turtle.clear()
# Desafio 3

def reta(comprimento):
    turtle.forward(comprimento)

def triangulo(comprimento):
    for _ in range(3):
        turtle.forward(comprimento)
        turtle.right(120)

def quadrado(comprimento):
    for _ in range(4):
        turtle.forward(comprimento)
        turlte.right(90)

def estrela(comprimento):
    for _ in range(3):
        turtle.forward(comprimento)
        turtle.left(90)
        turtle.forward(comprimento)
        turtle.left(140)

estrela(300)
