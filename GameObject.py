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
    
    def ChangeSpriteImage(self, newImage):
        self.sprite.image = newImage
        self.sprite.rect = self.sprite.image.get_rect()  

    def Update(self):
        #pass here because our default gameObject doesn't update
        pass


