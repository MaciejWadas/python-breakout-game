from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position,move_speed):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(position)
        self.move_speed = move_speed

    def move_left(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x,self.ycor())

    def move_right(self):
        new_x = self.xcor() + self.move_speed
        self.goto(new_x,self.ycor())
