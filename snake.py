from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        initial_position = 0

        for part in range(0, 3):
            snake = Turtle(shape='square')
            snake.color('white')
            snake.penup()
            snake.setx(initial_position)
            initial_position -= 20
            self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.segments[0].left(90)
