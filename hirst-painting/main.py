# import colorgram
#
# colors = colorgram.extract('image2.jpg', 25)
#
# rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
#
# print(rgb)

import turtle as t
import random

#10x10 dots
#circle size is 20
#space between is 50

color_list = [(199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209)]

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setx(-230)
tim.sety(230)


for __ in range(10):
    for _ in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)
    tim.setx(-230)
    tim.sety(tim.ycor()-50)

screen = t.Screen()
screen.exitonclick()
