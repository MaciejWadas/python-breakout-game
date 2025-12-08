from random import choice
from block import Block

BOX_SIZES = [2,3,5]
COLORS = ["red", "blue", "green"]
class BlockGrid:
    def __init__(self,grid_width,grid_height, num_of_rows, num_of_columns, offset, position):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.num_of_rows = num_of_rows
        self.num_of_columns = num_of_columns
        self.offset = offset
        self.position = position
        self.blocks = [[] for i in range(num_of_rows)]

    def add_blocks(self):
        for row in range(self.num_of_rows):
            space_left = 30
            while space_left > 5:
                dims = [2, choice(BOX_SIZES)]
                color = choice(COLORS)
                if len(self.blocks[row]) > 0:
                    last_block = self.blocks[row][-1]
                    position = (last_block.xcor() + (last_block.shapesize()[1]*21 /2) + dims[1]*21/2 + self.offset, self.position[1]-50*row)
                else:
                    position = (self.position[0] + dims[1]*21//2 ,self.position[1] - 50*row)
                block = Block(dims,color,position)
                self.blocks[row].append(block)

    def check_coords(self):
        for row in range(self.num_of_rows):
            for column in range(self.num_of_columns):
                print(self.blocks[row][column].pos())