import pygame
import UIObject

class ShopButton(UIObject.UIObject):
    
    def __init__(self,game, shopWindow, buttonName):
        super(ShopButton,self).__init__(game)
        self.ChangeSpriteImage(pygame.image.load("Images/ShopButton.png"))
        self.buttonName = buttonName
        self.shopWindow = shopWindow
        
    
    def Update(self):
        allclicks=pygame.mouse.get_pressed()
        leftclick=allclicks[0]
        if leftclick:
            print("Left Click")
            mousePosition=pygame.mouse.get_pos();
            if mousePosition[0] <= self.sprite.rect.x+self.sprite.rect.width and mousePosition[0] >= self.sprite.rect.x:
                if mousePosition[1] <= self.sprite.rect.y+self.sprite.rect.height and mousePosition[1] >= self.sprite.rect.y:
                    self.shopWindow.ButtonWasClicked(self.buttonName)
        