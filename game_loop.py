from math import *
import pygame
from background import Background
from globals import *
from obstacle import Obstacle
from player import Player

class GameLoop : 
    def __init__(self, sprite_sheet_image, load_sprite_sheets, flip, settings) :
        self.enemy = []
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT, pygame.Rect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)), sprite_sheet_image, load_sprite_sheets, flip)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock =  pygame.time.Clock()
        self.fps = 120
        self.settings = settings
        self.offset = pygame.math.Vector2(0, 0)
        self.background = Background()

    def addEnemy(self, enemy) :
        self.enemy.append(enemy)

    def tick(self, tick) :
        res = False
        key = pygame.key.get_pressed()
        self.move(key)
        
        if (len(self.enemy) < MAX_ENEMY) : 
            self.addEnemy(Obstacle())

        if tick % 8 is 0 :
            for enemy in self.enemy : 
                enemy.updatePos(self.offset)
                res = self.player.check_col(enemy.entity)
                if res : 
                    print('returned')
                    return True
            self.getDammage()
            self.kill()
        return res
            

    def move(self, key) :
        if key[self.settings.up] == True or key[pygame.K_UP] == True:
            self.offset[1] += 1
        if key[self.settings.down] == True or key[pygame.K_DOWN] == True:
            self.offset[1] -= 1
        if key[self.settings.left] == True or key[pygame.K_LEFT] == True:
            self.offset[0] += 1
        if key[self.settings.right] == True  or key[pygame.K_RIGHT] == True:
            self.offset[0] -= 1


    def display(self, win) : 

        pygame.display.update()
        self.screen.fill((0,0,0))
        self.display_background()
        self.player.draw(win)
        for enemy in self.enemy :
            pygame.draw.rect(self.screen, enemy.getColor(), enemy.entity)
        self.clock.tick(self.fps)
      

    def display_background(self) :
        for tile in self.background.tiles:
            self.screen.blit(self.background.image, tuple(map(lambda i, j: i + j, tile, (self.offset[0], self.offset[1]))))

    def getDammage(self) : 
        for enemy in self.enemy : 
            dist =  sqrt((enemy.x - ( SCREEN_WIDTH/2 - self.offset[0]))**2 + (enemy.y - ( SCREEN_HEIGHT/2 - self.offset[1]))**2)
            if (dist < 150) : 
                enemy.hp -= 5

    def kill(self) : 
        for enemy in self.enemy:
            if enemy.hp <= 0:
                self.enemy.remove(enemy)
     


            