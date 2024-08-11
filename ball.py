from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 10
        self.set_up()
        self.game_on = True

    def set_up(self):
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def detect_wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def detect_left_miss(self, scoreboard):
        if self.xcor() > 360:
            self.goto(0, 0)
            self.bounce_x()
            scoreboard.r_point()

    def detect_right_miss(self, scoreboard):
        if self.xcor() < -360:
            self.goto(0, 0)
            self.bounce_x()
            scoreboard.l_point()

    def quit_game(self):
        self.game_on = False
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
