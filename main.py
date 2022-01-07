import turtle
import pandas as pd

from state_position import StatePosition

# screen set up
screen = turtle.Screen()
screen.title('U.S States Game')

image = 'images/blank_states_img.gif'
turtle.addshape(image)

turtle.shape(image)

data = pd.read_csv('data/50_states.csv')

list_states_names = data.state.to_list()
correct_user_answers = []

while len(correct_user_answers) <= len(list_states_names):
    user_guess = (screen.textinput(f'{len(correct_user_answers)}/{len(list_states_names)} '
                                   f'States correct', 'What\'s another state name?')).title()
    if user_guess=='Exit':
        states_to_learn = [state for state in list_states_names if state not in correct_user_answers]
        df = pd.DataFrame(states_to_learn, columns=['States to learn'])
        df.to_csv('data/states_to_learn.csv')
        break

    if user_guess in list_states_names and user_guess not in correct_user_answers:
        x = int(data.x[data.state==user_guess])
        y = int(data.y[data.state==user_guess])
        StatePosition(x, y, user_guess)
        correct_user_answers.append(user_guess)

screen.mainloop()
