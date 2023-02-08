from pickle import TRUE
import pygame, sys, random

from pygame.locals import *


WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fractal')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 3



def draw_window():
    WIN.fill(WHITE)
    
    drawCircle([WIDTH/2, HEIGHT/2], 450)
    
    pygame.display.update()

def drawCircle(center, radius):
    pygame.draw.circle(WIN, BLACK, center, radius, width=1)
    if (radius > 50):
        drawCircle([center[0] + radius/2, center[1]], radius/2)
        drawCircle([center[0] - radius/2, center[1]], radius/2)
        drawCircle([center[0], center[1] + radius/2], radius/2)
        drawCircle([center[0], center[1] - radius/2], radius/2)


def main():

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
           
        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()