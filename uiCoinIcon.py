import UIObject
import pygame

class UICoinIcon(UIObject.UIObject):
     def __init__(self, game):
        super(UICoinIcon,self).__init__(game)
        self.ChangeSpriteImage(pygame.image.load("Images/coin.png"))
