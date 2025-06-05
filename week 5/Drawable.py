from random import random
import pygame
import abc
import random

class Drawable(metaclass = abc.ABCMeta):
    
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y

    def getLoc(self):
        return (self.__x, self.__y)
    
    def setLoc(self,p):
        self.__x = p[0]
        self.__y = p[1]

    @abc.abstractmethod
    def draw(self,surface):
        pass

class Rectangle(Drawable):
    
    def __init__(self, x=0, y=0 ,width = 0  ,height = 0 ,color = ""):
        super().__init__(x, y)
        
        self.__width = width
        self.__height = height
        self.__color = color
        
    def draw(self,surface):
        xcor,ycor = Drawable.getLoc(self)
        pygame.draw.rect(surface,self.__color,(xcor,ycor,self.__width,self.__height))
        
class SnowFlake(Drawable):

    def __init__(self):
        super().__init__()

    def draw(self, surface):
        x , y = self.getLoc()
        white = (255,255,255)
        pygame.draw.line(surface,white,(x-5,y),(x+5,y))
        pygame.draw.line(surface,white,(x,y-5),(x,y+5))
        pygame.draw.line(surface,white,(x-5,y-5),(x+5,y+5))
        pygame.draw.line(surface,white,(x-5,y+5),(x+5,y-5))
if __name__ == '__main__':
    white = (255,255,255)
    blue = (0,0,255)
    green = (0,255,0)
    width = 550
    height =  350


    pygame.init()
    surface = pygame.display.set_mode((width, height*2))
    surface.fill(white)
    pygame.display.set_caption("Snowflake")

    sky = Rectangle(0,0,width,height,blue)
    ground = Rectangle(0,height,width,height,green)
    snow = SnowFlake()

    play = 1
    


    drawables = []
    drawables.append(sky)
    drawables.append(ground)
    drawables.append(snow)

    fps =  pygame.time.Clock()
    

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            
            elif event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE:
                if play == 1:
                    play = 0
                else:
                    play = 1
        if play == 1:
            for drawable in drawables:
                drawable.draw(surface)

                if isinstance(drawable, SnowFlake):
                    x, y = drawable.getLoc()
                    drawable.setLoc((x,y+1))
                    drawable.draw(surface)
            snow = SnowFlake() 
            x = random.randint(0, width)
            snow.setLoc((x,0))
            drawables.append(snow)
        fps.tick(100)
        pygame.display.update()


