'''
Created on Feb 24, 2015

@author: arhoda
'''
import pygame, sys;



if __name__ == '__main__':
    pygame.init()

    size = width, height = 400, 500
    
    black = 0,0,0
    white = 255,255,255
    
    screen = pygame.display.set_mode(size)
    
    square_rect = (50,50,100,100)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            screen.fill(white)
            square = pygame.draw.rect(screen, black, square_rect)
            pygame.display.flip()