import pygame
from textwrap import fill
from constants import *

black = (0, 0, 0)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        screen.fill(black)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return




if __name__ == "__main__":
    main()