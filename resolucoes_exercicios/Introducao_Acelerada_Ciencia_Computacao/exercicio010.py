"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

turtle = turtle.Turtle()


for _ in range(4):	
	turtle.color('red')	
	turtle.shape('arrow')
	turtle.forward(100)
	turtle.right(90)

turtle.penup()
turtle.backward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.pendown()

for _ in range(4):
	turtle.color('blue')
	turtle.shape('turtle')
	turtle.left(90)
	turtle.forward(100)

turtle.penup()
turtle.forward(20)
turtle.pendown()

for _ in range(4):
	turtle.color('pink')
	turtle.shape('square')
	turtle.forward(100)
	turtle.left(90)

turtle.penup()
turtle.backward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.pendown()

for _ in range(4):
	turtle.color('purple')
	turtle.shape('circle')
	turtle.right(90)
	turtle.forward(100)

turtle.penup()
turtle.backward(110)
turtle.right(90)
turtle.forward(110)
turtle.left(90)
turtle.pendown()

for _ in range(4):
    turtle.color("green")
    turtle.shape("square")
    turtle.forward(240)
    turtle.left(90)
