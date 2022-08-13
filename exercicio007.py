"""
Exercicios:

1) Mude a distancia entre as lentes dos óculos
2) Mude o tamanho das lentes
"""

import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(200)

turtle.backward(300)
turtle.right(90)

for _ in range(3):
  turtle.forward(200)
  turtle.left(90)

