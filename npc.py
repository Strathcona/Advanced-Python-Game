import GameObject
import pygame
    
class NPC(GameObject.GameObject):    
    def __init__(self, game):
        super(NPC, self).__init__(game)
        self.ChangeSpriteImage(pygame.image.load("Images/NPC.png"))
        self.name = "shopkeeper"
        self.interactable=True
        
    def Interact(self):
        shop = self.game.FindGameObject("Shop Window")
        shop.ShowWindow()
        