import turtle
from turtle import Screen, Turtle
import pandas


screen = Screen()
screen.title("US Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0


data = pandas.read_csv('50_states.csv')
data_state = data.state.to_list()

is_on = True
while is_on:
    user_input = screen.textinput(title=f"{score}/50. Guess the State", prompt="What's the another State").capitalize()
    for state in data_state:
        if user_input == state:
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_row = data[data.state == user_input]
            t.goto(int(state_row.x),int(state_row.y))
            t.write(user_input)
            score = score + 1


screen.exitonclick()