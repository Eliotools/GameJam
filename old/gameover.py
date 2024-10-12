import pygame
from globals import *

def gameover(screen, score):
    font = pygame.font.SysFont('inkfree',50)#try inkfree, georgia,impact,dubai,arial

    title = font.render('Game Over',True,(255,255,255))
    title_rect = title.get_rect()
    title_rect.center = (SCREEN_WIDTH * 0.5, title.get_height() * 2)

    score_txt = font.render("You scored " + str(score) + " points!!!",True,(255,255,255))
    score_rect = score_txt.get_rect()
    score_rect.center = (SCREEN_WIDTH * 0.5, score_txt.get_height() * 4)

    exit = font.render("Press any button to exit",True,(255,255,255))
    exit_rect = exit.get_rect()
    exit_rect.center = (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT - exit.get_height() * 2)

    run = True

    screen.fill((0,0,0))

    screen.blit(title, title_rect)
    screen.blit(score_txt, score_rect)
    screen.blit(exit, exit_rect)
    
    pygame.display.update()

    while(run):

        for event in pygame.event.get() : 
            if event.type == pygame.QUIT :
                run = False
            if event.type == pygame.KEYDOWN:
                run = False