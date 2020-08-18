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
        self.textBoxOpen = False
        self.cooldown = 30
        self.cooldownTimer = 0 
        self.updatesWhenTextBoxOpen = True
        
    def Interact(self):
        if self.cooldownTimer <= 0:
            if self.textBoxOpen:
                textBox = self.game.FindGameObject("Text Box")
                textBox.Hide()
                self.cooldownTimer = self.cooldown
                self.textBoxOpen = False
            else:
                textBox = self.game.FindGameObject("Text Box")
                textBox.ShowText(self.text)    
                self.cooldownTimer = self.cooldown
                self.textBoxOpen = True
            
            
    def Update(self):
        if self.textBoxOpen:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.Interact()
        if self.cooldownTimer > 0:
            self.cooldownTimer -= 1