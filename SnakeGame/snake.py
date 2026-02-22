from turtle import Turtle

POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.segments = []
        self.x_cor = 0
        self.y_cor = 0
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in POSITION:
            self.add_block(position)

    def add_block(self,position):
        tommy = Turtle('square')
        tommy.color("white")
        tommy.penup()
        tommy.goto(position)
        self.segments.append(tommy)

    def extend(self):
        self.add_block(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            self.x_cor = self.segments[seg-1].xcor()
            self.y_cor = self.segments[seg-1].ycor()
            self.segments[seg].goto(self.x_cor, self.y_cor)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)