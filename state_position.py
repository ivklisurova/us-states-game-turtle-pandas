from turtle import Turtle


class StatePosition(Turtle):

    def __init__(self, x, y, name):
        super().__init__()
        self.create(x, y, name)

    def create(self, x, y, name):
        self.color('black')
        self.hideturtle()
        self.penup()
        self.setposition(x, y)
        self.write(f'{name}')



