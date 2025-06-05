#Bilgehan Gul
#Cs 172
#Hw4
from draw import Drawable
import pygame

class Block(Drawable):
    def __init__(self, x = 0, y = 0, visible = True,size = 10):
        super().__init__(x, y, visible)
        self.size = size
        self.rect = pygame.Rect(x,y,size,size)
    def draw(self,surface):
        if self.getVis():
            black = (0,0,0)
            blue = (0,0,255)
            pygame.draw.rect(surface, blue,self.rect)
            pygame.draw.rect(surface, black, self.rect,2)

    def get_rect(self):
        pos = self.getX(), self.getY()
        size = self.get_size()
        self.rect = pygame.Rect(pos[0],pos[1],size,size)
        return self.rect

    def get_size(self):
        return self.size

    def set_size(self,siz):
        self.size = siz

