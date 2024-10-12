import pygame
from globals import *
from os import listdir
from os.path import isfile, join
import math

class Background(pygame.sprite.Sprite) :
    def __init__(self, x, y):
        self.image = pygame.image.load(join("assets", "backgrounds", BACKGROUND_IMAGE))
        _, _, self.width, self.height = self.image.get_rect()
        self.tiles = self.buildTiles()
        self.x = x
        self.y = y

    def draw(self, win):
        for tile in self.tiles:
            win.blit(self.image, tuple(map(lambda i, j: i - j, tile, (self.x, self.y))))
        
    def move(self, key):
        if key[pygame.K_z] == True or key[pygame.K_UP] == True:
            self.y -= 1
            if self.y % 16 == 0:
                self.generate_tile_inbound('up')
        if key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
            self.y += 1
            if self.y % 16 == 0:
                self.generate_tile_inbound('down')
        if key[pygame.K_q] == True or key[pygame.K_LEFT] == True:
            self.x -= 1
            if self.x % 16 == 0:
                self.generate_tile_inbound('left')
        if key[pygame.K_d] == True or key[pygame.K_RIGHT] == True:
            self.x += 1
            if self.x % 16 == 0:
                self.generate_tile_inbound('right')

    def buildTiles(self) :
        self.tiles = []
        for i in range(-1, SCREEN_WIDTH // self.width + 1):
            for j in range(-1, SCREEN_HEIGHT // self.height + 1):
                pos = (i * self.width, j * self.height)
                self.tiles.append(pos)

        return self.tiles
    
    def generate_tile_inbound(self, direction):
        max_x = max(self.tiles, key=lambda x: x[0])[0]
        min_x = min(self.tiles, key=lambda x: x[0])[0]
        max_y = max(self.tiles, key=lambda x: x[1])[1]
        min_y = min(self.tiles, key=lambda x: x[1])[1]

        if direction == 'up':
            self.tiles = [tile for tile in self.tiles if tile[1] != max_y]
            new_tuples = [(x, min_y - 16) for x in range(min_x, max_x + 1, 16)]
            self.tiles.extend(new_tuples)

        if direction == 'down':
            self.tiles = [tile for tile in self.tiles if tile[1] != min_y]
            new_tuples = [(x, max_y + 16) for x in range(min_x, max_x + 1, 16)]
            self.tiles.extend(new_tuples)
            
        if direction == 'left':
            self.tiles = [tile for tile in self.tiles if tile[0] != max_x]
            new_tuples = [(min_x - 16, y) for y in range(min_y, max_y + 1, 16)]
            self.tiles.extend(new_tuples)
            
        if direction == 'right':
            self.tiles = [tile for tile in self.tiles if tile[0] != min_x]
            new_tuples = [(max_x + 16, y) for y in range(min_y, max_y + 1, 16)]
            self.tiles.extend(new_tuples)
