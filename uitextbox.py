import pygame
import UIObject

class UITextBox(UIObject.UIObject):
    def __init__(self, game):
        super(UITextBox,self).__init__(game)
        self.name = "Text Box"
        self.font = pygame.font.Font("Roboto-Medium.ttf", 16)
        self.ChangeSpriteImage(pygame.image.load("Images/UIBox.png"))
        self.sprite.rect.x = 16
        self.sprite.rect.y = 165
        self.sprite.kill()
        self.textSprite = None

        
    def ShowText(self, text):
        #Add UITextBox background image to the list of visible sprites
        self.game.AddToVisibleSpriteGroup(self.sprite, 2)

        #Create a surface with font.render        
        textSurface = self.font.render(text,1,(0,0,0))
        #Turn it into a sprite
        self.textSprite = pygame.sprite.Sprite()
        self.textSprite.image = textSurface
        self.textSprite.rect = self.textSprite.image.get_rect()
        textRect = self.textSprite.rect
        textRect.x = 21
        textRect.y = 165
        self.game.AddToVisibleSpriteGroup(self.textSprite,3)
        
    def Hide(self):
        self.sprite.kill()
        self.textSprite.kill()

         
