import pygame
_ZOMBIE_SPEED = 0.01
_ZOMBIE_WIDTH = 0.10
_ZOMBIE_HEIGHT = 0.10

class Zombie(pygame.sprite.Sprite):
    def __init__(self, word):
        super(Zombie, self).__init__()
        self._width = _ZOMBIE_WIDTH
        self._height = _ZOMBIE_HEIGHT
        self._speed = _ZOMBIE_SPEED
        self.top_left_x = 1 - self._width / 2
        self.top_left_y = 0.7 - self._height / 2
        self._word = word
        
        self.index = 0

    def update(self, Images: 'List of Images', Rectangle: 'Pygame Rectangle', posX: int):
        self.rect = Rectangle
        self.index += 1
        if self.index >= len(Images):
            self.index = 0
        self.image = Images[self.index]

        ## Barrier For Now
        if posX > 0:
            self.move_left()
        
    def top_left(self) -> (float, float):
        ''' Return Position of the zombie in a tuple '''
        return (self.top_left_x, self.top_left_y)

    def getWidth(self) -> float:
        ''' Get Width '''
        return self._width

    def getHeight(self) -> float:
        ''' Get Height '''
        return self._height
    
    def getWord(self) -> str:
        ''' Get Word '''
        return self._word

    def move_left(self) -> None:
        ''' Zombie Move to Left '''
        self._move(-self._speed)
        
    def changeSpeed(self,newSpeed):
        ''' Change Speed '''
        self._speed = newSpeed

    def changeWord(self, newWord):
        ''' Change Word '''
        self._word = newWord
        
    def _move(self, delta_x: float) -> None:
        ''' Zombie Move (Private Function)'''
        tl_x = self.top_left_x
        new_x = tl_x + delta_x
        self.top_left_x = new_x

