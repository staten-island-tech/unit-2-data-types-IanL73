import turtle
from turtle import *
t = Turtle()

t.speed(100)

t.shape('turtle')

def square(x,y): # square function. allways set y to 90 so it actually makes a square.
    for i in range(4):
        t.forward(x)
        t.left(y)

def star(x,y): # star function. allways set y to 144 so it actually makes a star.
    for i in range(5):
        t.forward(x)
        t.left(y)

""" for i in range(60): # this makes the cool circle of squares
    square(100,90)
    t.right(5) """

""" def doubleSquares(iRange): # this makes squares of doubling size
    length = 18
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5) """

""" def spiralSquares(irange): # this makes a cool spiral of squares
    length = 15
    for i in range(60):
        square(length,90)
        length = length + 5
        t.right(5)
spiralSquares(60) """

def Constellation(irange):
    length = 30
    for i in range(irange):
        star(length, 144)
        length = length + 5
        t.right(5)
Constellation(60)

turtle.done()