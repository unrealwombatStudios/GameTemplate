import pygame as pg
import random
import math
import os

from Constants import *
from Player import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init() #init music
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("template")
        self.clock = pg.time.Clock()

        self.running = True

    def new(self):
        # Start a new Game
        self.all_sprites = pg.sprite.Group()
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            # keep lop running at right speed
            self.clock.tick(FPS)

            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - update
        self.all_sprites.update()

    def events(self):
        # Game loop - events
        # Process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type is pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game loop - renderscreen.fill(BLUE)
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # Game start screen
        pass

    def show_go_screen(self):
        # Game Over screen
        pass



g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
