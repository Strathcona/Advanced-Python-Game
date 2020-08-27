import pygame
import time
import player 
import PlayerHealthBar
import uiCoinCounter
import room
import uitextbox


class Game():
        
    #Initialize our game, setting up the screen and the variables
    def __init__(self):
        self.screen = pygame.display.set_mode([256,256])
        self.visibleSpriteGroup = pygame.sprite.LayeredUpdates()
        self.gameObjects = []
        self.removedGameObjects = []
        self.currentRoom = [1,1,1]
        self.room = room.Room()
        self.textBoxOpen = False;
        pygame.init()
        self.Run()
        
    #Function to add sprites to the group that gets drawn on screens
    def AddToVisibleSpriteGroup(self, sprite, layer):
        self.visibleSpriteGroup.add(sprite, layer=layer)
        
    def RemoveGameObject(self, gameObject):
        self.removedGameObjects.append(gameObject)

    def DrawSprites(self):   
       #Clear the screen with a black fill
       bgColor = 0,172,55
       self.screen.fill(bgColor)
       #Draw sprites
       self.visibleSpriteGroup.draw(self.screen)
       #Put the current surface onto the display
    
    def DrawToDisplay(self):
       pygame.display.flip()

    #Calls the update function of our gameObjects
    def Update(self):
        for gameObject in self.gameObjects:
            if self.textBoxOpen :
                if gameObject.updatesWhenTextBoxOpen:
                    gameObject.Update()
            else:
                gameObject.Update()
        
    #Performs any clean up actions before the end of the frame    
    def CleanUp(self):
        for toRemove in self.removedGameObjects:
            if toRemove in self.gameObjects:
                self.gameObjects.remove(toRemove)
        self.removedGameObjects.clear()
       
    #Gets the first game object with the name
    def FindGameObject(self, name):
        for obj in self.gameObjects:
            if obj.name == name:
                return obj
        return None
    
    #Gets all game objects with the name
    def FindAllGameObjects(self, name):
        toReturn = []
        for obj in self.gameObjects:
            if obj.name == name:
                toReturn.append(obj)
        return toReturn
    
    #Finds all objects with the solid bool set to true
    def FindAllSolidGameObjects(self):
        toReturn = []
        for obj in self.gameObjects:
            if obj.solid == True:
                toReturn.append(obj)
        return toReturn

    def FindAllInteractableGameObjects(self):
        toReturn = []
        for obj in self.gameObjects:
            if obj.interactable == True:
                toReturn.append(obj)
        return toReturn
    
    #Finds and checks collision with objects named name
    def GetCollision(self, parentRect, name):
        objectsWithName = self.FindAllGameObjects(name)
        collisions = []
        for obj in objectsWithName:
            if parentRect != obj.sprite.rect:#can't collid with itself
                if parentRect.colliderect(obj.sprite.rect):
                    collisions.append(obj)
        return collisions
    
    #Finds collisions inside of a list of objects
    def GetCollisionWithObjects(self, parentRect, objects):
        collisions = []
        for obj in objects:
            if parentRect.colliderect(obj.sprite.rect):
                collisions.append(obj)
        return collisions
    
    def SetCurrentRoom(self,x,y,z):
        self.currentRoom[0] =x
        self.currentRoom[1] =y
        self.currentRoom[2] =z
        print(self.currentRoom)
        self.room.Clear()
        self.room.LoadRoomFromCSV(str(self.currentRoom[0])+','+str(self.currentRoom[1])+','+str(self.currentRoom[2]),self)
    
    def ChangeRoom(self):
        print(self.currentRoom)
        self.room.Clear()
        self.room.LoadRoomFromCSV(str(self.currentRoom[0])+','+str(self.currentRoom[1])+','+str(self.currentRoom[2]),self)
        
    def GameOver(self):
        gameOverSprite = pygame.sprite.Sprite()
        gameOverSprite.image = pygame.image.load("Images/GameOver.png")
        gameOverSprite.rect = gameOverSprite.image.get_rect() 
        self.AddToVisibleSpriteGroup(gameOverSprite,2)

    def Run(self):
        self.screen = pygame.display.set_mode([256,256])
        #Create our starting game objects

        player1 = player.Player(self)
        player1.sprite.rect.x = 126
        self.ChangeRoom()
        playerHealthBar = PlayerHealthBar.PlayerHealthBar()
        playerHealthBar.CreateHealthBar(self, player1.maxHealth)
        playerCoinCounter = uiCoinCounter.UICoinCounter(self)        
        textBox = uitextbox.UITextBox(self)
        
        #Main Game loop
        while True:
            time.sleep(0.016)
            #Sleep to avoid refreshing too fast
            
            #This part handles exiting the game by pressing the X on the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.Update()

            self.DrawSprites()
            playerCoinCounter.UpdateCoins(player1.coins)
            self.DrawToDisplay()
            
            #Check if our player has moved off the current room
            if player1.sprite.rect.x > 276:
                self.currentRoom[0] -= 1
                self.ChangeRoom()
                player1.sprite.rect.x = 0
            elif player1.sprite.rect.x < -20:
                self.currentRoom[0] += 1
                self.ChangeRoom()
                player1.sprite.rect.x = 256
            if player1.sprite.rect.y > 276:
                self.currentRoom[1] += 1     
                self.ChangeRoom()
                player1.sprite.rect.y = 0
            elif player1.sprite.rect.y < -20:
                self.currentRoom[1] -= 1
                self.ChangeRoom()
                player1.sprite.rect.y = 256

            playerHealthBar.UpdateHealth(player1.currentHealth)
            self.CleanUp()

            

            
game = Game()
