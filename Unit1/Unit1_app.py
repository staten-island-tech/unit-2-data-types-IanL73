""" # def defines a function
# inside the parenthesis are the inputs / arguments
def add(x,y):
    print(x + y)
    # print(x + y)
    # return creates an output for the function

    return(x + y)

add(5,6) """

import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

""" def size(x):    # this creates a square
    t.forward(x / 2)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x / 2)
size(350) """

""" def size (x):   # this makes an equilateral triangle
    t.forward(x / 2)
    t.left (120)
    t.forward(x)
    t.left (120)
    t.forward(x)
    t.left (120)
    t.forward(x / 2)
size(600) """

""" def right():    # this makes a right triangle
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right() """

""" def size():    # this creates a  rectangle with a width of 100px and a length of 125px
    t.forward(50)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(50)
size() """

turtle.done()