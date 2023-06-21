from turtle import *
import random
timmy = Turtle()

colours = ["Indianred","Darkorchid","DeepSkyBlue","SeaGreen","Violet","Orange"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
for shape in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(shape)