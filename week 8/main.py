#Bilgehan Gul
#Cs 172
#Hw4
import pygame
from draw import Drawable
from Ball import Ball
from block import Block
from text import Text

# Imported needed classes from their files and pygame. 

def intersect(rect1, rect2):
    # This function returns True if two rectangles intersect
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False

if __name__ == "__main__":
    # Set-up the game
    pygame.init()
    pygame.display.set_caption("HW 4")
    fpsClock = pygame.time.Clock()
    displaySurface = pygame.display.set_mode((500, 500))
    surfaceColor = (255, 255, 255)

    ground = pygame.draw.line(displaySurface,(0,0,0),(0,400),(500,400),3)

    # The ball and block objects are created
    ball = Ball(36, 250, True, 10)
    xv = 0
    yv = 0
    posX = 35
    posY = 400

    blocks = []
    for i in range(0, 3):
        for k in range(1, 4):
            blocks.append(Block(400 + i * 20, 400 - k * 20, True, 20))

    

    score = 0
    score_str = Text(5, 10, True, "Score: ")

    # Constants that are needed are defined. 
    dt = 0.1
    g = 6.67
    R = 0.7
    eta = 0.5

    # Create a list that includes all of the objects to use to display the objects.  
    shapes = [ball, score_str]
    shapes += blocks

    while True:
        # A while loop is used for the program

        # Every object in shapes class gets displayed.
        displaySurface.fill(surfaceColor)
        ground = pygame.draw.line(displaySurface,(0,0,0),(0,400),(500,400),3)
        ball.draw(displaySurface)
        score_str.draw(displaySurface)
        for i in blocks:
            i.draw(displaySurface)

        # Stores position depending on the mouse movements. 
        for event in pygame.event.get():
            if(event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            
            elif(event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEBUTTONUP):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    downPos = []
                    downPos= pygame.mouse.get_pos()
                    

                elif event.type == pygame.MOUSEBUTTONUP:
                    upPos = []
                    upPos = pygame.mouse.get_pos()

                    xv = upPos[0] - downPos[0]
                    yv = -(upPos[1] - downPos[1])
    
        # Updates for the ball
        if abs(yv) > 0.0001:
            if posY > 400:
                yv = -R * yv
                xv = eta * xv
                posY = 400

            else:
                yv -= g * dt
                posX += dt * xv
                posY -= dt * yv

        else:
            if posY > 400:
                posY = 400

        if posX < 0 or posX > 500:
            posX = 35
            posY = 400
            xv = 0
            yv = 0

        ball.setX(posX)
        ball.setY(posY)
        
        
        # Checks if the ball intersected with any of the blocks, and turns the blocks' visibility to False if the ball intersects with it.a
        for block in blocks:
            if intersect(block.get_rect(),ball.get_rect()):
                if block.getVis():
                    block.setVis(False)
                    score += 1

        # Updates the changes on display and score
        score_str.setMsg("Score: " + str(score))
        pygame.display.update()
        fpsClock.tick(30)
        