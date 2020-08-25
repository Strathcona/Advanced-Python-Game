import GameObject
import pygame
    
class Wall(GameObject.GameObject):    
    def __init__(self, game):
        super(Wall, self).__init__(game)
        self.name = "Wall"

    def SetWallSprite(self):
        up = False
        down = False
        left = False
        right = False
        '''
        #Check right and left
        self.sprite.rect.y -= 1
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:
            up = True
        self.sprite.rect.y += 2
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:
            down = True
        self.sprite.rect.y -= 1
        
        #Check up and down
        self.sprite.rect.x -= 1
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:
            left = True
        self.sprite.rect.x += 2
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:
            right = True
        '''
        self.sprite.rect.x -= 1
        
        print(str(up)+str(down)+str(right)+str(left))
        if down and left:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallTR.png"))
        elif down and right:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallTL.png"))      
        elif up and right:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallBL.png"))  
        elif up and left:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallBR.png"))      
        else:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallT.png"))      



           