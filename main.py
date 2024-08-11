from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

turtle = Turtle()
# screen setup
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# left and right paddle
left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)
screen.update()

# moving the paddle
screen.listen()
screen.onkey(key="Up", fun=left_paddle.up)
screen.onkey(key="Down", fun=left_paddle.down)
screen.onkey(key="w", fun=right_paddle.up)
screen.onkey(key="s", fun=right_paddle.down)

# create a ball in center of the screen
ball = Ball()

# checking if game is on
game_on = True
while game_on:
    ball.move()
    time.sleep(0.1)
    screen.update()
    ball.detect_wall_collision()
    left_paddle.detect_collision(ball)
    right_paddle.detect_collision(ball)

screen.exitonclick()
