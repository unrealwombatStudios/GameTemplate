import pygame as pg
import random
import math
import os

from Constants import *

class Player(pg.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        self.image = pg.Surface((32,32))
        self.image.fill(RED)
        # make image transparent where nothing is drawn
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def update(self):
        pass
