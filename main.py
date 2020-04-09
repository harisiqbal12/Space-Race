import pygame
from pygame.locals import *
import random
import math

# initializing Pygame
pygame.init()

# Configuring The Display
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space-Race V-1.0")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('Background(1)_art1.jpg').convert()
bgX = 0
bgX2 = bg.get_width()
bg2_x2 = 0
bg2_x22 = bg.get_width()
clock = pygame.time.Clock()

# Player
PlayerIMG = pygame.image.load('spaceship (1).png')
PlayerX = 20
PlayerY = 250
Player_ChangeX = 0
Player_ChangeY = 0

# Bullet 1
BulletIMG = pygame.image.load('bullet-1.png')
BulletX = 0
BulletY = 250
Bullet_ChangeX = 10
Bullet_ChangeY = 0
Bullet_State = "ready"
# Bullet 2
BulletIMG2 = pygame.image.load('bullet-2.png')
BulletX2 = 0
BulletY2 = 300
Bullet_ChangeX2 = 10
Bullet_ChangeY2 = 50
Bullet_State2 = "ready"
# Laser
LaserIMG = pygame.image.load('laser.png')
LaserX = 0
LaserY = 400
Laser_ChangeX = 0
Laser_ChangeY = 0
Laser_State = "ready"

# Planet
PlanetIMG = pygame.image.load('Planet1.png')
PlanetX = 900
PlanetY = random.randint(-400, 100)
Planet_ChangeX = 1
Planet_ChangeY = 1

# Planet2
Planet2IMG = pygame.image.load('Planet2.png')
Planet2X = 1200
Planet2Y = random.randint(-150, 350)
Planet2_ChangeX = 1
Planet2_changeY = 1

# Planet3
Planet3IMG = pygame.image.load('Planet3.png')
Planet3X = 1050
Planet3Y = random.randint(-300, 320)
Planet3_ChangeX = 1
Planet3_ChangeY = 1

# Planet 4
Planet4IMG = pygame.image.load('Planet4.png')
Planet4X = 1700
Planet4Y = random.randint(-50, 200)
Planet4_ChangeX = 1
Planet4_ChangeY = 1

# Planet 5
Planet5IMG = pygame.image.load('Planet 5.png')
Planet5X = 1100
Planet5Y = random.randint(-400, 200)
Planet5_ChangeX = 1
Planet5_ChangeY = 1

# Black Hole
Black_HoleIMG = pygame.image.load('Black Hole.png')
Black_HoleX = 2000
Black_HoleY = random.randint(-400, 100)
Black_HoleChangeX = 1
Black_HoleChangeY = 1


# FX
def Player(x, y):
    win.blit(PlayerIMG, (x, y))


def Planet_1(x, y):
    win.blit(PlanetIMG, (x, y))


def Planet_2(x, y):
    win.blit(Planet2IMG, (x, y))


def Planet_3(x, y):
    win.blit(Planet3IMG, (x, y))


def Planet_4(x, y):
    win.blit(Planet4IMG, (x, y))


def Planet_5(x, y):
    win.blit(Planet5IMG, (x, y))


def BlackHole(x, y):
    win.blit(Black_HoleIMG, (x, y))


def Bullet(x, y):
    global Bullet_State
    Bullet_State = "fire"
    win.blit(BulletIMG, (x + 55, y + 0))


def Bullet2(x, y):
    global Bullet_State2
    Bullet_State2 = "fire"
    win.blit(BulletIMG2, (x + 55, y + 33))


def Laser(x, y):
    global Laser_State
    Laser_State = "fire"
    win.blit(LaserIMG, (x - 370, y - 330))

def collision(enemyX,enemyY,bulletX,bulletY):
    d = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletX,2)))
    if d:
        print(d)

pygame.time.set_timer(USEREVENT + 1, 500)
speed = 40  # Screen Speed
running = True

# Game-Loop
while running:
    # Background Scrolling Configuring
    rel_x = bgX % bg.get_rect().width
    win.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < W:
        win.blit(bg, (rel_x, 0))
    bgX -= 1
    # Player Drawing On The Screen
    Player(PlayerX, PlayerY)
    # KeyPressing Events
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == USEREVENT + 1:
            speed += 5
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                Player_ChangeY = 2
            if events.key == pygame.K_LEFT:
                Player_ChangeY = -2
            if events.key == pygame.K_UP:
                Player_ChangeX = -2
            if events.key == pygame.K_DOWN:
                Player_ChangeX = 2
            if events.key == pygame.K_SPACE:
                if Bullet_State is "ready":
                    BulletX = PlayerX
                    BulletY = PlayerY
                    Bullet(BulletX, BulletY)
                if Bullet_State2 is "ready":
                    BulletX2 = PlayerX
                    BulletY2 = PlayerY
                    Bullet2(BulletX2, BulletY2)
            if events.key == pygame.K_a:
                if Laser_State is "ready":
                    LaserX = PlayerX
                    LaserY = PlayerY
                    Laser(LaserX, LaserY)
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
                Player_ChangeY = 0.0
            if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                Player_ChangeX = 0.0

    if BulletX >= 1280:
        BulletY = 250
        Bullet_State = "ready"
    if BulletX2 >= 1280:
        BulletY2 = 300
        Bullet_State2 = "ready"
    if LaserX >= 0:
        LaserY = PlayerX
        Laser_State = "ready"
    if Bullet_State is "fire":
        Bullet(BulletX, BulletY)
        BulletX += Bullet_ChangeX
    if Bullet_State2 is "fire":
        Bullet2(BulletX2, BulletY2)
        BulletX2 += Bullet_ChangeX2
    if Laser_State is "fire":
        Laser(LaserX, LaserY)

    PlayerY += Player_ChangeX
    PlayerX += Player_ChangeY
    if PlayerX <= 20:
        PlayerX = 20
    elif PlayerX >= 1218:
        PlayerX = 1218
    if PlayerY <= 0:
        PlayerY = 0
    elif PlayerY >= 665:
        PlayerY = 665

    PlanetX -= Planet_ChangeX
    if PlanetX <= -800:
        PlanetX = 980
        PlanetY = random.randint(-400, 100)

    Planet2X -= Planet2_ChangeX
    if Planet2X <= -610:
        Planet2X = 1350
        Planet2Y = random.randint(-150, 350)

    Planet3X -= Planet3_ChangeX
    if Planet3X <= -400:
        Planet3X = 1100
        Planet3Y = random.randint(-300, 320)
    Planet4X -= Planet4_ChangeX
    if Planet4X <= -400:
        Planet4X = 2000
        Planet4Y = random.randint(-50, 200)
    Planet5X -= Planet5_ChangeX
    if Planet5X <= -450:
        Planet5X = 1200
        Planet5Y = random.randint(-50, 200)
    Black_HoleX -= Black_HoleChangeX
    if Black_HoleX <= -500:
        Black_HoleX = 2000
        Black_HoleY = random.randint(-50, 200)

    Planet_1(PlanetX, PlanetY)
    Planet_2(Planet2X, Planet2Y)
    Planet_3(Planet3X, Planet3Y)
    Planet_4(Planet4X, Planet4Y)
    Planet_5(Planet5X, Planet5Y)
    collision(PlanetX,PlanetY,BulletX,BulletY)
    BlackHole(Black_HoleX, Black_HoleY)
    clock.tick(speed)
    pygame.display.update()
