import pygame
import time
from constants import *
from player import *

def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    screen_color = pygame.Color("black")
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick()
        dt = clock.tick() / 1000
        screen.fill(screen_color)
        player.draw(screen)
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()
