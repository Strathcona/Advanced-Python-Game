import pygame 

class UIObject():    
    def __init__(self, game):
        self.name = ""
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load("Images/Default.png")
        self.sprite.rect = self.sprite.image.get_rect()        
        self.game = game
        self.game.AddToVisibleSpriteGroup(self.sprite, 1)
        self.game.gameObjects.append(self)
        self.solid = False
    
    def ChangeSpriteImage(self, newImage):
        self.sprite.image = newImage
        self.sprite.rect = self.sprite.image.get_rect()  

    def Update(self):
        #pass here because our default gameObject doesn't update
        pass


