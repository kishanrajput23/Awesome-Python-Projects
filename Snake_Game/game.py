# import packages
import random
import turtle
import time

# creating screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.tracer(0)
screen.setup(width=700,height=700)
screen.bgcolor("#1d1d1d")

# creating border
turtle.speed(5)   ###
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()  ##
turtle.hideturtle()  ##

# scores
score=0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed()
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.shape("square")
snake.direction= 'stop'

# food
fruit = turtle.Turtle()
fruit.speed()
fruit.color("white")
fruit.penup()
fruit.shape("square")
fruit.goto(30, 30)

old_fruit = []

# scoring
scoring= turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score : ",align="center",font=("Courier",24,"bold"))

# define how to move
def snake_go_up():
    if snake.direction != "Down":
        snake.direction = "Up"

def snake_go_down():
    if snake.direction != "Up":
        snake.direction = "Down"

def snake_go_right():
    if snake.direction != "Left":
        snake.direction = "Right"

def snake_go_left():
    if snake.direction != "Right":
        snake.direction = "Left"

def snake_move():
    if snake.direction == "Up":
        y = snake.ycor()
        snake.sety(y+20)

    if snake.direction == "Down":
        y = snake.ycor()
        snake.sety(y-20)

    if snake.direction == "Left":
        x = snake.xcor()
        snake.setx(x-20)

    if snake.direction == "Right":
        x = snake.xcor()
        snake.setx(x+20)

# keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop
while True:
    screen.update()

    # snake and fruit colision


    if snake.distance(fruit) < 20:
        x= random.randint(-250, 250)
        y = random.randint(-250, 250)
        fruit.goto(x, y)
        scoring.clear()
        score+=1
        scoring.write("Score : {}".format(score),align="center",font=("Courier",24,"bold"))
        delay -= 0.001

        # creating new fruits
        new_fruit =turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.penup()
        new_fruit.color("red")
        old_fruit.append(new_fruit)\

    # adding ball to snake
    for index in range(len(old_fruit) -1,0,-1):
        a=old_fruit[index -1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)


    if len(old_fruit) > 0:
        a=snake.xcor()
        b=snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()

    # snake and border collision
    if snake.xcor() >280 or snake.xcor() <-300 or snake.ycor() >240 or snake.ycor() <-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("     Game Over  \n  Your Score {}".format(score),align="center",font=("Courier",30,"bold"))

    # snake collision
    for food in old_fruit:
        if food.distance(snake) <20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("     Game Over  \n  Your Score {}".format(score), align="center", font=("Courier", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()
