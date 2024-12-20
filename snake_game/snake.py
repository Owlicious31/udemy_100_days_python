from turtle import Turtle

MOVEMENT_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        snake_seg = Turtle("square")
        snake_seg.color("dark green")
        snake_seg.penup()
        snake_seg.setposition(position)
        self.segments.append(snake_seg)

    def extend_snake(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        """Moves the snake by making each snake segment go to the position of the one in front of it."""

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)

        # Moving the first segment forward forever
        self.snake_head.forward(MOVEMENT_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)




