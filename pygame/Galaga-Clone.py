import sys
import pygame
import time

BLACK = 0,0,0

######
#
#   Sprite Classes
#
######

class Player(pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/assets/player.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = xCoord
        self.rect.y = yCoord
        self.dx = 0
        self.lives = 5

    def update(self):
        self.rect.x += self.dx

        if self.rect.left < 0 or self.rect.right > width:
            self.stop()

    def get_rect(self):
        return self.rect

    def go_left(self):
        self.dx = -5

    def go_right(self):
        self.dx = 5

    def stop(self):
        self.dx = 0


class Laser(pygame.sprite.Sprite):
    def __init__(self, start_X, start_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/assets/laser.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = start_X
        self.rect.y = start_y
        self.dy = -20
        self.damage = 10

    def update(self):
        self.rect.y += self.dy

        if self.rect.top < 0 or self.rect.bottom > height + 50:
           self.kill()


class Minion(pygame.sprite.Sprite):
    def __init__(self, start_X, start_Y):
        super().__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/assets/minion.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = start_X
        self.rect.y = start_Y
        self.dx = 0
        self.dy = 0
        self.health = 25

    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False



######
#
#   Main game loop
#
######

def spawn_minions(amount):
    count = 0
    row_count = 0
    column_count = 0

    while count < amount:
        if column_count > 5:
            column_count = 0
            row_count += 1

        xCoord = (25 + (75 * column_count))  # spaces each minion out by 75 pixels into 5 columns
        yCoord = (100 * row_count)

        new_minion = Minion(xCoord, yCoord)
        all_sprite_list.add(new_minion)
        enemy_sprite_list.add(new_minion)
        count += 1
        column_count += 1

def player_fire_laser(curtime, all_sprites, player_lasers, placement):
    shot_time = pygame.time.get_ticks()
    #   Checks to see if 500 ms has passed between shots
    if shot_time - cur_time > 500:
        #   shoots laser from other side of ship
        if placement == 1:
            new_laser = Laser((player.rect.x + 15), player.rect.y)
            all_sprites.add(new_laser)
            player_lasers.add(new_laser)
            placement *= -1

        else:
            new_laser = Laser((player.rect.x + 35), player.rect.y)
            all_sprite_list.add(new_laser)
            player_laser_list.add(new_laser)
            placement *= -1

pygame.init()

#   Sprite groups
all_sprite_list = pygame.sprite.Group()
enemy_sprite_list = pygame.sprite.Group()
player_laser_list = pygame.sprite.Group()
enemy_laser_list = pygame.sprite.Group()

#   Sprites
player = Player(220, 600)
all_sprite_list.add(player)

size = width, height = 500, 750
screen = pygame.display.set_mode(size)
cur_time = pygame.time.get_ticks()
shot_placement = 1

spawn_minions(18)


# Animation loop
while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#   Checks key presses
        if event.type == pygame.KEYDOWN:

# -------------- Player presses shoot --------------
            if event.key == pygame.K_SPACE:
                player_fire_laser(cur_time, all_sprite_list, player_laser_list, shot_placement)
                #   Switches side of the ship laser is fired from
                shot_placement *= -1
# -------------- End shooting loop ---------------------

            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_LEFT:
                player.go_left()

        #   Checks for key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()


#   Animate everything on screen
    all_sprite_list.update()

#   Checks collision between player lasers and enemy sprites
    for laser in player_laser_list:
        block_hit_list = pygame.sprite.spritecollide(laser, enemy_sprite_list, True)

        for each in block_hit_list:
            each.health -= laser.damage

#   Checks if the enemy minion's health is low enough to remove it from the screen and the game
            if each.health <= 0:
                all_sprite_list.remove(each)
                player_laser_list.remove(laser)
                all_sprite_list.remove(laser)

            all_sprite_list.remove(laser)
            player_laser_list.remove(laser)

        if laser.rect.y < -50:
            player_laser_list.remove(laser)
            all_sprite_list.remove(laser)

    screen.fill(BLACK)
    all_sprite_list.draw(screen)
    clock.tick(120)
    pygame.display.flip()
