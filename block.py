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

    def check_collision(self, ball):
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
            "L": ball_pos[0] - 42,
            "R": ball_pos[0] + 42,
            "U": ball_pos[1] + 42,
            "D": ball_pos[1] - 42,
        }
        if self.alive:
            if (abs(ball_dims["L"] - block_dims["L"]) < 3 or abs(ball_dims["R"] - block_dims["R"]) < 3) and (block_dims["D"] < ball_pos[1] < block_dims["U"]):
                ball.bounce_x()
                return True
            elif (abs(ball_dims["D"] - block_dims["D"]) < 3 or abs(ball_dims["U"] - block_dims["U"]) < 3) and block_dims["L"] < ball_pos[0] < block_dims["R"]:
                ball.bounce_y()
                return True

        return False