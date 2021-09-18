import turtle
import random

def turtle_wmove():
    turtle.seth(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_amove():
    turtle.seth(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_smove():
    turtle.seth(270)
    turtle.forward(50)
    turtle.stamp()

def turtle_dmove():
    turtle.seth(0)
    turtle.forward(50)
    turtle.stamp()
    
def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_wmove,'w')
turtle.onkey(turtle_amove,'a')
turtle.onkey(turtle_smove,'s')
turtle.onkey(turtle_dmove,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
