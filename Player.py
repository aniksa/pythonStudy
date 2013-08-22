import pygame
import math
from defines import *

class Player(object):
    """represents a player, attributes: pos, pos_rot, tile, step, rot"""
    def  __init__(self, pos=player_pos, step=player_step):
        self.pos = pos
        self.step = step
        self.tile = pygame.image.load("resources/images/dude.png")
        self.acc = [0,0]
    
    def draw(self,screen) :
        mouse_position = pygame.mouse.get_pos()
        player_rect = [self.tile.get_rect().width, self.tile.get_rect().height];
        angle = math.atan2(mouse_position[1] - (self.pos[1]+player_rect[1]), mouse_position[0]-(self.pos[0]+player_rect[0]))
        
        self.rot = pygame.transform.rotate(self.tile, 180*(2-angle/math.pi))
        player_rot_rect = [self.rot.get_rect().width, self.rot.get_rect().height];
        self.pos_rot = (self.pos[0]-player_rot_rect[0]/2, self.pos[1]-player_rot_rect[1]/2)
        
        screen.blit(self.rot,self.pos_rot)
    
    def move(self) :
        if keys['W_KEY']:
            self.pos[1] -= self.step
        if keys['A_KEY']:
            self.pos[0] -= self.step
        if keys['S_KEY']:
            self.pos[1] += self.step
        if keys['D_KEY']:
            self.pos[0] += self.step
