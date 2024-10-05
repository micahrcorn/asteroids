# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        
        
        for member in updatable:    
            member.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
        

            
        screen.fill(pygame.Color(0,0,0)) 
        
        for member in drawable:
            member.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        

        

if __name__ == "__main__":
    main()