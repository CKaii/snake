from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.current_score}", move=False, align='center', font=('Arial', 12, 'normal'))

    def add_score(self):
        self.clear()
        self.current_score += 1
        self.update_score()



