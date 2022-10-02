from turtle import Turtle


class LastLine:
    def __init__(self):
        self.last_line = Turtle()
        self.last_line.penup()
        self.last_line.color("red")
        self.last_line.hideturtle()
        self.last_line.goto(410, -160)
        self.last_line.left(90)
        self.last_line.pensize(10)

        self.new_pos_x = 410

        self.line_indicator = Turtle()
        self.line_indicator.color("red")
        self.line_indicator.pencolor("black")
        self.line_indicator.penup()
        self.line_indicator.goto(260, 223)
        self.line_indicator.pendown()
        self.line_indicator.pensize(3)

        self.indicator_dot = Turtle()
        self.indicator_dot.color("black")
        self.indicator_dot.penup()
        self.indicator_dot.hideturtle()
        self.indicator_dot.goto(255, 220)
        self.indicator_dot.pendown()
        self.indicator_dot.pensize(6)
        self.indicator_dot.circle(3)
        self.indicator_dot.penup()
        self.indicator_dot.goto(376, 220)
        self.indicator_dot.pendown()
        self.indicator_dot.pensize(6)
        self.indicator_dot.circle(3)

    def create_line(self):
        self.last_line.clear()
        self.last_line.circle(2)
        self.last_line.forward(380)
        self.last_line.circle(2)
        self.new_pos_x -= 25
        self.last_line.penup()
        self.last_line.goto(self.new_pos_x, -190)
        self.last_line.pendown()

    def move_line_indicator(self):
        self.line_indicator.forward(0.3)
