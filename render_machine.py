import random
import pygame
from entity import Coin, Demon, Fireball, Lightning, Tree
from globals import *
from hud import Hud


class RenderMachine():
  def __init__(self, screen, entities, frame_delay, transition):
    self.background =  self.buildBg()
    self.entities = entities
    self.screen = screen
    self.player = entities[0]
    self.frame_delay = frame_delay
    self.last_update_time = pygame.time.get_ticks()
    self.transition = transition
    self.hud = Hud()
    self.font =  pygame.font.SysFont('inkfree',30)
    self.run = True
    for i in range(random.randint(2,10)):
      y = random.randint(CoinAsset[1][0] + SCREEN_BORDER , SCREEN_HEIGHT - CoinAsset[1][1] - SCREEN_BORDER)
      x = random.randint(CoinAsset[1][1] + SCREEN_BORDER, SCREEN_WIDTH - CoinAsset[1][0] - SCREEN_BORDER)
      self.entities.append(Coin((x, y)))
    for i in range(random.randint(2,10)):
      y = random.randint(TreeAsset[1][0]+ SCREEN_BORDER, SCREEN_HEIGHT - TreeAsset[1][1]- SCREEN_BORDER)
      x = random.randint(TreeAsset[1][1]+ SCREEN_BORDER, SCREEN_WIDTH - TreeAsset[1][0]- SCREEN_BORDER)
      self.entities.append(Tree((x, y)))

  def buildBg(self):
      bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
      backgroundImage = pygame.image.load(BACKGROUND_IMAGE)
      
      for x in range(0, SCREEN_WIDTH, backgroundImage.get_width()):
          for y in range(0, SCREEN_HEIGHT, backgroundImage.get_height()):
              rand = random.randint(0, 100)
              if rand < 5:
                  rand_img = random.randint(0, 3) 
                  flower_image = pygame.image.load(BACKGROUND_FLOWER_IMAGE.replace('X', str(rand_img)))
                  bg_surface.blit(flower_image, (x, y))
              else:
                  bg_surface.blit(backgroundImage, (x, y))

      return bg_surface
  

  def checkSummon(self, pos):
    demonList = list(filter(lambda x:x.type == Type.Demon, self.entities))
    for demon in demonList:
        if (pos[0] + 50 > demon.pos[0] and pos[0] - 50 < demon.pos[0]):
          return True
        if (pos[1] + 50 > demon.pos[1] and pos[1] - 50 < demon.pos[1]):
          return True
    return False

  def checkRoom(self):
    if (self.player.pos[0] < 0):
      self.transition(Direction.LEFT)
      self.run = False
    if (self.player.pos[0] > SCREEN_WIDTH - 2*PLAYER_WIDTH):
        self.transition(Direction.RIGHT)
        self.run = False
    if (self.player.pos[1] > SCREEN_HEIGHT - 2*PLAYER_HEIGHT):
        self.transition(Direction.DOWN)
        self.run = False
    if (self.player.pos[1] < 0):
        self.transition(Direction.UP)
        self.run = False
    
   
  def loop(self):
    while self.run:
      if self.player.dead:
        return('PLYAER')
      current_time = pygame.time.get_ticks()
      coinList = list(filter(lambda x:x.type == Type.Coin, self.entities))
      if (self.player.coinCount == COINCOUNT):
        return('COIN')

      index = random.randint(0,5000)
      if (index < 10):
        if(len(coinList) != 0 and not self.checkSummon(coinList[index % len(coinList)].pos)):
          self.entities.append(Demon(coinList[index % len(coinList)].pos))
         
      for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            return('QUIT')
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.player.spellTimeout == 0):
              pos = pygame.mouse.get_pos()
              for demon in list(filter(lambda x:x.type == Type.Demon, self.entities)):
                if (checkColPos(demon.getBox(), pos)):
                    self.player.spellTimeout = 100
      if current_time - self.last_update_time > self.frame_delay:
          self.last_update_time = current_time 
          self.screen.fill((0,0,0))
          self.screen.blit(self.background, (0,0)) 
          self.entities.sort(key=lambda x: x.pos[1] + 2 * x.sprit.size[1]) 
          
          for entity in self.entities :
            entity.sprit.update()
            entity.move(self.entities)
            entity.kill(self.entities)
            entity.draw(self.screen)
          self.hud.drawBar(self.player.spellTimeout, self.screen)
          countText = self.font.render(f'Coin: {self.player.coinCount}/{COINCOUNT}', True, (0,0,0))
          self.screen.blit(countText, (50, 90))
          self.checkRoom()

      pygame.display.update()
  