import sys
import pygame as py

class Birb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = py.image.load('assets/birb.png')
        self.rect = self.image.get_rect()
        self.rect.x = 125
        self.rect.y = 256
        self.dy = -5
        self.alive = True

    def flap(self):
        """Moves the bird up with player motion"""


    def update(self):
        self.rect.y += self.dy

    def get_rect(self):
        return self.rect
