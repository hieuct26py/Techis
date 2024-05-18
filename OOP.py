import pygame, sys
from grid import Grid
from blocks import *

pygame.init()

#color
lightblue = (166, 209, 255)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Techis")

clock = pygame.time.Clock()

Con = True
fps = 60

gameGrid = Grid()
# gameGrid.printGrid()

test = LBlock()

while Con:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Con = False
    
    #Draw
    screen.fill(lightblue)
    gameGrid.draw(screen)
    test.draw(screen)

    pygame.display.update()
    clock.tick(fps)

