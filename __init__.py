import pygame
from pygame.locals import *
from sys import exit

from src.core.Player import Player
from src.config.constants import *

pygame.init()

screen_width = 512
screen_length = 500

screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption('PyFrogger')

sprites = pygame.sprite.Group()

player = Player(sprite_dir=FROG_SPRITES_DIR, player_speed=PLAYER_SPEED)
sprites.add(player)

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    screen.fill(BLACK_COLOR)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if keys[pygame.K_s]:
            if player.animate == False:
                player.down()
        if keys[pygame.K_w]:
            if player.animate == False:
                player.up()
        if keys[pygame.K_a]:
            if player.animate == False:
                player.left()
        if keys[pygame.K_d]:
            if player.animate == False:
                player.right()

    screen.blit(player.image, player.position())
    sprites.draw(screen)
    sprites.update()

    pygame.display.flip()