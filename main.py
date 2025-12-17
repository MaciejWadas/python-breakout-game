from turtle import Screen
from ball import Ball
from block_grid import BlockGrid
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

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

    grid.check_collisions(ball)
screen.exitonclick()

#TODO-1 Score
#TODO-2 Corner Collisions
#TODO-3 Game end screen
#TODO-4 Timer