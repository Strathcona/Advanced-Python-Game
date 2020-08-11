import UIObject
import pygame

class UIHeart(UIObject.UIObject):
     def __init__(self, game):
        super(UIHeart,self).__init__(game)
        self.fullSprite = pygame.image.load("Images/UIHeartFull.png")
        self.emptySprite = pygame.image.load("Images/UIHeartEmpty.png")
        self.ChangeSpriteImage(self.fullSprite)
    