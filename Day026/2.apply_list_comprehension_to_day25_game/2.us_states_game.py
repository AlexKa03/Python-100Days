import turtle
import pandas

def get_mouse_click_color(x, y):
    print(x, y)

# Main
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# turtle.onscreenclick(get_mouse_click_color)

guessed = 0
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
x_cords = data["x"].tolist()
y_cords = data["y"].tolist()
cords = []
for i in range(0, 50):
    cords.append((x_cords[i], y_cords[i]))
correct_guesses = []

while guessed <= 49:
    answer = screen.textinput(title=f"{guessed}/50 States Correct", prompt="What is another state's name?").title()
    if answer == "Exit":
        #check original used for loop and if statement to create list of missing states in day 25
        missing_states = [state for state in states if state not in correct_guesses]
        states_to_learn = pandas.DataFrame()
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer in states:
        guessed += 1
        index = states.index(answer)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.color("black")
        state.goto(cords[index])
        state.write(answer)
        correct_guesses.append(answer)




