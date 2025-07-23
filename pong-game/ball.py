from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.change_in_y = 10
        self.change_in_x = 10
        self.speed1 = 0.1

    def move(self):
        new_y = self.ycor() + self.change_in_y
        new_x = self.xcor() + self.change_in_x
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.change_in_y *= -1

    def bounce_x(self):
        self.change_in_x *= -1
        self.speed1 *= 0.9

    def reset_position(self):
        self.change_in_x *= -1
        self.speed1 = 0.1
        self.goto(0,0)
