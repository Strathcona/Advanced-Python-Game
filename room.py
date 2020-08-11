import moblin
import tree 
import coin
import stone
import signpost

class Room():        
    roomObjects = []
    
    def Clear(self):
        for obj in self.roomObjects:
            obj.sprite.kill()
            obj.game.RemoveGameObject(obj)
        self.roomObjects.clear()
    
    def LoadRoomFromCSV(self, fileName, game):
        lineStrings = []
        try:
            f = open("Text/"+fileName+".csv","r")
            lineStrings = f.readlines()
        except FileNotFoundError:
            print("Room"+fileName+" not found ")
            return
        f.close()
        xPosition = 0
        yPosition = 0
        #Keep track of signposts to enter data for each"
        signposts = []
        
        #Each line represents one row of our level data
        for line in lineStrings:
            if line[0] == '"':
                signposts.pop(0).text = line
                
            columns = line.split(',')
            for column in columns:#Each column is one instance of our level info
                #Check what our character is and create the appropriate object
                if column == '_':
                    pass
                elif column == 'T':
                    newTree = tree.Tree(game)
                    newTree.sprite.rect.x = xPosition
                    newTree.sprite.rect.y = yPosition
                    self.roomObjects.append(newTree)
                elif column == 'R':
                    newStone = stone.Stone(game)
                    newStone.sprite.rect.x = xPosition   
                    newStone.sprite.rect.y = yPosition
                    self.roomObjects.append(newStone)
                elif column == 'M':
                    newMoblin = moblin.Moblin(game)
                    newMoblin.sprite.rect.x = xPosition   
                    newMoblin.sprite.rect.y = yPosition
                    self.roomObjects.append(newMoblin)
                elif column == 'S':
                    newSignPost = signpost.SignPost(game)
                    newSignPost.sprite.rect.x = xPosition   
                    newSignPost.sprite.rect.y = yPosition
                    self.roomObjects.append(newSignPost)
                    signposts.append(newSignPost)
                xPosition += 16#Increment our position counters as we move on to the next character
            xPosition = 0
            yPosition += 16