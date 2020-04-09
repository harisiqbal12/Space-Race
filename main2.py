import pygame
from pygame import *
import os
import sys
import math

pygame.init()

W, H = 1280, 720
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space-Race V-1.0")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
bg = pygame.image.load(os.path.join('Background(1)_art1.jpg')).convert()
bgX = 0
bgX2 = bg.get_width()
clock = pygame.time.Clock()

# Player
PlayerIMG = pygame.image.load('spaceship (1).png')
PlayerX = 20
PlayerY = 250
Player_ChangeX = 0
Player_ChangeY = 0


# FX

def Player(x, y):
    win.blit(PlayerIMG, (x, y))


def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    Player(PlayerX, PlayerY)
    pygame.display.update()



pygame.time.set_timer(USEREVENT + 1, 500)
speed = 60
running = True
# Game Loop
while running:
    redrawWindow()
    bgX -= 2
    bgX2 -= 2
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == USEREVENT + 1:
            speed += 10
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                Player_ChangeY = 2
            if events.key == pygame.K_LEFT:
                Player_ChangeY = -2
            if events.key == pygame.K_UP:
                Player_ChangeX = -2
            if events.key == pygame.K_DOWN:
                Player_ChangeX = 2
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
                Player_ChangeY = 0.0
            if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                Player_ChangeX = 0.0

    PlayerY += Player_ChangeX
    PlayerX += Player_ChangeY
    pygame.display.update()
    clock.tick(speed)

