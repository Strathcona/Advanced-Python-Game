import pygame
import GameObject
class Sword(GameObject.GameObject):
    #If we are currently swinging
    swinging = False
    #How long the sword swings for
    swingTime = 9
    swingTimer = 0
    
    def __init__(self, game):
        super(Sword,self).__init__(game)
        self.name = "Sword"
        self.damage = 1
        self.solid = False
        self.animationFrames = {
                        "SwordU1":pygame.image.load("Images/SwordU1.png"),
                        "SwordU2":pygame.image.load("Images/SwordU2.png"),
                        "SwordU3":pygame.image.load("Images/SwordU3.png"),

                        "SwordD1":pygame.image.load("Images/SwordD1.png"),
                        "SwordD2":pygame.image.load("Images/SwordD2.png"),
                        "SwordD3":pygame.image.load("Images/SwordD3.png"),
                        
                        "SwordL1":pygame.image.load("Images/SwordL1.png"),
                        "SwordL2":pygame.image.load("Images/SwordL2.png"),
                        "SwordL3":pygame.image.load("Images/SwordL3.png"),
                        
                        "SwordR1":pygame.image.load("Images/SwordR1.png"),
                        "SwordR2":pygame.image.load("Images/SwordR2.png"),
                        "SwordR3":pygame.image.load("Images/SwordR3.png"),
                        }
        self.animations = {"SwordU":["SwordU1","SwordU2","SwordU3"],
                           "SwordD":["SwordD1","SwordD2","SwordD3"],
                           "SwordR":["SwordR1","SwordR2","SwordR3"],
                           "SwordL":["SwordL1","SwordL2","SwordL3"]
                           }
        #Hide our sword at the start!
        self.currentAnimation = "SwordU1"
        #keep count of frames for animation
        self.frameCounter = 0
        #current animation frame is what image in the animation we are on
        self.currentAnimationFrame = 0
        #What direction our character is facing
        self.sprite.kill()

    def SetAnimation(self, animationName):
        if animationName in self.animations and self.currentAnimation != animationName:
            self.currentAnimation = animationName
            self.currentAnimationFrame = 0
            self.frameCounter = 0
        
    def Animate(self):
        framesPerAnimation = 3
        if(self.frameCounter > framesPerAnimation):
            self.currentAnimationFrame += 1
            self.frameCounter = 0
        self.frameCounter += 1
        #Reset our animation frame back to 0 if we reach the end of the animation
        if self.currentAnimationFrame > (len(self.animations[self.currentAnimation]) - 1):
            self.currentAnimationFrame = 0
            
        #animation frames takes a string from animations indexed by current frame to produce an image
        self.sprite.image = self.animationFrames[self.animations[self.currentAnimation][self.currentAnimationFrame]]
    
    def Use(self, facing):
        #Start swinging the sword
        if facing == "Up":
            self.SetAnimation("SwordU")
        if facing == "Down":
            self.SetAnimation("SwordD")
        if facing == "Left":
            self.SetAnimation("SwordL")
        if facing == "Right":
            self.SetAnimation("SwordR")

        self.swinging = True
        self.swingTimer = self.swingTime
        self.game.AddToVisibleSpriteGroup(self.sprite, 1)
        
    def Update(self):
        if self.swinging:
            self.Animate()

            collisions = self.game.GetCollision(self.sprite.rect, "Moblin")
            for collision in collisions:
                collision.TakeDamage(self.damage)
                
            self.swingTimer -= 1
            if self.swingTimer <= 0:
                self.swinging = False
                self.sprite.kill()
    