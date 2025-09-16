import turtle
from turtle import *

t = Turtle()

t.speed(0)

for i in range(4):
    t.forward(100)
    t.left(90)

def triangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)


def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)

#for i in range(60):
    square(100)
    t.right(5)

sidelength = 100
rotate = 90

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
#triangle(100,90)

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
#doubleSquares(5)

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
#addSquares(5)

def bigSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        t.right(5)
        length += 5
bigSquares(60)

def star(iRange):
    length



    
    