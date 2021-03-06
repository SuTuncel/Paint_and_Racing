from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def spaces():
    timmy.penup()
    timmy.forward(20)
    timmy.pendown()


def clear():
    timmy.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="p", fun=spaces)
screen.onkey(key="c", fun=clear)

screen.exitonclick()