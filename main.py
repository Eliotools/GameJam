import math
from entity import Player
from globals import *
import pygame

from render_machine import RenderMachine


pygame.init()
pygame.font.init()

class SceneManager():
    def __init__(self):
      self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      self.player = Player()
      self.scenes = [[0 for i in range(10) ]for i in range(10)]
      self.index = 5,5
      self.run = True
      self.transitionFR = 0
      self.scenes[self.index[0]][self.index[1]] = RenderMachine(self.screen, [self.player], FRAME_DELAY, self.transition)
    def game(self):
      self.scenes[self.index[0]][self.index[1]].loop()

    def replace(self):
      self.player.pos = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
      self.game()
       

    def transition(self, direction):
      x,y = self.index
     
      current = self.scenes[self.index[0]][self.index[1]]
      if direction == Direction.LEFT:
        size = SCREEN_WIDTH
        offset = [1,0]
        if (x == 0):
          self.replace()
          return
        x = x-1 
      elif direction == Direction.RIGHT:
        size = SCREEN_WIDTH
        offset = [-1,0]
        if (x == 10):
          self.replace()
          return
        x +=  1
      elif direction == Direction.UP:
        offset = [0,1]
        size = SCREEN_HEIGHT
        if (y == 10):
          self.replace()
          return
        y +=  1
      elif direction == Direction.DOWN:
        offset = [0,-1]
        size = SCREEN_HEIGHT
        if (y == 0):
          self.replace()
          return
        y -= 1
      if (self.scenes[x][y] == 0):
        newScene = RenderMachine(self.screen, [self.player], FRAME_DELAY, self.transition)
      else :
        newScene = self.scenes[x][y]
      for entity in newScene.entities:
         if (type(entity) == Player):
                 continue
         entity.pos = entity.pos[0] - SCREEN_WIDTH*offset[0],entity.pos[1] - SCREEN_HEIGHT*offset[1],
      i, loop = 0,0
      loop=0
      # PLAYER OUT
      while True:
        current_time = pygame.time.get_ticks()
        if current_time - i > self.transitionFR*10:
          loop += 1
          i = current_time 
          self.screen.fill((0,0,0))
          self.screen.blit(current.background, (0,0)) 
          self.player.pos = self.player.pos[0] - offset[0], self.player.pos[1] - offset[1]
          for entity in current.entities:
            entity.draw(self.screen)
          pygame.display.update()
        if loop == PLAYER_WIDTH:
           break

      # SCREEN TRANSITION
      while True:
        current_time = pygame.time.get_ticks()
        if (loop > size):
           break
        if current_time - i > self.transitionFR:
          i = current_time 
          self.screen.fill((0,0,0))
          self.screen.blit(current.background, (offset[0]*loop, offset[1]*loop)) 
          self.screen.blit(newScene.background, (offset[0]*loop - SCREEN_WIDTH*offset[0], offset[1]*loop -  SCREEN_HEIGHT*offset[1])) 
          loop += 1 
          
          for entity in current.entities:
              if (type(entity) == Player):
                 continue
              entity.pos = entity.pos[0] + offset[0], entity.pos[1] + offset[1]
              entity.draw(self.screen)
          for entity in newScene.entities:
              if (type(entity) == Player):
                continue
              entity.pos = entity.pos[0]+offset[0], entity.pos[1]+offset[1]
              entity.draw(self.screen)

          pygame.display.update()

      # RESET SCREEN POS
      for entity in current.entities:
         if (type(entity) == Player):
                 continue
         entity.pos = entity.pos[0] - SCREEN_WIDTH*offset[0],entity.pos[1] - SCREEN_HEIGHT*offset[1],
      
      self.index = x,y
      self.scenes[self.index[0]][self.index[1]] = newScene
      self.player.pos =  self.player.pos[0] + (SCREEN_WIDTH*offset[0]) - (PLAYER_WIDTH*offset[0]), self.player.pos[1] + (SCREEN_HEIGHT*offset[1]) - (PLAYER_WIDTH*offset[1]),
      loop=0
      # PLAYER IN
      while True:
        current_time = pygame.time.get_ticks()
        if current_time - i > self.transitionFR*10:
          loop += 1
          i = current_time 
          self.screen.fill((0,0,0))
          self.screen.blit(newScene.background, (0,0)) 
          self.player.pos = self.player.pos[0] - offset[0], self.player.pos[1]- offset[1]

          for entity in newScene.entities:
            entity.draw(self.screen)
          pygame.display.update()
          
        if loop ==  PLAYER_WIDTH:
           break
      self.game()




run = True
sceneManager = SceneManager()

   
       

if __name__ == '__main__':
  
    sceneManager.game()
    print('end')
    pygame.quit()