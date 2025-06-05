#Bilgehan Gul
#Cs 172
#Hw4
from draw import Drawable
import pygame

class Ball(Drawable):
    def __init__(self, x = 0, y = 0, visible = True,size = 2):
        super().__init__(x, y, visible)
        self.size = size
        self.rect = pygame.Rect((x-size),(y-size),size*2,size*2)
    def draw(self,surface):
        if self.getVis():
            red = (255,0,0)
            pygame.draw.circle(surface, red, (self.getX(),self.getY()), self.size)

    def get_rect(self):
        pos = self.getX(), self.getY()
        size = self.get_size()
        self.rect = pygame.Rect((pos[0]-size),(pos[1]-size),size*2,size*2)
        return self.rect
        

    def get_size(self):
        return self.size

    def set_size(self,siz):
        self.size = siz


