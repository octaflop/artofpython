# encoding: utf-8

import turtle as t
from utils import save_a_png

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

if __name__ == "__main__":
    t.hideturtle()
    t.speed(0)
    t.up()
    size = 350
    t.setup(width=size, height=size)
    t.title("Koch fractals")
    t.setpos([-(size/2), 0])
    t.down()
    draw_koch(4, size)
    save_a_png(t, "img/fractals")
    t.done()
    t.bye()
