from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-160, -100, -40, 20, 80, 140]
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
            break
        else:
            pass

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# turtle1 = Turtle(shape="turtle")
# turtle1.color(colors[0])
# turtle1.penup()
# turtle1.goto(x=-230, y=140)
#
# turtle2 = Turtle(shape="turtle")
# turtle2.color(colors[1])
# turtle2.penup()
# turtle2.goto(x=-230, y=80)
#
# turtle3 = Turtle(shape="turtle")
# turtle3.color(colors[2])
# turtle3.penup()
# turtle3.goto(x=-230, y=20)
#
# turtle4 = Turtle(shape="turtle")
# turtle4.color(colors[3])
# turtle4.penup()
# turtle4.goto(x=-230, y=-40)
#
# turtle5 = Turtle(shape="turtle")
# turtle5.color(colors[4])
# turtle5.penup()
# turtle5.goto(x=-230, y=-100)
#
# turtle6 = Turtle(shape="turtle")
# turtle6.color(colors[5])
# turtle6.penup()
# turtle6.goto(x=-230, y=-160)


# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.back(10)
#
# def counter_clockwise():
#     tim.setheading(tim.heading()+5)
#
# def clockwise():
#     tim.setheading(tim.heading()-5)
#
# def clear():
#     # tim.goto(0,0)
#     # tim.clear()
#
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)
screen.exitonclick()