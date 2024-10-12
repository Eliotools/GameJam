import pygame

BLUE = (159, 255, 245, 10)
BG = (34, 34, 59, 128)

class Hud():
  def __init__(self):
    self.barWidth = 100
    self.barHeight = 30
    

  def drawBar(self, stamina, screen):
    pygame.draw.rect(screen, BG, ( 50, 50, self.barWidth+10, self.barHeight+10))

    # Dessiner la barre de santé actuelle (verte, en fonction de la santé restante)
    pygame.draw.rect(screen, BLUE, (55, 55,  100 - (self.barWidth / 100 * stamina), self.barHeight))
