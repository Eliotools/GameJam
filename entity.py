import math
import random
import pygame
from globals import *
from sprit import Sprit


class Entity:
  def __init__ (self, asset, pos, randKey=False):
    self.sprit = Sprit(asset[0],randKey, asset[1])
    self.type = asset[2]
    self.pos = pos
    self.direction = Direction.LEFT
    self.dead = False

  def getCenterPos(self):
    return self.pos[0] + self.sprit.size[0],self.pos[1] + self.sprit.size[1]

  def getBox(self):
    return self.pos, (self.pos[0]+ self.sprit.size[0],self.pos[1]+ self.sprit.size[1])

  def kill(self, entities):
    if (self.dead is True):
      entities[entities.index(self)] = Grave(self.pos)
    return
  
  def draw(self, screen):
      sprite = self.sprit.entity if self.direction == Direction.RIGHT else self.sprit.reversed
      screen.blit(sprite[self.sprit.key], self.pos)

  def action(self, entities):
    return 0,0
  
  def move(self, entities):
    pos = self.action(entities)
    if (pos == None):
      return
    self.direction = Direction.LEFT if pos[0] < 0 else Direction.RIGHT
    self.pos = self.pos[0] + pos[0], self.pos[1] + pos[1]
 
class Fireball(Entity):
    def __init__(self, pos, angle=0):
      super().__init__(FirballAsset, pos, randKey=False)
      self.primaryAngle = angle
      self.deadSprit = Sprit(DeadFirballAsset[0],False, DeadFirballAsset[1] )
      self.angle = 0
      self.life = 50

    def kill(self, entities):
      if (self.life <= 0) :
        entities.remove(self)

    def action(self, entities):
        pos = self.getCenterPos()
        playerPos = list(filter(lambda x:x.type == Type.Player, entities))[0].getCenterPos()
        x,y = 0,0
        if (playerPos[0] >= pos[0]+10):
            x = 3
        elif (playerPos[0] < pos[0]-10):
            x = - 3
        if (playerPos[1] >= pos[1]+10):
          y =  3
        elif (playerPos[1] < pos[1]-10):
          y = - 3
        return x ,y

    def move(self, entities):
      self.life -= 1
      player = list(filter(lambda x:x.type == Type.Player, entities))[0]
      playerPos = player.getCenterPos()
      pos = self.action(entities)
      if (checkColEntity(player.getBox(), self.getBox() )):
        player.dead = True
      if (pos == None):
        return
      for tree in  list(filter(lambda x:x.type == Type.Tree, entities)) :
        if (checkColEntity(self.getBox(), tree.getBox())):
          tree.burning()
      self.pos = self.pos[0] + pos[0], self.pos[1] + pos[1]
      if self.pos[0] != playerPos[0]:
        dx = playerPos[0] - self.pos[0]
        dy = playerPos[1] - self.pos[1]
        self.angle = -math.degrees(math.atan2(dy, dx)) + self.primaryAngle
        
    def draw(self, screen):
      sprite = self.sprit if self.life > 10 else self.deadSprit
      res = pygame.transform.rotate(sprite.entity[self.sprit.key], self.angle)  
      screen.blit(res, self.pos)

class Demon(Entity):
  def __init__(self, pos):
    super().__init__(DemonAsset, pos, randKey=False)
    self.sprit = Sprit(SmockAsset[0], False, SmockAsset[1])
    self.change = False

  def move(self, entities):
    if (self.sprit.key == 0):
      self.sprit = Sprit(DemonAsset[0], False, DemonAsset[1])
    pos = self.action(entities)
    self.direction = Direction.LEFT  if pos[0] < 0 else Direction.RIGHT
    if (pos == None):
      return
    self.pos = self.pos[0] + pos[0], self.pos[1] + pos[1]

  def action(self, entities):
    pos = self.getCenterPos()
    playerPos = list(filter(lambda x:x.type == Type.Player, entities))[0].getCenterPos()
    dist = math.sqrt(math.pow(pos[0] - playerPos[0],2) + math.pow(pos[1] - playerPos[1],2))
    if (dist < 200 and random.randint(0, 100) < 3) :
        entities.append(Fireball(self.getCenterPos(), +90))
      
    index = random.randint(0, 5)
    if index == 0:
      return 0,1
    elif index == 1:
      return 0,-1
    elif index == 2:
      return 1,0
    elif index == 3:
      return -1,0
    else :
      return 0,0
      
class Player(Entity):
  def __init__(self):
    super().__init__(PlayerAsset, (SCREEN_WIDTH/2, SCREEN_HEIGHT / 2))
    self.spellTimeout = 0
    self.coinCount = 0
    
  
  def action(self, entities):
    self.spellTimeout = self.spellTimeout-1 if self.spellTimeout > 0 else 0
    click = pygame.mouse.get_pressed()[0]
    key = pygame.mouse.get_pos()
    pos = self.getCenterPos()
    dist = (3 if click else 1)
    x,y = 0,0
    if (key[0] >= pos[0]+10):
       x += dist
    elif (key[0] < pos[0]-10):
        x -= dist
    if (key[1] >= pos[1]+10):
       y += dist
    elif (key[1] < pos[1]-10):
       y -= dist
    return x,y
  
  def kill(self, entities):
    pass

class Tree(Entity):
  def __init__(self, pos):
    super().__init__(TreeAsset, pos, randKey=True)
    self.burningSprite =  Sprit(BurnignTreeAsset[0], False, BurnignTreeAsset[1])
    self.buring = 0
    
  def burning(self):
    self.sprit = self.burningSprite
    self.buring = 1
  
  def kill(self, entities):
     if (self.buring == 1 and self.sprit.key == 0):
        entities.remove(self)

class Coin(Entity):
  def __init__(self, pos):
    super().__init__(CoinAsset, pos, randKey=True)

  def action(self,entities):
      pos = self.getCenterPos()
      player =  list(filter(lambda x:x.type == Type.Player, entities))[0]
      playerPos =player.getCenterPos()

      dist = math.sqrt(math.pow(pos[0] - playerPos[0],2) + math.pow(pos[1] - playerPos[1],2))

      if (dist < 30): 
        player.coinCount += 1
        entities.remove(self)

      if (dist < 120):
        x,y = 0,0
        if (playerPos[0] >= pos[0]+10):
            x = 6
        elif (playerPos[0] < pos[0]-10):
            x = - 6
        if (playerPos[1] >= pos[1]+10):
          y =  6
        elif (playerPos[1] < pos[1]-10):
          y = - 6
        return x ,y
      return 0,0
  
class Lightning(Entity):
  def __init__(self, pos, target):
    super().__init__(LightningAsset, pos)
    self.life = True
    self.target = target
    self.pos = pos[0] - LightningAsset[1][0]/2, pos[1] - LightningAsset[1][1]

  def action(self, entities):
    self.life = False
    return 0,0
  
  def kill(self, entities):
    if (self.life == False and self.sprit.key == 0):
     
      self.target.dead = True
      entities.remove(self)

class Grave(Entity):
  def __init__(self, pos):
    super().__init__(GraveAsset, pos)
    self.frame = 0
    self.sprit = Sprit(SmockAsset[0], False, SmockAsset[1])
    self.secSprite = Sprit(GraveAsset[0], False, GraveAsset[1] )
  
  def action(self, entities):
    if (self.sprit.key == 0):
      self.sprit = self.secSprite
    return 0,0