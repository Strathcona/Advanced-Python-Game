import pygame 

class GameObject():    
    def __init__(self, game):
        self.name = ""
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("Images/Default.png")
        self.sprite.rect = self.sprite.image.get_rect()        
        self.game = game
        self.game.AddToVisibleSpriteGroup(self.sprite, 0)
        self.game.gameObjects.append(self)
        self.animationFrames = []
        self.animations = {}
        self.solid = True
        self.interactable = False
        self.updatesWhenTextBoxOpen = False
    
    def ChangeSpriteImage(self, newImage):
        x = self.sprite.rect.x
        y = self.sprite.rect.y
        self.sprite.image = newImage
        self.sprite.rect = self.sprite.image.get_rect()  
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    def Update(self):
        #pass here because our default gameObject doesn't update
        pass

    def Interact(self):
        pass

