"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
6. Toogle fill/no fill
7. Remove repeted code in figure functions
template method -> design patterns for OO

"""

from turtle import setup, onscreenclick, listen, onkey, undo, done, up, goto, down, mainloop, begin_fill, end_fill, forward, left, right, circle, color, pensize
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(360):
        forward(end.x - start.x)
        left(1)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    lenght = end.x - start.x
    for count in range(2):
        forward(lenght)
        left(90)
        forward(lenght / 2)
        left(90)
    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()
    undo()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        # state['start'] = vector(x, y)
        store('start', vector(x, y))
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        # state['start'] = None
        store('start', None)

def store(key, value):
    """Store value in state at key."""
    state[key] = value

def increase_pensize():
    state['size'] = state['size'] + 1
    pensize(state['size'])

def decrease_pensize():
    size = state['size']
    if (size > 1): 
        size = size - 1
        pensize(size)
        state['size'] = size

state = {'start': None, 'shape': line, 'size': 1}

setup(1600, 900)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(increase_pensize, 'Up')
onkey(decrease_pensize, 'Down')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
mainloop()
