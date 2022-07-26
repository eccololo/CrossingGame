from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Turtle is moving up when player press Up arrow."""
        self.forward(MOVE_DISTANCE)

    def reset_player_position(self):
        """This method resets player position to starting position."""
        self.goto(STARTING_POSITION)
