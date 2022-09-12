import turtle

t = turtle.Turtle()
def pule(distancia):
    t.penup()
    t.right(90)
    t.forward(distancia)
    t.left(90)
    t.pendown()

def desenhe_triangulo_branco(comprimento):
    t.color("white")
    t.begin_fill()
    for _ in range(3):
        t.forward(comprimento)
        t.right(120)
    t.end_fill()

def desenhe_retangulo_verde(altura,comprimento):
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(comprimento)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

def desenhe_retangulo_branco(altura,comprimento):
    t.color("white")
    t.begin_fill()
    for i in range(2):
        t.forward(comprimento)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

def desenhe_retangulo_vermelho(altura,comprimento):
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.forward(comprimento)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

desenhe_retangulo_verde(180,300)
pule(60)
desenhe_retangulo_branco(60, 300)
pule(20)
desenhe_retangulo_vermelho(20, 300)
t.penup()
t.home()
t.pendown()

t.right(30)
desenhe_triangulo_branco(180)
input()