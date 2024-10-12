from math import *
import pygame
from background import Background
from globals import *
from obstacle import Obstacle
from player import Player
from bullet import Bullet

red = 255,0,0


class GameLoop : 
    def __init__(self, screen, load_sprite_sheets, flip, settings) :
        font = pygame.font.SysFont('inkfree',50)#try inkfree, georgia,impact,dubai,arial
        self.load_sprite_sheets = load_sprite_sheets
        self.flip = flip
        self.enemies = []
        self.proj = []
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, load_sprite_sheets, flip)
        self.clock =  pygame.time.Clock()
        self.fps = 120
        self.screen = screen
        self.settings = settings
        self.offset = pygame.math.Vector2(0, 0)
        self.background = Background(0, 0)
        self.bullet_cooldown = 0
        self.BULLET_COOLDOWN_TIME = 70
        self.score = 0
        self.score_text = font.render("Score:" + str(self.score) ,True,(255,255,255))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (SCREEN_WIDTH * 0.15, self.score_text.get_height() * 2)


    def addEnemy(self, enemy) :
        self.enemies.append(enemy)

    def tick(self, tick) :
        res = False
        key = pygame.key.get_pressed()
        self.move(key)
        self.background.move(key)
        
        if (len(self.enemies) < MAX_ENEMY) : 
            self.addEnemy(Obstacle(self.load_sprite_sheets, self.flip))
        self.bullet_cooldown = max(0, self.bullet_cooldown - 1)

        if self.bullet_cooldown == 0:
            self.create_bullet()
            self.bullet_cooldown = self.BULLET_COOLDOWN_TIME
        if tick % 8 is 0 :
            for proj in self.proj : 
                proj.move()
            for enemy in self.enemies : 
                enemy.updatePos(self.offset)
                res = self.player.check_col(enemy.entity)
                if res : 
                    return True
            for proj in self.proj :
                for enemy in self.enemies : 
                    proj.check_shoot(enemy)
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

    def display(self) :
        font = pygame.font.SysFont('inkfree',50)#try inkfree, georgia,impact,dubai,arial
        pygame.display.update()
        self.score_text = font.render("Score: " + str(self.score) ,True,(0,0,0))
        self.screen.fill((0,0,0))
        self.background.draw(self.screen)
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for proj in self.proj : 
            proj.draw(self.screen)
        self.screen.blit(self.score_text, self.score_rect)
        self.clock.tick(self.fps)

    def getDammage(self) : 
        for enemy in self.enemies : 
            dist =  sqrt((enemy.x - ( SCREEN_WIDTH/2 - self.offset[0]))**2 + (enemy.y - ( SCREEN_HEIGHT/2 - self.offset[1]))**2)
            if (dist < 150) : 
                enemy.hp -= 5

    def kill(self) : 
        for enemy in self.enemies:
            if enemy.hp <= 0:
                self.enemies.remove(enemy)
                self.score += 1

    def create_bullet(self) :
        enemy = self.Find_Near()
        if not enemy :
            return
        self.proj.append(Bullet(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2, 20,20, 20, enemy.x + self.offset[0] ,enemy.y + self.offset[1], self.load_sprite_sheets, self.flip))

    def Find_Near(self)  :
        if len(self.enemies) is 0 :
            return False
        res = self.enemies[0]
        for enemy in self.enemies :
            if res.dist > enemy.dist : 
                res = enemy
        return res
     


            