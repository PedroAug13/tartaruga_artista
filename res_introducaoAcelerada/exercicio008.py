"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(2)

colors = ['red','magenta','lime','black','purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (37):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(180)
    turtle.backward(180)
    turtle.right(10)

