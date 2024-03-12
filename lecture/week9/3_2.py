import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        
        screen.blit(pygame.image.load('ball.png'), (20, 20))
        
        pygame.display.flip()
        clock.tick(60)