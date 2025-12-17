from datetime import datetime, timedelta
from turtle import Turtle

class Block(Turtle):
    def __init__(self,dims,color,position):
        Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=dims[0],stretch_len=dims[1])
        self.color(color)
        self.goto(position)
        self.alive = True

    def destroy(self):
        self.hideturtle()
        self.alive = False

    def check_collision(self, ball, last_bounce_time, sensitivity, time_delta):
        left_edge = self.xcor()-(self.shapesize()[1]*21/2)
        right_edge = self.xcor()+(self.shapesize()[1]*21/2)
        up_edge = self.ycor()+21
        down_edge = self.ycor()-21
        block_dims = {
            "L": left_edge,
            "R": right_edge,
            "U": up_edge,
            "D": down_edge
        }
        ball_pos = ball.pos()
        ball_dims = {
            "L": ball_pos[0] - 10.5,
            "R": ball_pos[0] + 10.5,
            "U": ball_pos[1] + 10.5,
            "D": ball_pos[1] - 10.5,
        }
        if self.alive:
            if (abs(ball_dims["L"] - block_dims["R"]) < sensitivity or abs(ball_dims["R"] - block_dims["L"]) < sensitivity) and (block_dims["D"] < ball_dims["D"] + 5< block_dims["U"] or block_dims["D"] < ball_dims["U"] - 5 < block_dims["U"]):
                if datetime.now() - last_bounce_time > timedelta(milliseconds=time_delta):
                    ball.bounce_x()
                return True
            elif (abs(ball_dims["D"] - block_dims["U"]) < sensitivity or abs(ball_dims["U"] - block_dims["D"]) < sensitivity) and (block_dims["L"] < ball_dims["L"] + 5< block_dims["R"] or block_dims["L"] < ball_dims["R"] - 5< block_dims["R"]):
                if datetime.now() - last_bounce_time > timedelta(milliseconds=time_delta):
                    ball.bounce_y()
                return True

        return False