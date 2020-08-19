import pygame
import UIObject

class UITextBox(UIObject.UIObject):
    def __init__(self, game):
        super(UITextBox,self).__init__(game)
        self.name = "Text Box"
        self.font = pygame.font.Font("Roboto-Medium.ttf", 16)
        self.ChangeSpriteImage(pygame.image.load("Images/UIBox.png"))
        self.sprite.rect.x = 16
        self.sprite.rect.y = 152
        self.sprite.kill()
        self.textSprites = []

        
    def ShowText(self, text):
        #Add UITextBox background image to the list of visible sprites
        self.game.AddToVisibleSpriteGroup(self.sprite, 2)
        self.game.textBoxOpen = True
        lines = []
        
        splitText , remainingText = self.SplitLineToFit(text,220)  
        lines.append(splitText)
        while self.font.size(remainingText)[0] > 220:
            splitText , remainingText = self.SplitLineToFit(remainingText,220)  
            print(splitText + " " +remainingText)
            lines.append(splitText)  
        lines.append(remainingText)
        lineHeight = self.font.size("")[1]+2
        lineNum = 0
        self.textSprites.clear()
        for line in lines:
            textSurface = self.font.render(line,1,(0,0,0))
            #Turn it into a sprite
            textSprite = pygame.sprite.Sprite()
            textSprite.image = textSurface
            textSprite.rect = textSprite.image.get_rect()
            textRect = textSprite.rect
            textRect.x = 21
            textRect.y = 152 + lineNum * lineHeight
            self.game.AddToVisibleSpriteGroup(textSprite,3)
            self.textSprites.append(textSprite)
            lineNum += 1
        
    def Hide(self):
        self.sprite.kill()
        for textSprite in self.textSprites:
            textSprite.kill()
        self.game.textBoxOpen = False
        
    def SplitLineToFit(self, text, width):
        currentSize = self.font.size(text)
        newText = text.rsplit(" ",1)[0]
        while self.font.size(newText)[0] > width:
            newText = newText.rsplit(" ",1)[0]
        return (newText, text[len(newText):])

         
