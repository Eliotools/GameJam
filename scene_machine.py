import pygame
from globals import *
from render_machine import RenderMachine


class SceneMachine():
  def __init__(self):
    self.scene = [[]]
    self.index = 0,0

  def transition(self, direction, screen, entities):
    i = 0
    
    if direction == Direction.LEFT:
      func = lambda x:x < SCREEN_WIDTH - 20 - PLAYER_WIDTH
      offset = [1,0]
    elif direction == Direction.RIGHT:
      func = lambda x:x > SCREEN_WIDTH - 10 - PLAYER_WIDTH
      offset = [-1,0]
    elif direction == Direction.UP:
      func = lambda x:x > 10
      offset = [0,-1]
    elif direction == Direction.DOWN:
      func = lambda x:x < SCREEN_HEIGHT - 10 - PLAYER_HEIGHT
      offset = [0,1]
    while func(i):
      screen.fill((0,0,0))
      screen.blit(self.scene[self.index[0]][self.index[1]].background, (0,0)) 
      for entity in entities:
          entity.pos = entity.pos[0] + offset[0], entity.pos[1] + offset[1]
          entity.draw(screen)
      pygame.display.update() 
      i += 1

    self.appendScene(RenderMachine(screen, entities, 10, self.transition), direction)
    

  def appendScene(self, newScene, direction):
    if direction == Direction.LEFT:
      self.scene.insert(0, [newScene])
    elif direction == Direction.RIGHT:
        self.scene.append([newScene])
        self.index = self.index, self.index+1
    elif direction == Direction.UP:
         self.scene[self.index[0]].append([newScene])
    elif direction == Direction.DOWN:
      offset = [0,1]