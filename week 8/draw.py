#Bilgehan Gul
#Cs 172
#Hw4
from abc import ABC, abstractmethod


class Drawable(ABC):

    def __init__(self,x,y,visible):
        self.x = x
        self.y = y
        self.visible = visible
    
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_rect(self):
        pass

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getVis(self):
        return self.visible

    def setX(self,x):
        self.x= x
    def setY(self,y):
        self.y =y
    def setVis(self,vis):
        self.visible = vis 