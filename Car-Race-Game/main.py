import time
import random
from road import Road
from turtle import Turtle, Screen
from cars import Cars
from last_line import LastLine
from level import Level

CARS_COLORS = ["cars1.gif", "cars2.gif", "cars3.gif", "cars4.gif", "cars5.gif"]

screen = Screen()
screen.setup(width=850, height=480)
screen.bgpic("bg-road1.gif")
screen.addshape("cars5.gif")
screen.addshape("cars4.gif")
screen.addshape("cars3.gif")
screen.addshape("cars2.gif")
screen.addshape("cars1.gif")
screen.title("TRAFFIC RACER GAME")

screen.tracer(0)

last_line = LastLine()
level = Level()
road_pos_x = -270
road_list = []
for i in range(0, 8):
    road = Road(road_pos_x)
    road_list.append(road)
    road_pos_x += 120

cars = Cars()

user_car = Turtle()
user_car.shape("cars5.gif")
user_car.penup()
user_car.goto(-360, 0)

screen.update()


def car_up():
    if user_car.ycor() < 160:
        new_x = user_car.xcor()
        new_y = user_car.ycor() + 10
        user_car.goto(x=new_x, y=new_y)


def car_down():
    if user_car.ycor() > -160:
        new_x = user_car.xcor()
        new_y = user_car.ycor() - 10
        user_car.goto(x=new_x, y=new_y)


screen.listen()
screen.onkeypress(fun=car_up, key="Up")
screen.onkeypress(fun=car_down, key="Down")
is_game_on = True
distance = 0
while is_game_on:
    level.write_level()
    for each in road_list:
        y_diff = user_car.ycor() - each.ycor()
        x_diff = user_car.xcor() - each.xcor()
        if -30 < y_diff < 30 and -130 < x_diff < 135:
            each.hideturtle()
        each.move()

    last_line.move_line_indicator()

    if distance > 350:
        last_line.create_line()

    if distance < 350:
        random_chance = random.randint(0, 10)
        if random_chance == 3:
            cars.create_car()
            length = len(cars.all_cars) - 1
            cars.all_cars[length].shape(random.choice(CARS_COLORS))


    for each in cars.all_cars:
        # each.shape("cars3.gif")
        y_diff = user_car.ycor() - each.ycor()
        x_diff = each.xcor() - user_car.xcor()
        if user_car.distance(each) < 150 and -50 < y_diff < 50 and -110 < x_diff < 145:
            tom = Turtle()
            tom.hideturtle()
            tom.write(arg="Game Over", align="center", font=("Arial", 40, "bold"))
            is_game_on = False

    cars.move()

    if user_car.xcor() > last_line.last_line.xcor():
        tom = Turtle()
        tom.hideturtle()
        tom.write(arg="You Win!", align="center", font=("Arial", 40, "bold"))
        is_game_on = False
        level.level_value += 1
        distance = 0

    screen.update()
    time.sleep(0.1)
    distance += 1

screen.exitonclick()
