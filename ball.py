from turtle import Turtle

class Ball(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = -3
        self.move_speed = 0.1
        self.goto(pos[0],pos[1])
        self.res_x = pos[0]
        self.res_y = pos[1]

    def move(self):
        new_x = self.xcor() + self.x_move * self.move_speed
        new_y = self.ycor() + self.y_move * self.move_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(self.res_x,self.res_y)
        self.move_speed = 0.1
        self.bounce_x()

    def update_speed(self):
        self.move_speed *= 1.1
