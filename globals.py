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


PlayerAsset=["./assets/charactere/player/left.png", (PLAYER_WIDTH,PLAYER_HEIGHT), Type.Player, 1]
TreeAsset=["./assets/item/tree.png", (64,64), Type.Tree, 2]
BurnignTreeAsset=["./assets/item/treeBurning.png", (64,64), Type.Tree, 2]
SmockAsset=["./assets/item/smoke.png", (32,32), Type.Smock, 2]
CoinAsset=["./assets/item/coin.png", (20,20), Type.Coin, 2]
DemonAsset=["./assets/charactere/demon/left.png", (64,60), Type.Demon, 1]
FirballAsset=["./assets/fireballs/RedFireball/run.png", (15,15), Type.Fireball, 2]
DeadFirballAsset=["./assets/fireballs/RedFireball/dead.png", (15,15), Type.Fireball, 2]
LightningAsset=["./assets/item/lightning.png", (32,32), Type.Lightning, 2]
GraveAsset=["./assets/item/grave.png", (32,32), Type.Grave, 2]


def checkColEntity(entity1, entity2): 
      a = entity1.pos[0] < entity2.pos[0] and entity2.pos[0] < entity1.pos[0] + entity1.sprit.size[0]*2
      b = entity1.pos[0] < entity2.pos[0]+ entity2.sprit.size[0] and  entity2.pos[0]+ entity2.sprit.size[0] < entity1.pos[0] + entity1.sprit.size[0]*2
      c = entity1.pos[1] < entity2.pos[1] and entity2.pos[1] < entity1.pos[1] + entity1.sprit.size[1]*2
      d = entity1.pos[1] < entity2.pos[1]+ entity2.sprit.size[1] and  entity2.pos[1]+ entity2.sprit.size[1] < entity1.pos[1] + entity1.sprit.size[1]*2
      
      return  (a or b) and (c or d)

def checkColPos(entity1, pos): 
      a = entity1.pos[0] < pos[0] and pos[0] < entity1.pos[0] + entity1.sprit.size[0]*2
      c = entity1.pos[1] < pos[1] and pos[1] < entity1.pos[1] + entity1.sprit.size[1]*2
      
      return  a and c
     