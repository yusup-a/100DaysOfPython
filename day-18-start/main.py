import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)



# for _ in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)

# for _ in range(3, 11):
#     tim.color(random_color())
#     for x in range(_):
#         tim.forward(100)
#         tim.right(360/_)


tim.speed("fastest")
# tim.pensize(15)
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(15)
#     tim.setheading(random.randint(0, 4) * 90)

def draw_spirograph(amount):
    for _ in range(amount):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + (360/amount))

draw_spirograph(100)

screen = t.Screen()
screen.exitonclick()