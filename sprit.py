import random
import pygame

class Sprit:
  def __init__(self, path, randKey, size=(10,10), scale=1 ):
      self.key = 0 if not randKey else -1
      self.size = size
      self.scale = scale
      self.entity = self.loadSprit(path, size[0], size[1])
      self.reversed = self.flip(self.entity)
         

  def flip(self, sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

 
  def update(self):
      self.key = (self.key + 1) % len(self.entity)

  def loadSprit(self, path, width, height):
    sprite_sheet = pygame.image.load(path).convert_alpha()

    sprites = []
    nbSprite = sprite_sheet.get_width() // width
    if (self.key == -1):
        self.key = random.randint(0, nbSprite-1)
    for i in range(nbSprite):
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(i * width, 0, width, height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale_by(surface, self.scale))
                
    return sprites