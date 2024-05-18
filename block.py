from colors import Colors
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rotaionState = 0
        self.colors = Colors.getCellColors()

    def draw(self, screen):
        tiles = self.cells[self.rotaionState]
        for tile in tiles:
            tileRect = pygame.Rect(tile.col * self.cellSize + 1 , tile.row * self.cellSize + 1, self.cellSize - 1, self.cellSize - 1)
            pygame.draw.rect(screen, self.colors[self.id], tileRect)