from turtle import Turtle,Screen
import random
window=Screen()
choice=window.textinput("Turtles speed","Choose the fastest turtle\n red, green, blue")
sam=Turtle()
mike=Turtle()
john=Turtle()
sam.shape("turtle")
mike.shape("turtle")
john.shape("turtle")
sam.color("red")
sam.penup()
mike.color("green")
mike.penup()
john.color("blue")
john.penup()
window.setup(width=800,height=800)
sam.goto(-380,0)
mike.goto(-380,150)
john.goto(-380,-150)
steps=[1*2,2*2,3*2,4*2,5*2]
window.title("Turtles")

color=""
while True:
    sam.forward(random.choice(steps))
    mike.forward(random.choice(steps))
    john.forward(random.choice(steps))
    if sam.xcor()>380 :
        color=sam.pencolor()
        break
    elif mike.xcor()>380:
        color=mike.pencolor()
        break
    elif john.xcor()>380:
        color=john.pencolor()
        break
window.clearscreen()
turtle=Turtle()
turtle.hideturtle()
turtle.color("white")
turtle.penup()

if choice==color:
    window.bgcolor("black")
    turtle.goto(0,100)
    turtle.write(f"Congratulations",font=("arial",40,"bold"),align="center")
    turtle.goto(0,0)
    turtle.write(f"You won.....",font=("arial",40,"bold"),align="center")
    
else:
    window.bgcolor("red")
    turtle.goto(0,100)
    turtle.write(f"Opps",font=("arial",40,"bold"),align="center")
    turtle.goto(0,0)
    turtle.write(f"You lost....",font=("arial",40,"bold"),align="center")
    
window.exitonclick()