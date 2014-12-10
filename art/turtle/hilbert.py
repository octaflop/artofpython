# -*- coding: utf-8 -*-

import turtle as t

iteration = 8
length = 2 

def left_hilbert(length, width):
    if length == 0:
        return
    t.right(90)
    right_hilbert(length - 1, width)
    t.forward(width)
    t.left(90)
    left_hilbert(length - 1, width)
    t.forward(width)
    left_hilbert(length - 1, width)
    t.left(90)
    t.forward(width)
    right_hilbert(length - 1, width)
    t.right(90)

def right_hilbert(length, width):
    if length == 0:
        return
    t.left(90)
    left_hilbert(length - 1, width)
    t.forward(width)
    t.right(90)
    right_hilbert(length - 1, width)
    t.forward(width)
    right_hilbert(length - 1, width)
    t.right(90)
    t.forward(width)
    left_hilbert(length - 1, width)
    t.left(90)

if __name__ == '__main__':
    # setup
    # t.hideturtle()
    t.speed(0)
    # t.up()
    # t.setpos([-800, 0])
    # t.setup(width=800, height=800)
    t.title("hilbert")
    # draw
    t.down()
    left_hilbert(iteration, length)
    # bye!
    t.done()
    t.bye()


