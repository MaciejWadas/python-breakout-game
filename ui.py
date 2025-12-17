from turtle import Turtle

class UIWriter(Turtle):
    def __init__(self, score_pos):
        super().__init__()
        self.score_pos = score_pos
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(self.score_pos[0], self.score_pos[1])
        self.write(f"Score: {self.score}", align="center", font=("Courier", 40, "bold"))

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write("You Win!", align="center", font=("Courier", 60, "bold"))