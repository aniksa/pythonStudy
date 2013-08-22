import pygame
import math
from defines import *

healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

def draw_clock(screen):
    font = pygame.font.Font(None, 24)
    time = time_limit-pygame.time.get_ticks()
    if time <= 0:
        time = 0
    survivedtext = font.render(str(time/60000)+":"+str(time/1000%60).zfill(2), True,(0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635,5]
    screen.blit(survivedtext,textRect)

def draw_healthbar(screen):
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue[0]):
        screen.blit(health,(health1+8,8))

def show_final(screen, accuracy, exitcode):
    pygame.font.init()
    font = pygame.font.Font(None,24)
    text = font.render("Accuracy: "+str(round(accuracy,2))+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    if exitcode == 1:
        screen.blit(youwin, (0,0))
    else:
        screen.blit(gameover, (0,0))
    screen.blit(text, textRect)