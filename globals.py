from enum import Enum

import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 60
FRAME_DELAY = 40
SCREEN_BORDER = 20
COINCOUNT = 10
BACKGROUND_IMAGE = "assets/backgrounds/plain.png"
BACKGROUND_FLOWER_IMAGE = "assets/backgrounds/plain_flower_X.png"


PROJ_COLOR = (255, 0, 0)

class Direction(Enum):
  RIGHT=0
  UP=1
  DOWN=2
  LEFT=3
  
class Type(Enum):
  Player=0
  Tree=1
  Coin=2
  Demon=3
  Fireball=4
  Smock=5
  Lightning=6
  Grave=7


PlayerAsset=["./assets/charactere/player/left.png", (PLAYER_WIDTH,PLAYER_HEIGHT), Type.Player]
TreeAsset=["./assets/item/tree.png", (124,124), Type.Tree]
BurnignTreeAsset=["./assets/item/treeBurning.png", (124,124), Type.Tree]
SmockAsset=["./assets/item/smoke.png", (90,60), Type.Smock]
CoinAsset=["./assets/item/coin.png", (40,40), Type.Coin]
DemonAsset=["./assets/charactere/demon/left.png", (64,60), Type.Demon]
FirballAsset=["./assets/item/fireball.png", (30,30), Type.Fireball]
DeadFirballAsset=["./assets/item/fireball_dead.png", (30,30), Type.Fireball]
LightningAsset=["./assets/item/lightning.png", (128,128), Type.Lightning]
GraveAsset=["./assets/item/grave.png", (64,64), Type.Grave]


def checkColEntity(entity1, entity2): 
      print(entity1, entity2)
      x = lambda x: entity1[0][0] < x and x < entity1[1][0]
      y = lambda y: entity1[0][1] < y and y < entity1[1][1]

      a = x(entity2[1][0]) and y(entity2[1][1])
      b = x(entity2[0][0]) and y(entity2[1][1])
      c = x(entity2[0][0]) and y(entity2[0][1])
      d = x(entity2[1][0]) and y(entity2[0][1])

      return a or b or c or d
     
def checkColPos(entity1, pos): 
      x = entity1[0][0] <  pos[0] and pos[0] < entity1[1][0]
      y = entity1[0][1] <  pos[1] and pos[1] < entity1[1][1]
      
      return  x and y
     