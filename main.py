from random import *
from turtle import *

shape("turtle")


def slunicko():
        bgcolor("black")
        pencolor("yellow")
        width(10)
        i = 0
        f = 100
        for i in range(36):
                speed(40)
                forward(f)
                left(10)
                backward(f)
                right(20)
                forward(20)

def sachovnice():

        speed(4000)
        penup()
        backward(300)
        right(90)
        forward(300)
        left(90)
        pendown()
        for k in range(8):
                for i in range(8):
                        for j in range(4):
                                forward(50)
                                right(90)
                        forward(50)
                backward(400)
                left(90)
                penup()
                forward(50)
                pendown()
                right(90)



def divnyTvar():

        a=100
        pencolor("blue")
        forward(a)



mainloop()

