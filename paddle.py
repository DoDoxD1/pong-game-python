from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)

    def create_left_paddle(self):
        self.goto(x=350, y=0)

    def create_right_paddle(self):
        self.goto(x=-350, y=0)

    def up(self):
        self.forward(20)
        Screen().update()

    def down(self):
        self.backward(20)
        Screen().update()
