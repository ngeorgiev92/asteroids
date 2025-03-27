import pygame
from circleshape import *
from constants import *

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.radius = radius

    def update(self, dt):
        self.position += self.velocity * dt
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
