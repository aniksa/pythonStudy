import pygame
import math
import random

import pygame._view
from Player import *
from interface import *
from pygame.locals import *


pygame.init()    

player = Player()
screen = pygame.display.set_mode((width,height))
arrows = []

badguys = [[640,100]]
badtimer = [100,0]
running, exitcode = 1,0

grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg = pygame.image.load("resources/images/badguy.png")
badguyimg1 = badguyimg

def key_switch(flag) :
    if event.key == K_w:
        keys['W_KEY'] = flag
    if event.key == K_a:
        keys['A_KEY'] = flag
    if event.key == K_s:
        keys['S_KEY'] = flag
    if event.key == K_d:
        keys['D_KEY'] = flag

def draw_scene() :
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*grass.get_width(),y*grass.get_height()))
    
    x, y = 0,0
    for y in range(numCastles):
        screen.blit(castle,(x,y*castle.get_height()+castleYOffset))
    
def draw_arrows():
    print "arrows draw"
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*arrow_speed
        vely = math.sin(bullet[0])*arrow_speed
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>width or bullet[2]<-64 or bullet[2]>height:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 180*(2-projectile[0]/math.pi))
            screen.blit(arrow1, (projectile[1], projectile[2]))

def attack_castle(index):
    badrect = pygame.Rect(badguyimg.get_rect());
    badrect.top = badguys[index][1]
    badrect.left =badguys[index][0]
    if badrect.left < 64:
        healthvalue[0] -= random.randint(5,20)
        print healthvalue
        badguys.pop(index)
        return True
    return False

def kill_badguys(index):
    index1 = 0
    print index
    badrect = pygame.Rect(badguyimg.get_rect());
    badrect.top = badguys[index][1]
    badrect.left = badguys[index][0]
    for bullet in arrows:
        bullrect = pygame.Rect(arrow.get_rect())
        bullrect.left = bullet[1]
        bullrect.top = bullet[2]
        if badrect.colliderect(bullrect):
            player.acc[0] += 1
            badguys.pop(index)
            arrows.pop(index1)
        index1+=1

def move_badguys(timer):
    timer[0]-=1
    if timer[0] == 0:
        badguys.append([640,random.randint(50,430)])
        print "badtimer append"
        timer[0] = 100 - timer[1]*2
        if timer[1] >= 35:
            timer[1] = 35
        else:
            timer[1] += 5
    index = 0
    for badguy in badguys:
        if badguy[0]<=-64:
            badguys.pop(index)
        badguy[0]-=7
        attacked = attack_castle(index)
        if not attacked:
            kill_badguys(index)
        index+=1

def draw_badguys() :
    for badguy in badguys:
        screen.blit(badguyimg,badguy)



while running:
    screen.fill(0)
    draw_scene()
    player.draw(screen)
    draw_arrows()
    move_badguys(badtimer)
    draw_badguys()   
    draw_clock(screen)
    draw_healthbar(screen)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            key_switch(True)
        if event.type == pygame.KEYUP:
            key_switch(False)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print "Mouse button down"
            mouse_position = pygame.mouse.get_pos()
            player.acc[1]+=1
            arrows.append([math.atan2(mouse_position[1]-(player.pos_rot[1]+32),mouse_position[0]-(player.pos_rot[0]+26)),player.pos_rot[0]+32,player.pos_rot[1]+32])

    player.move()
    if pygame.time.get_ticks()>=time_limit:
        running = 0
        exitcode = 1
    if healthvalue[0] <= 0:
        running = 0
        exitcode = 0
    if player.acc[1]!=0:
        accuracy = player.acc[0]*1.0/player.acc[1]*100
    else:
        accuracy = 0

    show_final(screen, accuracy, exitcode)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
    
    


