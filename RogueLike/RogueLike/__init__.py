import pygame, sys
from pygame.locals import *
from random import randint

displayx,displayy = 1000, 800
border = 50
interval = 25

def resolveSquare(mousex,mousey):
    return 1+ (mousex - border) // interval, 1+ (mousey - border) // interval
def returnTopLeftOfSquare(squarex, squarey):
    return (squarex-1) * interval + border, (squarey-1) * interval + border
def pickRandomSpot():
    x,y = resolveSquare(randint(border, displayx-border-1),randint(border,displayy-border-1))
    return returnTopLeftOfSquare(x,y)

def moveLeft(topleftX, topleftY, moves):
    if topleftX - interval < border or moves == 0: return topleftX, topleftY, moves
    return topleftX - interval, topleftY, moves -1
def moveRight(topleftX, topleftY, moves):
    if topleftX + interval >= displayx - border or moves == 0: return topleftX, topleftY, moves
    return topleftX + interval, topleftY, moves -1
def moveDown(topleftX, topleftY, moves):
    if topleftY + interval >= displayy - border or moves == 0: return topleftX, topleftY, moves
    return topleftX, topleftY + interval, moves -1
def moveUp(topleftX, topleftY, moves):
    if topleftY - interval < border or moves == 0: return topleftX, topleftY, moves
    return topleftX, topleftY - interval, moves -1

if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    character = pygame.image.load('character.png')
    token = pygame.image.load('token.png')
    windowSurfaceObject = pygame.display.set_mode((displayx, displayy))
    whiteColor = pygame.Color(255,255,255)
    blueColor = pygame.Color(0,0,255)
    greenColor = pygame.Color(0,255,0)
    redColor = pygame.Color(255,0,0)
    blackColor = pygame.Color(0,0,0)
    mousex, mousey = 0,0
    charx,chary = pickRandomSpot()
    tokens = {pickRandomSpot() for _ in range(randint(50,100))} - {(charx,chary)}
    print(tokens)
    moves = 100
    score = 0
    message = 'Hello World'

    fontObj = pygame.font.Font("freesansbold.ttf",32)
    looping = True
    while looping:
        windowSurfaceObject.fill( blackColor )
        pygame.draw.rect(windowSurfaceObject, whiteColor, (border,border,displayx - 2*border,displayy - 2*border))
        #
        for x in range(border,displayx-border,interval):
            pygame.draw.line(windowSurfaceObject, blackColor, (x,0),(x,displayy),1)
        for y in range(border,displayy-border,interval):
            pygame.draw.line(windowSurfaceObject, blackColor, (0,y),(displayx,y),1)
        
        for t in tokens:
            windowSurfaceObject.blit(token, (t[0]+1,t[1]+1))
        windowSurfaceObject.blit(character,(charx+1,chary+1))
        message = str(charx) + "," + str(chary)
        
        """messageSurfaceObj = fontObj.render(message, False, blueColor)
        messageRectObj = messageSurfaceObj.get_rect()
        messageRectObj.topleft = (10,20)
        windowSurfaceObject.blit(messageSurfaceObj, messageRectObj)"""
        
        movesSurfaceObj = fontObj.render("Moves: "+str(moves), False, blueColor)
        movesRectObj = movesSurfaceObj.get_rect()
        movesRectObj.bottomright = (displayx//4,displayy)
        windowSurfaceObject.blit(movesSurfaceObj, movesRectObj)
        
        scoreSurfaceObj = fontObj.render("Score: "+str(score), False, blueColor)
        scoreRectObj = scoreSurfaceObj.get_rect()
        scoreRectObj.bottomright = (3*displayx//4,displayy)
        windowSurfaceObject.blit(scoreSurfaceObj, scoreRectObj)
        if (charx, chary) in tokens:
            tokens -= {(charx, chary)}
            score += 1
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if event.button in (1,2,3):
                    sx,sy = resolveSquare(mousex, mousey)
                    cx, cy = returnTopLeftOfSquare(sx,sy)
                    message = str(mousex)+","+str(mousey) + " " + str(sx) + "," + str(sy) + " " + str(cx) + "," + str(cy)
                elif event.button in (4,5):
                    pass
                    #message = 'mouse scroll up or down'
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:#, K_RIGHT, K_UP, K_DOWN):
                    #message = 'Left key pressed'
                    charx, chary, moves = moveLeft(charx, chary, moves)
                elif event.key == K_RIGHT:
                    #message = 'Right key pressed'
                    charx, chary, moves = moveRight(charx, chary, moves)
                elif event.key == K_UP:
                    #message = 'Up key pressed'
                    charx, chary, moves = moveUp(charx, chary, moves)
                elif event.key == K_DOWN:
                    #message = 'Down key pressed'
                    charx, chary, moves = moveDown(charx, chary, moves)
                elif event.key == K_a:
                    pass
                    #message = '"A" key pressed'
                elif event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                    
        pygame.display.update()
        fpsClock.tick(30)