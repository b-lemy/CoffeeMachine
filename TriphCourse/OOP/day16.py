# import turtle

#or
from turtle import Turtle, Screen

lemy = Turtle()
lemy.shape('turtle')
lemy.color('red')
lemy.speed(50)
lemy.forward(100)
print(lemy)

for i in range(36):
    lemy.circle(150)
    lemy.left(10)
lemy.color('green')

for i in range(36):
    lemy.circle(100)
    lemy.left(10)

lemy.color("red")
for i in range(36):
    lemy.circle(80)
    lemy.left(10)

lemy.color("yellow")

for i in range(36):
    lemy.circle(60)
    lemy.left(10)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()









