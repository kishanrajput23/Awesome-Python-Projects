from turtle import Turtle


class Road(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=0.8, stretch_len=2.5)
        self.color("white")
        self.penup()
        self.goto(pos, 0)
        self.left(180)

    def move(self):
        self.forward(30)
        if self.xcor() < -440:
            self.showturtle()
            self.goto(510, 0)
