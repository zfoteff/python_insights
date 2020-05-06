

import sys
import pygame
import time

class Sun(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord):
        super().__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sun.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = xCoord
        self.rect.y = yCoord
        self.dx = 1
        self.dy = 1

    def get_rect(self):
        return self.rect

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0 or self.rect.right > width:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > height:
            self.dy *= -1

class Player(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord):
        super().__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = xCoord
        self.rect.y = yCoord
        self.dx = 0
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0 or self.rect.right > width:
            self.stop()
        if self.rect.top < 0 or self.rect.bottom > height:
            self.stop()

    def get_rect(self):
        return self.rect

    def go_left(self):
        self.dx = -5

    def go_right(self):
        self.dx = 5

    def go_up(self):
        self.dy = -5

    def go_down(self):
        self.dy = 5

    def stop(self):
        self.dx = 0
        self.dy = 0



pygame.init()
sprite_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()


size = width, height = 500, 500
black = 0,0,0
screen = pygame.display.set_mode(size)

player = Player(100, 100)
sun1 = Sun(150, 250)
sprite_list.add(sun1)
sprite_list.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN: # key pressed
            # move player up when w key is pressed
            if event.key == pygame.K_w:
                player.go_up()

            # move player down when s key is pressed
            if event.key == pygame.K_s:
                player.go_down()

            # move player left when a key is pressed
            if event.key == pygame.K_a:
                player.go_left()

            # move player right when d key is pressed
            if event.key == pygame.K_d:
                player.go_right()

        if event.type == pygame.KEYUP:
            player.stop()

    for sprite in sprite_list:
        sprite.update()

    screen.fill(black)
    sprite_list.draw(screen)
    time.sleep(.06)
    pygame.display.flip()
