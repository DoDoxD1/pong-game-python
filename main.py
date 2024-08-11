from turtle import Turtle, Screen
from paddle import Paddle

turtle = Turtle()
# screen setup
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# left paddle
left_paddle = Paddle()
left_paddle.create_left_paddle()
right_paddle = Paddle()
right_paddle.create_right_paddle()
screen.update()

# moving the paddle
screen.listen()
screen.onkey(key="Up", fun=left_paddle.up)
screen.onkey(key="Down", fun=left_paddle.down)
screen.onkey(key="w", fun=right_paddle.up)
screen.onkey(key="s", fun=right_paddle.down)

screen.exitonclick()
