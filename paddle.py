from turtle import Turtle
STARTING_POSITION = [(350, -40), (350, -20), (350, -00), (350, -20), (350, 40)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.initialize(1)

    def initialize(self, side):
        for segment in STARTING_POSITION:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(segment)
            self.segments.append(new_segment)
            side = side
