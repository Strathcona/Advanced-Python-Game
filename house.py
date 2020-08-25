import GameObject
import pygame
    
class House(GameObject.GameObject):    
    def __init__(self, game):
        super(House, self).__init__(game)
        self.ChangeSpriteImage(pygame.image.load("Images/House.png"))