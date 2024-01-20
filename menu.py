from globals import *
import pygame
from button import *
from game import *
from os import listdir
from os.path import isfile, join
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('inkfree',30,italic=True,bold=True)#try inkfree, georgia,impact,dubai,arial

font.set_underline(True)

pygame.Rect((400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)).bottomleft


sprite_sheet_image = pygame.image.load('./assets/characters/MiniNobleMan.png').convert_alpha()

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction = False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    
    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))
                
        if direction:
            all_sprites[image.replace('.png', '') + '_right'] = sprites
            all_sprites[image.replace('.png', '') + '_left'] = flip(sprites)
        else:
            all_sprites[image.replace('.png', '')] = sprites
                
    return all_sprites

def main_menu():
    run = True

    play_img = pygame.image.load("./assets/buttons/menu/large/regular/Play.png").convert_alpha()
    play_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Play.png").convert_alpha()
    button_scale = (play_img.get_height() / SCREEN_HEIGHT) * 2

    button_space = play_img.get_height() * 0.75
    play_button_height = (SCREEN_HEIGHT / 4)
    play_button = Button(SCREEN_WIDTH * 0.5, play_button_height, play_img, play_img_colored, button_scale)
    play_button.selected = True

    settings_img = pygame.image.load("./assets/buttons/menu/large/regular/Settings.png").convert_alpha()
    settings_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Settings.png").convert_alpha()
    settings_button_height = play_button_height + button_space
    settings_button = Button(SCREEN_WIDTH * 0.5, settings_button_height, settings_img, settings_img_colored, button_scale)

    quit_img = pygame.image.load("./assets/buttons/menu/large/regular/Quit.png").convert_alpha()
    quit_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Quit.png").convert_alpha()
    quit_button_height = settings_button_height + button_space
    quit_button = Button(SCREEN_WIDTH * 0.5, quit_button_height, quit_img, quit_img_colored, button_scale)

    buttons = [play_button, settings_button, quit_button]

    settings = Settings()

    while run:
        screen.fill((0,0,0))
        
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT :
                run = False

        for menu_button in buttons:
            action = menu_button.draw(screen)
            if (action and quit_button.selected):
                run = False
            if (action and play_button.selected):
                launch_game(screen, sprite_sheet_image, load_sprite_sheets, flip, settings)
            if (action and settings_button.selected):
                settings.menu(screen)
        pygame.display.update()

if __name__ == '__main__':
    main_menu()
    pygame.quit()