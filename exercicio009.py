"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle
from random import randint

turtle.colormode(255)

turtle = turtle.Turtle()

for c in range(360):
    turtle.color(randint(0,255),randint(0,255),randint(0,255))
    turtle.forward(2)
    turtle.right(1)
