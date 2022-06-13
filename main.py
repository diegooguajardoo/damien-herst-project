import random
from turtle import Turtle, Screen
from colors import extract_colors

timmy = Turtle()
timmy.shape("circle")
timmy.speed("slow")
timmy.penup()
timmy.setposition(-200, -200)

screen = Screen()
screen.colormode(255)

color_list = extract_colors(8)


def get_color():
    return random.choice(color_list)


def new_line(dots):
    for i in range(dots):
        timmy.stamp()
        timmy.forward(45)
        timmy.color(get_color())
    x = timmy.xcor()
    y = timmy.ycor()
    timmy.setposition((-200, y+50))


def painting(rows, height):
    for i in range(rows):
        new_line(10)



painting(10, 20)

screen = Screen()
screen.exitonclick()
