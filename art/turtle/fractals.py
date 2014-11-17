# encoding: utf-8

import turtle as t

def draw_koch(order, size):
    """
    Similar to the branching pattern
    """
    deg = 60
    if order == 0:
        t.forward(size)
    else:
        draw_koch(order-1, size/3)
        t.left(deg)
        draw_koch(order-1, size/3)
        t.right(2*deg)
        draw_koch(order-1, size/3)
        t.left(deg)
        draw_koch(order-1, size/3)

t.hideturtle()
t.speed(0)
t.up()
size = 350
t.setpos([-size, 0])
t.down()
draw_koch(4, size)
t.done()
