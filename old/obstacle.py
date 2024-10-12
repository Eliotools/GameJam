from cmath import sqrt
from random import *
import pygame
from globals import *


class Obstacle: 
    def __init__(self, load_sprite_sheets, flip, offset=(0,0)) :
        self.x, self.y = START_POS[randint(0, 3)]
        self.x -= offset[0]
        self.y -= offset[1]
        self.entity = pygame.Rect(self.x, self.y, 32, 32)
        self.hp = 100
        self.dist = 10000
        self.direction = "left"
        self.animation_count = 0
        self.load_sprite_sheets = load_sprite_sheets
        self.flip = flip
        self.name = self.charette_or_monsieur(0.2)
        self.sprite = self.load_sprite_sheets("characters", self.name, 64 if self.name == "MiniCharette" else 32, 32, True)["idle_left"][0]
        self.speed = randint(0, MAX_SPEED) if self.name == "MiniNobleMan" else 8

    def draw(self, win):
        win.blit(self.sprite, (self.entity.x, self.entity.y))

    def charette_or_monsieur(self, charette_chance):
        if random() < charette_chance:
            return "MiniCharette"
        else:
            return "MiniNobleMan"

    def getDirection(self, offset) :
        sprite_sheet = "idle"
        if (self.x < offset[0]):
            sprite_sheet = "run"
            self.x += self.speed * 0.1
        if (self.x > offset[0]):
            sprite_sheet = "run"
            self.x -= self.speed
        if (self.y < offset[1]):
            sprite_sheet = "run"
            self.y += self.speed
        if (self.y > offset[1]):
            sprite_sheet = "run"
            self.y -= self.speed

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.load_sprite_sheets("characters", self.name, 64 if self.name == "MiniCharette" else 32, 32, True)[sprite_sheet_name]
        sprite_index = (self.animation_count // (round(self.speed) + 1) % len(sprites))
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

    def updatePos(self, offset) :
        self.getDirection([SCREEN_WIDTH/2 - offset[0] , SCREEN_HEIGHT/2 - offset[1]])
        x = self.x + offset[0]
        y = self.y + offset[1]
        self.entity.x = x
        self.entity.y = y
        self.dist =  sqrt((self.x - ( SCREEN_WIDTH/2 - offset[0]))**2 + (self.y - ( SCREEN_HEIGHT/2 - offset[1]))**2).real

    def getColor(self) : 
        if self.hp < 33 :
            return (255, 0, 0)
        elif self.hp < 66 :
            return (255, 255, 0)
        else :
            return (0, 255, 0)