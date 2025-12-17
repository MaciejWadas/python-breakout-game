from random import choice
from block import Block
from datetime import datetime

BOX_SIZES = [2,3,5]
COLORS = ["red", "blue", "green"]
class BlockGrid:
    def __init__(self,grid_width,grid_height, num_of_rows, space_per_row, offset, position):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.num_of_rows = num_of_rows
        self.space_per_row = space_per_row
        self.offset = offset
        self.position = position
        self.blocks = [[] for i in range(num_of_rows)]
        self.last_bounce_time = datetime.now()


    def add_blocks(self):
        for row in range(self.num_of_rows):
            space_left = self.space_per_row
            while space_left > 0:
                if space_left == 2:
                    dims = [2,2]
                elif space_left == 3:
                    dims = [2,3]
                elif space_left == 4:
                    dims = [2,2]
                else:
                    dims = [2, choice(BOX_SIZES)]
                color = choice(COLORS)
                if len(self.blocks[row]) > 0:
                    last_block = self.blocks[row][-1]
                    position = (last_block.xcor() + (last_block.shapesize()[1]*21 /2) + dims[1]*21/2 + self.offset, self.position[1]-50*row)
                else:
                    position = (self.position[0] + dims[1]*21/2 ,self.position[1] - 50*row)
                block = Block(dims,color,position)
                self.blocks[row].append(block)
                space_left -= dims[1]

    def check_coords(self):
        for row in range(self.num_of_rows):
            for column in range(len(self.blocks[row])):
                print(self.blocks[row][column].pos(), self.blocks[row][column].xcor(), self.blocks[row][column].ycor())

    def check_collisions(self,ball):
        for row in range(self.num_of_rows):
            for column in range(len(self.blocks[row])):
                block = self.blocks[row][column]
                if block.check_collision(ball,self.last_bounce_time,0.5,25):
                    block.destroy()
                    self.last_bounce_time = datetime.now()

    def check_for_win(self):
        for row in range(self.num_of_rows):
            for column in range(len(self.blocks[row])):
                block = self.blocks[row][column]
                if block.alive:
                    return False
        return True

