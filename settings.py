from time import sleep
import pygame
from globals import *
from button import *

class Settings():
    def __init__(self):
        self.up = pygame.K_w
        self.down = pygame.K_s
        self.left = pygame.K_a
        self.right = pygame.K_d

    def menu(self, screen):
        not_allowed = [self.up, self.down, self.left, self.right, pygame.K_ESCAPE, pygame.K_SPACE]
        run = True

        font = pygame.font.SysFont('inkfree',50)#try inkfree, georgia,impact,dubai,arial
        text = font.render('Pause Menu',True,(255,255,255))
        textrect = text.get_rect()
        print (text.get_height())
        textrect.center = (SCREEN_WIDTH * 0.5, text.get_height() * 2)

        right_img = pygame.image.load("./assets/buttons/menu/square/regular/right.png").convert_alpha()
        right_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/right.png").convert_alpha()
        button_scale = (right_img.get_height() / SCREEN_HEIGHT) * 1.5

        font = pygame.font.SysFont('inkfree',50)#try inkfree, georgia,impact,dubai,arial

        keybinds_button_width = SCREEN_WIDTH * 0.15
        keybinds_text_width = keybinds_button_width + 200

        button_space = right_img.get_height() * 0.75
        right_button_height = (SCREEN_HEIGHT / 8)
        right_button = Button(keybinds_button_width, right_button_height, right_img, right_img_colored, button_scale)

        right_keybind = font.render(pygame.key.name(self.right),True,(255,255,255))
        right_textrect = text.get_rect()
        right_textrect.center = (keybinds_text_width, right_button_height)

        right_button.selected = True

        left_img = pygame.image.load("./assets/buttons/menu/square/regular/left.png").convert_alpha()
        left_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/left.png").convert_alpha()
        left_button_height = right_button_height + button_space
        left_button = Button(keybinds_button_width, left_button_height, left_img, left_img_colored, button_scale)

        left_keybind = font.render(pygame.key.name(self.left),True,(255,255,255))
        left_textrect = text.get_rect()
        left_textrect.center = (keybinds_text_width, left_button_height)

        up_img = pygame.image.load("./assets/buttons/menu/square/regular/up.png").convert_alpha()
        up_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/up.png").convert_alpha()
        up_button_height = left_button_height + button_space
        up_button = Button(keybinds_button_width, up_button_height, up_img, up_img_colored, button_scale)

        up_keybind = font.render(pygame.key.name(self.up),True,(255,255,255))
        up_textrect = text.get_rect()
        up_textrect.center = (keybinds_text_width, up_button_height)

        down_img = pygame.image.load("./assets/buttons/menu/square/regular/down.png").convert_alpha()
        down_img_colored = pygame.image.load("./assets/buttons/menu/square/colored/down.png").convert_alpha()
        down_button_height = up_button_height + button_space
        down_button = Button(keybinds_button_width, down_button_height, down_img, down_img_colored, button_scale)

        down_keybind = font.render(pygame.key.name(self.down),True,(255,255,255))
        down_textrect = text.get_rect()
        down_textrect.center = (keybinds_text_width, down_button_height)

        exit_img = pygame.image.load("./assets/buttons/menu/large/regular/exit.png").convert_alpha()
        exit_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/exit.png").convert_alpha()
        exit_button_height = SCREEN_HEIGHT - exit_img.get_height() * 0.25
        exit_button_width = SCREEN_WIDTH - exit_img.get_width() * 0.17
        exit_button = Button(exit_button_width, exit_button_height, exit_img, exit_img_colored, button_scale * 0.6)

        buttons = [right_button, left_button, up_button, down_button, exit_button]

        while run:
            screen.fill((0,0,0))
            down_keybind = font.render(pygame.key.name(self.down),True,(255,255,255))
            up_keybind = font.render(pygame.key.name(self.up),True,(255,255,255))
            left_keybind = font.render(pygame.key.name(self.left),True,(255,255,255))
            right_keybind = font.render(pygame.key.name(self.right),True,(255,255,255))
            not_allowed = [self.up, self.down, self.left, self.right, pygame.K_ESCAPE, pygame.K_SPACE]

            for button in buttons:
                action = button.draw(screen)
                if (action and right_button.selected):
                    set_keybind = True
                    while (set_keybind):
                        for event in pygame.event.get() :
                            if (event.type == pygame.KEYDOWN and event.key not in not_allowed):
                                self.right = event.key
                                set_keybind = False
                if (action and left_button.selected):
                    set_keybind = True
                    while (set_keybind):
                        for event in pygame.event.get() :
                            if (event.type == pygame.KEYDOWN and event.key not in not_allowed):
                                self.left = event.key
                                set_keybind = False
                if (action and up_button.selected):
                    set_keybind = True
                    while (set_keybind):
                        for event in pygame.event.get() :
                            if (event.type == pygame.KEYDOWN and event.key not in not_allowed):
                                self.up = event.key
                                set_keybind = False
                if (action and down_button.selected):
                    set_keybind = True
                    while (set_keybind):
                        for event in pygame.event.get() :
                            if (event.type == pygame.KEYDOWN and event.key not in not_allowed):
                                self.down = event.key
                                set_keybind = False
                if (action and exit_button.selected):
                    run = False
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT :
                    run = False

            screen.blit(right_keybind, right_textrect)
            screen.blit(left_keybind, left_textrect)
            screen.blit(down_keybind, down_textrect)
            screen.blit(up_keybind, up_textrect)
            
            pygame.display.update()
