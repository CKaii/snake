from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_score = 0
        with open('score.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 275)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", move=False, align='center', font=('Arial', 12, 'normal'))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('score.txt', mode='w') as new_score:
                new_score.write(f'{self.high_score}')
        self.current_score = 0
        self.update_score()

    def add_score(self):
        self.current_score += 1
        self.update_score()



