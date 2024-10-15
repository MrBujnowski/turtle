import random
import turtle
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
        x=0

        speed(4000)
        penup()
        backward(300)
        right(90)
        forward(300)
        left(90)
        pendown()
        for i in range(8):
                if i == 2 or i == 4 or i == 6:
                        penup()
                        backward(50)
                        pendown()
                for j in range(8):
                        if (j+x) % 2 == 0:
                                penup()
                                forward(50)
                                pendown()
                                for k in range(25):
                                        right(90)
                                        forward(50)
                                        left(90)
                                        forward(1)
                                        left(90)
                                        forward(50)
                                        right(90)
                                        forward(1)
                        if (j+x) % 2 != 0:
                                for l in range(4):
                                        forward(50)
                                        right(90)
                                        forward(50)
                                        right(90)
                penup()
                backward(400)
                left(90)
                forward(50)
                pendown()
                right(90)
                if x % 2 == 0:
                        penup()
                        forward(50)
                        pendown()
                x+=1


def divny_tvar():

        pencolor("blue")
        speed(1000)
        a = [0,90,180,270]
        while True:
                forward(30)
                right(random.choice(a))

def strom():
        a=250
        b = [90,270]
        speed(1000)
        left(90)
        penup()
        turtle.goto(0,-400)
        pendown()
        while True:
                for i in range(10):
                        forward(a)
                        c = random.choice(b)
                        left(c)
                        forward(a)
                        right(c)
                        a=a/2
                penup()
                turtle.goto(0,-400)
                pendown()
                a=250


mainloop()
