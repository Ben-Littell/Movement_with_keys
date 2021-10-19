import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, BLACK]

# Math Constants
PI = math.pi

# Game Constants
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
FPS = 60


##############################################################################
class Box:

    def __init__(self, display, x, y, width, height, x_speed=0, y_speed=0):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_speed = x_speed
        self.y_speed = y_speed

    def draw_box(self):
        pygame.draw.rect(self.display, RED, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.x += -1 * self.x_speed
        if self.y <= 0 or self.y >= HEIGHT - self.height:
            self.y += -1 * self.y_speed


##############################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()

running = True
# CREATE PLAYER
player_width = 50
x_loc = (WIDTH - player_width) / 2
y_loc = HEIGHT - 2 * player_width
player = Box(screen, x_loc, y_loc, player_width, player_width)
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.x_speed = 0
                # player.y_speed = 0
            if event.key == pygame.K_LEFT:
                player.x_speed = 0
                # player.y_speed = 0
            if event.key == pygame.K_UP:
                player.y_speed = 0
                # player.x_speed = 0
            if event.key == pygame.K_DOWN:
                player.y_speed = 0
                # player.x_speed = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.x_speed = 5
                # player.y_speed = 0
            if event.key == pygame.K_LEFT:
                player.x_speed = -5
                # player.y_speed = 0
            if event.key == pygame.K_UP:
                player.y_speed = -5
                # player.x_speed = 0
            if event.key == pygame.K_DOWN:
                player.y_speed = 5
                # player.x_speed = 0
            if event.key == pygame.K_SPACE:
                player.x_speed = 0
                player.y_speed = 0

    screen.fill(WHITE)
    player.draw_box()
    player.update()
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
