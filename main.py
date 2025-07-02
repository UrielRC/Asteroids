import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    
    


    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
        

        screen.fill("black")
        updatable.update(dt)
        for player_char in drawable:
            player_char.draw(screen)
        # After the update step
        for asteroid in asteroids:
            for bullet in shot:
                if asteroid.collision(bullet):
                    asteroid.split(asteroid_field)
                    bullet.kill()
            
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
        
        pygame.display.flip()  

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
