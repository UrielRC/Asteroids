import pygame
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt) 

    def split (self,asteroid_field):
        if self.radius > ASTEROID_MIN_RADIUS:
            rand_angle = random.uniform(20, 50)
            new_ast_1 = self.velocity.rotate(rand_angle) * 1.2
            new_ast_2 = self.velocity.rotate(-rand_angle) * 1.2
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid_field.spawn(new_rad, self.position, new_ast_1)
            asteroid_field.spawn(new_rad, self.position, new_ast_2)
            self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return