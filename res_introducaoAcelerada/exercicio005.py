"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle
import random

turtle = turtle.Turtle()
colors = ['red','blue','green','yellow','purple','magenta','pink']
turtle.pensize(3)

for _ in [1, 2, 3]:
    turtle.shape("circle")
    turtle.color(random.choice(colors))
    turtle.forward(155)
    turtle.right(120)
turtle.forward(-20)
for _ in [1, 2, 3, 4]:
    turtle.shape("turtle")
    turtle.color(random.choice(colors))
    turtle.forward(195)
    turtle.right(90)
