from turtle import Turtle

class Block(Turtle):
    def __init__(self,dims,color,position):
        Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=dims[0],stretch_len=dims[1])
        self.color(color)
        self.goto(position)

    def destroy(self):
        self.hideturtle()