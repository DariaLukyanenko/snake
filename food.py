from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("red")
        self.penup()
        self.speed(0)

    def apper_food(self):

        self.goto(random.randint(-230,230),random.randint(-230,230))