import pygame
import GameObject
class Sword(GameObject.GameObject):
    #If we are currently swinging
    swinging = False
    #How long the sword swings for
    swingTime = 10
    swingTimer = 0
    
    def __init__(self, game):
        super(Sword,self).__init__(game)
        self.name = "Sword"
        self.damage = 1
        self.solid = False
        self.animationFrames = {
                        "SwordU":pygame.image.load("Images/SwordU.png"),
                        "SwordD":pygame.image.load("Images/SwordD.png"),
                        "SwordL":pygame.image.load("Images/SwordL.png"),
                        "SwordR":pygame.image.load("Images/SwordR.png"),
                        }
        #Hide our sword at the start!
        self.sprite.kill()

    
    def Use(self, facing):
        #Start swinging the sword
        if facing == "Up":
            self.sprite.image = self.animationFrames["SwordU"]
        if facing == "Down":
            self.sprite.image = self.animationFrames["SwordD"]
        if facing == "Left":
            self.sprite.image = self.animationFrames["SwordL"]
        if facing == "Right":
            self.sprite.image = self.animationFrames["SwordR"]

        self.swinging = True
        self.swingTimer = self.swingTime
        self.game.AddToVisibleSpriteGroup(self.sprite, 1)
        
    def Update(self):
        if self.swinging:
            collisions = self.game.GetCollision(self.sprite.rect, "Moblin")
            for collision in collisions:
                collision.TakeDamage(self.damage)
                
            self.swingTimer -= 1
            if self.swingTimer <= 0:
                self.swinging = False
                self.sprite.kill()
    