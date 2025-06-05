#Bilgehan Gul
#Cs 172
#Hw4
from draw import Drawable
import pygame

class Text(Drawable):
    def __init__(self, x, y, visible,msg):
        super().__init__(x, y, visible)
        self.__msg = msg
        
        self.__fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.__surface = self.__fontObj.render(msg, True, (0, 0, 0))

    # This method gets the message of the object
    def getMsg(self):
        return self.__msg

    # This method sets the message of the object
    def setMsg(self, msg):
        self.__msg = msg
        self.__surface = self.__fontObj.render(msg, True, (0, 0, 0))


    

    # This method takes as a parameter a surface to draw on
    def draw(self, surface):
        if self.getVis():
            surface.blit(self.__surface, (self.getX(),self.getY()))

    # This method returns a Pygame Rect object that is the bounding rectangle that fits tightly around your object.
    def get_rect(self):
        x = self.getX()
        y = self.getY()
        size = self.__fontObj.size(self.msg)
        return self.Rect(x, y, size[0], size[1])