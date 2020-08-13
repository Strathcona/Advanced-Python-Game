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
        textBox = self.game.FindGameObject("Text Box")
        textBox.ShowText(self.text)          
            
            
    def Update(self):
        pass