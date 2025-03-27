import pygame
import time
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
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
        dt = clock.tick(60) / 1000
        screen.fill(screen_color)
        updatable.update(dt)
        for asteroid in asteroids:
            if(asteroid.check_collision(player)):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if(asteroid.check_collision(shot)):
                    asteroid.split()
                    shot.kill()
        try:
            drawable.draw(screen)
        except AttributeError:
    # If that fails, try drawing each sprite individually
            for sprite in drawable:
                if hasattr(sprite, 'draw') and callable(sprite.draw):
                    sprite.draw(screen)

        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()
