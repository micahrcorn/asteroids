import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        
        radius = self.radius - ASTEROID_MIN_RADIUS
        roid1 = Asteroid(self.position.x, self.position.y, radius)
        roid2 = Asteroid(self.position.x, self.position.y, radius)

        roid1.velocity = v1 * 1.2
        roid2.velocity = v2 * 1.2
