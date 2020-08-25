import GameObject
import pygame

class Transport(GameObject.GameObject):
    
    def __init__(self,game):
        super(Transport,self).__init__(game)
        self.destination = [0,0,0]
        self.solid = False
        self.ChangeSpriteImage(pygame.image.load("Images/Doorway.png"))
        
    def SetDestination(self, destinationString):
        self.destination[0] = int(destinationString[1])
        self.destination[1] = int(destinationString[3])
        self.destination[2] = int(destinationString[5])
    
    def Update(self):
        collisions = self.game.GetCollision(self.sprite.rect, "Player")
        if len(collisions)  > 0:
            self.game.SetCurrentRoom(self.destination[0],self.destination[1],self.destination[2])