import pygame
from colors import Colors

class Grid:

    def __init__(self):
        self.numRows = 20
        self.numCols = 10
        self.cellSize = 30 # 30 pixel per edge
        self.grid = [[0 for j in range(self.numCols)] for i in range(self.numRows)]
        self.colors = Colors.getCellColors()

    def printGrid(self):
        for i in range(self.numRows):
            for j in range(self.numCols):
                print(self.grid[i][j], end = " ")
            print()

    def getCellColors(self):
        darkGray = (26, 31, 40)
        green = (166, 255, 167)
        red = (255, 167, 166)
        orange = (255, 105, 64)
        yellow = (250, 234, 62) 
        purple = (200, 64, 255)
        cyan = (64, 255, 200)
        blue = (64, 81, 255)    
        return [darkGray, green, red, orange, yellow, purple, cyan, blue]
    
    def draw(self, screen):
        for i in range(self.numRows):
            for j in range(self.numCols):
                cellValue = self.grid[i][j]
                cellRect =  pygame.Rect(j * self.cellSize + 1, i * self.cellSize + 1, self.cellSize - 1, self.cellSize - 1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)
