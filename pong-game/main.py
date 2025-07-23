from tkinter.tix import Balloon
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# right_paddle = Turtle("square")
# right_paddle.penup()
# right_paddle.color("white")
# right_paddle.shapesize(stretch_wid=5, stretch_len=1)
# right_paddle.goto(350, 0)
#
# def move_up():
#      new_y = right_paddle.ycor() + 20
#      right_paddle.goto(right_paddle.xcor(), new_y)
#
# def move_down():
#     new_y = right_paddle.ycor() - 20
#     right_paddle.goto(right_paddle.xcor(), new_y)

screen.listen()

screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)

screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(ball.speed1)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l()

    #Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r()

screen.exitonclick()