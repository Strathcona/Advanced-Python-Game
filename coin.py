import pygame 
import GameObject    
    
class Coin(GameObject.GameObject):
    
    def __init__(self, game):
        super(Coin, self).__init__(game)
        #Define a name, sprite, rect, and game and add it to visible objects
        self.name = "Coin"
        self.solid = False
        self.ChangeSpriteImage(pygame.image.load("Images/Coin.png"))
        
    def Update(self):
        collisions = self.game.GetCollision(self.sprite.rect, "Player")
        for collision in collisions:
            collision.coins += 1
            self.sprite.kill()
            print("Coin Collected!")
            self.game.RemoveGameObject(self)