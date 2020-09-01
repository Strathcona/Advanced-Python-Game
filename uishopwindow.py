import pygame
import UIObject
import shopbutton

class UIShopWindow(UIObject.UIObject):    
    def __init__(self, game):
        super(UIShopWindow,self).__init__(game)
        self.name = "Shop Window"
        self.ChangeSpriteImage(pygame.image.load('Images/Shop.png'))
        self.sprite.rect.x = 16
        self.sprite.rect.y = 16
        self.buttons = [shopbutton.ShopButton(game,self,"Hearts")]
        startX = 32
        startY = 156
        i = 0
        for button in self.buttons:
            button.sprite.rect.x = startX + i * 32
            button.sprite.rect.y = startY
            button.sprite.kill()
            i += 1
        self.sprite.kill()
        
    def ShowWindow(self):
        self.game.AddToVisibleSpriteGroup(self.sprite,2)
        for button in self.buttons:
            self.game.AddToVisibleSpriteGroup(button.sprite,2)
        
    def ButtonWasClicked(self, buttonName):
        print(buttonName+' was clicked')
        