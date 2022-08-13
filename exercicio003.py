"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

turtle = turtle.Turtle()
turtle.pensize(3)
turtle.shape('arrow')

for quadrados in range(2):
	for color in ['black','pink','blue','red']:
		turtle.color(color)
		turtle.forward(100)
		turtle.right(90)
	turtle.penup()
	turtle.forward(200)
	turtle.pendown()

