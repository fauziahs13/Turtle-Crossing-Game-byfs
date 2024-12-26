from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.shapesize(1, 1)
        self.setheading(90)
        self.finish = FINISH_LINE_Y
        self.start()


    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def start(self):
        self.goto(STARTING_POSITION)


