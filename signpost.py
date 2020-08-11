import GameObject
import pygame
    
class SignPost(GameObject.GameObject):    
    
    
    def __init__(self, game):
        super(SignPost, self).__init__(game)
        self.name = "signpost"
        self.text = ""
        self.interactable = True
        self.ChangeSpriteImage(pygame.image.load("Images/SignPost.png"))
        #how long in between readings
        self.cooldown = 60
        self.cooldownTimer = 0 
        
    def Interact(self):
        if self.cooldownTimer <= 0:
            print(self.text)
            self.cooldownTimer = self.cooldown
    
    def Update(self):
        if self.cooldownTimer > 0:
            self.cooldownTimer -= 1
        