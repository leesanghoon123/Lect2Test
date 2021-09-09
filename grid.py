import turtle

a=5
while(a>0):
    turtle.forward(500)
    turtle.left(90)
    a=a-1
turtle.penup()

b=400

turtle.pendown()

while(b>=100):
    turtle.goto(b,0)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    b=b-100

turtle.penup()
turtle.right(90)
c=400

while(c>=100):
    turtle.goto(0,c)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    c=c-100
    
turtle.exitonclick()
