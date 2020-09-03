import pygame
import UIObject
import shopbutton

class UIShopWindow(UIObject.UIObject):    
    def __init__(self, game):
        super(UIShopWindow,self).__init__(game)
        self.name = "Shop Window"
        self.ChangeSpriteImage(pygame.image.load('Images/Shop.png'))
        self.exitButton = shopbutton.ShopButton(game,self,"exit")
        self.exitButton.sprite.rect.x = 16
        self.exitButton.sprite.rect.y = 16

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
        self.exitButton.sprite.kill()
        
    def ShowWindow(self):
        self.game.AddToVisibleSpriteGroup(self.sprite,2)
        self.game.AddToVisibleSpriteGroup(self.exitButton.sprite, 2)
        for button in self.buttons:
            self.game.AddToVisibleSpriteGroup(button.sprite,2)
        
    def ButtonWasClicked(self, buttonName):
        if(buttonName == "exit"):
            self.sprite.kill()
            self.exitButton.sprite.kill()
            for button in self.buttons:
                button.sprite.kill()
            return

        player = self.game.FindGameObject("Player")
        if(buttonName == "Hearts" and player.coins >= 1):
            player.maxHealth += 1
            player.coins -= 1
        