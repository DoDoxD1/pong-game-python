from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x=x, y=y)

    def detect_collision(self, ball):
        if self.distance(ball) < 50 and (ball.xcor() > 320 or ball.xcor() < -320):
            ball.bounce_x()

    def up(self):
        if self.ycor() < 230:
            self.forward(20)

    def down(self):
        if self.ycor() > -230:
            self.backward(20)
