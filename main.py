from turtle import Screen
from ball import Ball
from block_grid import BlockGrid
from paddle import Paddle
from ui import UIWriter

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.title("Breakout")
screen.tracer(0)

ui = UIWriter((0,280))

paddle = Paddle((0,-270),50)
grid = BlockGrid(800,300,5,35,5,(-395,200))
ball = Ball((0,-100))

grid.add_blocks()
grid.check_coords()

screen.listen()
screen.onkeypress(lambda: paddle.move_left(-screen.window_width()/2), "a")
screen.onkeypress(lambda: paddle.move_right(screen.window_width()/2), "d")


game_is_on = True
while game_is_on:
    if grid.check_for_win():
        game_is_on = False
        ui.end_game()
    screen.update()
    ball.move()

    if ball.ycor() < -250:
        if paddle.xcor() - paddle.shapesize()[1]*10.5 < ball.xcor() < paddle.xcor() + paddle.shapesize()[1]*10.5:
            ball.bounce_y()
    if -390 > ball.xcor()  or ball.xcor() > 390:
        ball.bounce_x()
    if ball.ycor() > 290:
        ball.bounce_y()

    if ball.ycor() < -290:
        ball.reset_position()

    if grid.check_collisions(ball):
        ui.update_score()
screen.exitonclick()
