# -*- coding: utf-8 -*-

import turtle as t

iteration = 6
length = 6

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

left_hilbert(iteration, length)

