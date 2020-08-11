import pygame
import uiCoinIcon

class UICoinCounter():
    def __init__(self, game):
        self.game = game;
        self.font = pygame.font.Font("Roboto-Medium.ttf", 16)
        self.coinIcon = uiCoinIcon.UICoinIcon(self.game)
        self.coinIcon.sprite.rect.x = 216
         
    def UpdateCoins(self, currentCoins):
        text = self.font.render("x"+str(currentCoins),1,(255,255,255))
        textRect = text.get_rect()
        textRect.x = 236
        textRect.y = 0
        self.game.screen.blit(text,textRect)
