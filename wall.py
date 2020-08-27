import GameObject
import pygame
    
class Wall(GameObject.GameObject):    
    def __init__(self, game):
        super(Wall, self).__init__(game)
        self.ChangeSpriteImage(pygame.image.load("Images/HouseWallT.png"))
        self.name = "Wall"
        self.wallDirection = "  "

    def SetWallSprite(self):
        up = False
        down = False
        left = False
        right = False
        
        neighbourIsLeft = False
        neighbourIsRight = False
        neighbourIsTop = False
        neighbourIsBottom = False
        
        #Check right and left
        self.sprite.rect.y -= 1
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:

            up = True
        self.sprite.rect.y += 2
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:
            down = True
            if walls[0].wallDirection[1] == "L":
                neighbourIsLeft = True
            elif walls[0].wallDirection[1] == "R":
                neighbourIsRight = True
        self.sprite.rect.y -= 1
        
        #Check up and down
        self.sprite.rect.x -= 1
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:
            left = True
            if walls[0].wallDirection[0] == "T":
                neighbourIsTop = True
            elif walls[0].wallDirection[0] == "B":
                neighbourIsBottom = True
        self.sprite.rect.x += 2
        walls = self.game.GetCollision(self.sprite.rect, "Wall")
        if len(walls) > 0:
            right = True
            if walls[0].wallDirection[0] == "T":
                neighbourIsTop = True
            elif walls[0].wallDirection[0] == "B":
                neighbourIsBottom = True
        self.sprite.rect.x -= 1
        
        #Set our image to one of the eight options depending on the neighbours
        if down and left:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallTR.png"))
            self.wallDirection = "TR"
        elif down and right:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallTL.png"))  
            self.wallDirection = "TL"
        elif up and right:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallBL.png"))  
            self.wallDirection = "BL"
        elif up and left:
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallBR.png")) 
            self.wallDirection = "BR"
        elif up and down:
            if neighbourIsLeft:                    
                self.ChangeSpriteImage(pygame.image.load("Images/HouseWallL.png"))  
                self.wallDirection = " L"
            elif neighbourIsRight:
                self.ChangeSpriteImage(pygame.image.load("Images/HouseWallR.png"))  
                self.wallDirection = " R"
        elif left and right:
            if neighbourIsTop:                    
                self.ChangeSpriteImage(pygame.image.load("Images/HouseWallT.png"))  
                self.wallDirection = "T "
            elif neighbourIsBottom:
                self.ChangeSpriteImage(pygame.image.load("Images/HouseWallB.png"))  
                self.wallDirection = "B "
        else:#Just in case
            print("default")
            self.ChangeSpriteImage(pygame.image.load("Images/HouseWallB.png"))  
            self.wallDirection = "  "
                
