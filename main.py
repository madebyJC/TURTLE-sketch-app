from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)


def turn_left():
    left_heading = t.heading() + 10
    t.setheading(left_heading)


def turn_right():
    right_heading = t.heading() - 10
    t.setheading(right_heading)


def turtle_home():
    t.home()
    t.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=turtle_home)

screen.exitonclick()
