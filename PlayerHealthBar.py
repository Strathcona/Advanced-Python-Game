import UIHeart


class PlayerHealthBar():
    hearts = []
    xOffset = 16

    def CreateHealthBar(self, game, maxHealth):
        for i in range(maxHealth):
            heart = UIHeart.UIHeart(game)
            heart.sprite.rect.x = 0 + self.xOffset * i
            heart.sprite.rect.y = 0
            self.hearts.append(heart)
    
    def UpdateHealth(self, currentHealth):
        i = 0
        for heart in self.hearts:
            if currentHealth > 0:
                heart.ChangeSpriteImage(heart.fullSprite)
            else:
                heart.ChangeSpriteImage(heart.emptySprite)
            heart.sprite.rect.x = 0 + self.xOffset * i
            heart.sprite.rect.y = 0
            currentHealth -= 1
            i += 1
