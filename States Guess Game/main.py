import turtle
import pandas 
from scipy.fftpack import tilbert
screen = turtle.Screen()
screen.title("India States Game")
image = ("India_states.gif")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("States.csv")
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states) < 30:
    answer_state = screen.textinput(title="Guess the State", 
                                prompt="What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

screen.exitonclick()