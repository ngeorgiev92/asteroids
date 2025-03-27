import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, 2)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.radius = radius

    def update(self, dt):
        self.position += self.velocity * dt
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vector_1 = self.velocity.rotate(random_angle)
            vector_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2
            
