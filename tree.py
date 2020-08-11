import GameObject
import pygame
    
class Tree(GameObject.GameObject):    
    def __init__(self, game):
        super(Tree, self).__init__(game)
        self.ChangeSpriteImage(pygame.image.load("Images/Tree.png"))