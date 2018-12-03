import random as rn
import pygame
from pygame.locals import *
import sys

class ConwaysGame:

#variables set to None are shown for readiablity reasons, all of them are set equal to something later on.
    def __init__(self):
        self.cols = 50
        self.rows = 50
        # self.cols = 174
        # self.rows = 98
        self.size = None
        self.screen = None
        self.gap = None
        self.grid = None

#initializes the gui and sets the grid equal to an array
    def setup(self):

        self.size = 10
        self.gap = 1
        pygame.init()
        self.screen = pygame.display.set_mode([1920,1080])
        self.screen.fill([255,0,0])
        self.grid = self.make_array(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                pygame.draw.rect(self.screen,[255,255,255],((self.size + self.gap) * i, (self.size + self.gap) * j, self.size, self.size))
        pygame.display.flip()

#makes the array for the game
    def make_array(self,cols, rows):

        array = []
        for i in range(cols):
            rowList = []
            for j in range(rows):
                rowList.append(rn.randint(0, 1))
            array.append(rowList)
        return array

    def draw(self,next_gen):
        white = [255,255,255]
        black = [0,0,0]
        for i in range(self.cols):
            for j in range(self.rows):
                if next_gen[i][j] ==0:
                    pygame.draw.rect(self.screen, black, ((self.size + self.gap) * i, (self.size + self.gap) * j, self.size, self.size))
                if next_gen[i][j] ==1:
                    pygame.draw.rect(self.screen, white, ((self.size + self.gap) * i, (self.size + self.gap) * j, self.size, self.size))
        pygame.display.flip()

#this applies all the game of life rules and changes the states of the cells
    def calculate(self):
        next_generation = self.make_array(self.cols,self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                state = self.grid[i][j]
                neighbors = self.find_neighbors( i, j)
                if state == 0 and neighbors == 3:
                    next_generation[i][j] = 1

                elif (state == 1 and (neighbors < 2 or neighbors > 3)):
                    next_generation[i][j] = 0


                else:
                    next_generation[i][j] = state

        self.grid = next_generation
        self.draw(next_generation)

#calculates the amount of neighboring cells that are alive
    def find_neighbors(self, x, y):
        counter = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                col = (x + i + self.cols) % self.cols
                row = (y + j + self.rows) % self.rows
                counter += self.grid[col][row]
        counter -= self.grid[x][y]
        return counter

#main code
if __name__ == '__main__':
    cg = ConwaysGame()
    cg.setup()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
        cg.calculate()