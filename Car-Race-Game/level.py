from turtle import Turtle


class Level:
    def __init__(self):
        self.level = Turtle()
        self.level.hideturtle()
        self.level.penup()
        self.level.color("white")
        self.level.goto(0, 208)
        self.level_value = 1

    def write_level(self):
        self.level.write(arg=f"Level {self.level_value}", align="center", font=("Arial", 20, "bold"))

