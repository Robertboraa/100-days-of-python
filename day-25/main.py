import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []
while len(guessed_states)< 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="What is your guess?").strip().title()
    if answer == "Exit":
       break

    if answer in data["state"].values:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data["state"] == answer.lower().title()].iloc[0]
        x = row["x"]
        y = row["y"]
        t.goto(x, y)
        t.write(answer)
    else :
        screen.textinput(title="Wrong!", prompt="That's not a US state. Try again:")
all_states = data["state"].tolist()
missing = [state for state in all_states if state not in guessed_states]
df = pandas.DataFrame(missing, columns=["state"])
df.to_csv("states_to_learn.csv", index=False)
turtle.mainloop()