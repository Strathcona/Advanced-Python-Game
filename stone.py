import GameObject
import pygame

class Stone(GameObject.GameObject):    
    def __init__(self, game):
        super(Stone,self).__init__(game)
        self.ChangeSpriteImage(pygame.image.load("Images/stone.png"))