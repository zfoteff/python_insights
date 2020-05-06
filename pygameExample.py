import sys, pygame
from pygame.locals import *
pygame.init()

width = 320
height = 240

size = width, height
dx = 2
dy = 2
speed = [dx,dy]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()


  ballrect =  ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    dx *= -1
  if ballrect.top < 0 or ballrect.bottom > height:
    dy *= -1

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()
