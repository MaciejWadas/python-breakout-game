from turtle import Screen, Turtle
import time

from block_grid import BlockGrid
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0,-270),20)
grid = BlockGrid(800,300,3,10,5,(-395,200))

grid.add_blocks()
grid.check_coords()

screen.listen()
screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_right, "d")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
