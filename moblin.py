import pygame 
import GameObject    
import random
import coin

class Moblin(GameObject.GameObject):
    
    def __init__(self, game):
        super(Moblin,self).__init__(game)      
        self.name = "Moblin"
        self.solid = False
        self.animationFrames = {
                        "MoblinD1":pygame.image.load("Images/MoblinD1.png"),
                        }
        
        self.ChangeSpriteImage(self.animationFrames["MoblinD1"])
        self.health = 10
        #The target is who the enemy is chasing!
        self.damage = 1
        self.target = self.game.FindGameObject("Player")
        
    def Update(self):
        #Check the x and y position of our target and move towards them!
        if self.target.sprite.rect.x > self.sprite.rect.x:
            self.sprite.rect.x += 1
        elif self.target.sprite.rect.x < self.sprite.rect.x:
            self.sprite.rect.x -= 1
            
        if self.target.sprite.rect.y > self.sprite.rect.y:
            self.sprite.rect.y += 1
        elif self.target.sprite.rect.y < self.sprite.rect.y:
            self.sprite.rect.y -= 1
        
        collisions = self.game.GetCollision(self.sprite.rect, "Player")
        for collision in collisions:
            collision.TakeDamage(self.damage)
        
    def TakeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.sprite.kill()
            print("Moblin died!")
            self.game.RemoveGameObject(self)
            if random.random() > 0.5:#50% to drop a coin
                coin1 = coin.Coin(self.game)
                coin1.sprite.rect.x = self.sprite.rect.x
                coin1.sprite.rect.y = self.sprite.rect.y
                