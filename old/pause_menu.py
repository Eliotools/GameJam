from button import *
from globals import *
import pygame

def pause_menu(screen):
    run = True
    main_menu = False

    font = pygame.font.SysFont('inkfree',50)#try inkfree, georgia,impact,dubai,arial
    text = font.render('Pause Menu',True,(255,255,255))
    textrect = text.get_rect()
    
    textrect.center = (SCREEN_WIDTH * 0.5, text.get_height() * 2)

    menu_img = pygame.image.load("./assets/buttons/menu/large/regular/Menu.png").convert_alpha()
    menu_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Menu.png").convert_alpha()
    button_scale = (menu_img.get_height() / SCREEN_HEIGHT) * 2

    button_space = menu_img.get_height() * 0.75
    menu_button_height = (SCREEN_HEIGHT / 3)
    menu_button = Button(SCREEN_WIDTH * 0.5, menu_button_height, menu_img, menu_img_colored, button_scale)
    menu_button.selected = True

    resume_img = pygame.image.load("./assets/buttons/menu/large/regular/Resume.png").convert_alpha()
    resume_img_colored = pygame.image.load("./assets/buttons/menu/large/colored/Resume.png").convert_alpha()
    resume_button_height = menu_button_height + button_space
    resume_button = Button(SCREEN_WIDTH * 0.5, resume_button_height, resume_img, resume_img_colored, button_scale)

    buttons = [menu_button, resume_button]

    while run:
        for button in buttons:
            action = button.draw(screen)
            if (action and menu_button.selected):
               run = False
               main_menu = True
            if (action and resume_button.selected):
               run = False
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT :
                run = False
                main_menu = True
        screen.blit(text, textrect)
        pygame.display.update()
    return main_menu