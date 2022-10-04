from turtle import Turtle
import random


class Cars:
    def __init__(self):
        self.all_cars = []
        self.previous_car_pos = (0, 0)

    def create_car(self):

        new_car = Turtle()
        new_car.penup()
        random_y = random.randint(-160, 160)
        while -32 < random_y < 32:
            random_y = random.randint(-160, 160)
        new_car.goto(500, random_y)
        new_car.left(180)
        self.all_cars.append(new_car)

    def move(self):
        for each in self.all_cars:
            x_diff = self.previous_car_pos[0] - each.xcor()
            y_diff = self.previous_car_pos[1] - each.ycor()
            if -49 < y_diff < 49 and -145 < x_diff < 145:
                # each.hideturtle()
                each.left(180)
            each.forward(25)
            self.previous_car_pos = each.pos()
