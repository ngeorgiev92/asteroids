from circleshape import *
from constants import *


class Player(CircleShape, pygame.sprite.Sprite):  # Inherit from CircleShape and pygame.sprite.Sprite
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Initialize CircleShape
        pygame.sprite.Sprite.__init__(self)   # Explicitly initialize pygame's Sprite

        # Create a transparent surface for the triangle
        self.image = pygame.Surface((self.radius * 3, self.radius * 3), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)  # Center the rect on the CircleShape's position
        self.hitbox = self.rect
        self.rotation = 0  # Angle of rotation in degrees
        self.update_image()  # Draw the initial triangle on the image

    
    def triangle(self):
        """Calculate the three points of the triangle."""
        # Forward vector (points "up" relative to rotation)
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        # Right vector (perpendicular, scaled slightly smaller for offset)
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        
        # Triangle vertices: one forward, and two mirrored backward
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update_image(self):
        """Redraw the triangle image based on the current rotation."""
        # Clear the surface by filling it with transparency
        self.image.fill((0, 0, 0, 0))  # (0, 0, 0, 0) is fully transparent

        # Calculate the offset so the triangle is centered in the larger surface
        center_offset = pygame.Vector2(self.image.get_width() // 2, self.image.get_height() // 2)

        # Get adjusted triangle points relative to the new center of the surface
        triangle_points = [
            (center_offset.x + point.x - self.position.x, center_offset.y + point.y - self.position.y)
            for point in self.triangle()
        ]

    # Draw the triangle on the surface
        pygame.draw.polygon(self.image, pygame.Color("white"), triangle_points, 2)

    # Update the rect's position to match the CircleShape's position
        self.rect.center = self.position

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.update_image()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt * -1)
        if keys[pygame.K_s]:
            self.move(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = self.position
