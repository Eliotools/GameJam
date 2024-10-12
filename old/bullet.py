import pygame, math, random,time

from globals import PROJ_COLOR


class Bullet:
    ANIMATION_DELAY = 50

    def __init__(self, x, y, width, height, speed, targetx, targety, load_sprite_sheets, flip):
        self.entity = pygame.Rect(x, y, width, height)
        self.direction = "left"
        self.animation_count = 0
        self.angle = math.atan2(targety-y, targetx-x)
        self.dx = math.cos(self.angle)*speed
        self.dy = math.sin(self.angle)*speed
        self.x = x
        self.y = y
        self.load_sprite_sheets = load_sprite_sheets
        self.flip = flip
        self.sprite = load_sprite_sheets("fireballs", "RedFireball", 16, 16, True)["idle_left"][0]

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.entity.x = int(self.x)
        self.entity.y = int(self.y)

        sprites = self.load_sprite_sheets("fireballs", "RedFireball", 16, 16, True)["idle_left"]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY % len(sprites))
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

    def draw(self, win):
        print(math.degrees(self.angle))
        win.blit(pygame.transform.rotate(self.sprite, math.degrees(self.angle)), (self.entity.x, self.entity.y))

    def check_shoot(self, enemy):
        if  ((
            self.entity.right <= enemy.entity.right and self.entity.right >= enemy.entity.left
             ) or (self.entity.left >= enemy.entity.left and self.entity.left <= enemy.entity.right
                   )) and ((self.entity.top >= enemy.entity.top and self.entity.top <= enemy.entity.bottom
                       ) or (self.entity.bottom <= enemy.entity.bottom and self.entity.bottom >= enemy.entity.top)): 
            enemy.hp -= 5
            return True
        return False
