import pygame 
import sword
import GameObject

class Player(GameObject.GameObject):
    
    def __init__(self, game):
        super(Player,self).__init__(game)
        self.maxHealth = 5
        self.currentHealth = 5
        self.name = "Player"
        self.solid = False
        #How many coins the player has collected
        self.coins = 0
        self.invincibilityFrames = 30
        self.invincibilityTimer = 0
        #This dictionary stores images and is index with strings
        self.animationFrames = {"CharacterD1":pygame.image.load("Images/CharacterD1.png"),
                                "CharacterD2":pygame.image.load("Images/CharacterD2.png"),
                                "CharacterU1":pygame.image.load("Images/CharacterU1.png"),
                                "CharacterU2":pygame.image.load("Images/CharacterU2.png"),
                                "CharacterL1":pygame.image.load("Images/CharacterL1.png"),
                                "CharacterL2":pygame.image.load("Images/CharacterL2.png"),
                                "CharacterR1":pygame.image.load("Images/CharacterR1.png"),
                                "CharacterR2":pygame.image.load("Images/CharacterR2.png")
                                }
        #This dictionary stores animations as lists of strings that correspond to the animationFrames dictionary
        self.animations = {"WalkL":["CharacterL1","CharacterL2"],
                           "WalkU":["CharacterU1","CharacterU2"],
                           "WalkR":["CharacterR1","CharacterR2"],
                           "WalkD":["CharacterD1","CharacterD2"],
                           "StandD":["CharacterD1"],
                           "StandU":["CharacterU1"],
                           "StandL":["CharacterL1"],
                           "StandR":["CharacterR1"],
                           }
        #Key animation Variables
        #current animation stores what animation is playing right now
        self.currentAnimation = "WalkD"
        #keep count of frames for animation
        self.frameCounter = 0
        #current animation frame is what image in the animation we are on
        self.currentAnimationFrame = 0
        #What direction our character is facing
        self.facing = "Down"
        self.holdingOffset = (0,0)
                
        self.sword = sword.Sword(self.game)
        #what we are currently holding
        self.holding = self.sword
        
    def TakeDamage(self, amount):
        if self.invincibilityTimer == 0:
            self.invincibilityTimer = self.invincibilityFrames
            self.currentHealth -= amount
            if self.currentHealth <= 0:
                self.sprite.kill()
                self.game.RemoveGameObject(self)
                self.game.GameOver()
                
    def AddHealth(self, amount):
        if amount + self.currentHealth <= self.maxHealth:
            self.currentHealth += amount

    def SetAnimation(self, animationName):
        if animationName in self.animations and self.currentAnimation != animationName:
            self.currentAnimation = animationName
            self.currentAnimationFrame = 0
            self.frameCounter = 0
        
    def Animate(self):
        framesPerAnimation = 16
        if(self.frameCounter > framesPerAnimation):
            self.currentAnimationFrame += 1
            self.frameCounter = 0
        self.frameCounter += 1
        #Reset our animation frame back to 0 if we reach the end of the animation
        if self.currentAnimationFrame > (len(self.animations[self.currentAnimation]) - 1):
            self.currentAnimationFrame = 0
            
        #animation frames takes a string from animations indexed by current frame to produce an image
        self.sprite.image = self.animationFrames[self.animations[self.currentAnimation][self.currentAnimationFrame]]
    
    def Update(self): 
        
        #Update invincibility frames
        if self.invincibilityTimer > 0:
            self.invincibilityTimer -= 1
        
        #Change our character's position based on key presses
        keysPressed = pygame.key.get_pressed()
        walking = False
        
        #Keep track of what directions we're moving. Useful for collisions
        #use these instead of facing because we can be moving in multiple directions
        up = False
        down = False
        left = False
        right = False 
        #Check each key if it's pressed and move accordingly
        xVelocity = 0
        yVelocity = 0
        
        #Y movement and collision
        if keysPressed[pygame.K_w]:
            walking = True
            up = True
            self.facing = "Up"
            self.holdingOffset = (0,-12)
            self.SetAnimation("WalkU")
            yVelocity = -2
        if keysPressed[pygame.K_s]:
            walking = True
            down = True
            self.facing = "Down"
            self.holdingOffset = (0,12)
            self.SetAnimation("WalkD")
            yVelocity = 2
        
        self.sprite.rect.y += yVelocity
        self.HandleCollisionY(yVelocity)
        
        #X movement and collision
        if keysPressed[pygame.K_a]:
            walking = True
            left = True
            self.facing = "Left"
            self.holdingOffset = (-12,0)
            self.SetAnimation("WalkL")
            xVelocity = -2
        if keysPressed[pygame.K_d]:
            walking = True
            right = True
            self.facing = "Right"
            self.holdingOffset = (12,0)
            self.SetAnimation("WalkR")
            xVelocity = 2
        
        self.sprite.rect.x += xVelocity
        self.HandleCollisionX(xVelocity)     
        
        if not walking:
            if self.facing == "Up":
                self.SetAnimation("StandU")
            if self.facing == "Down":
                self.SetAnimation("StandD")
            if self.facing == "Left":
                self.SetAnimation("StandL")
            if self.facing == "Right":
                self.SetAnimation("StandR")

        #Update our held object's position
        self.holding.sprite.rect.x = self.sprite.rect.x + self.holdingOffset[0]
        self.holding.sprite.rect.y = self.sprite.rect.y + self.holdingOffset[1]           

        if keysPressed[pygame.K_SPACE]:
            self.holding.Use(self.facing)
        self.Animate()
        
            
    def HandleCollisionX(self, XMovement):
        #We find all objects we could collide into
        solidObjects = self.game.FindAllSolidGameObjects()
        for obj in self.game.GetCollisionWithObjects(self.sprite.rect, solidObjects):
            while self.sprite.rect.colliderect(obj.sprite.rect):
                if XMovement > 0:
                    self.sprite.rect.x -= 1
                else:
                    self.sprite.rect.x += 1
            
            
    def HandleCollisionY(self, YMovement):
        solidObjects = self.game.FindAllSolidGameObjects()
        for obj in self.game.GetCollisionWithObjects(self.sprite.rect, solidObjects):
            while self.sprite.rect.colliderect(obj.sprite.rect):
                if YMovement > 0:
                    self.sprite.rect.y -= 1
                else:
                    self.sprite.rect.y += 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            