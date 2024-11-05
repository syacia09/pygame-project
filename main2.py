# main.py
import pygame
import random
from pygame.locals import *
from conf import *
from sprites import Candy
from statistics import display_score

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Candy Crush')

# Load side panel images
left_image = pygame.image.load("jin_left.png")
right_image = pygame.image.load("jin_right.png")

# Rescale images to fit side panel width
left_image = pygame.transform.smoothscale(left_image, (SIDE_PANEL_WIDTH, BOARD_HEIGHT))
right_image = pygame.transform.smoothscale(right_image, (SIDE_PANEL_WIDTH, BOARD_HEIGHT))

# Create the candy board
board = [[Candy(row, col) for col in range(BOARD_WIDTH // CANDY_WIDTH)] for row in range(BOARD_HEIGHT // CANDY_HEIGHT)]
score = 0
moves = 0

def draw():
    screen.fill((173, 216, 230))
    
    # Draw side panel images
    screen.blit(left_image, (0, 0))
    screen.blit(right_image, (BOARD_WIDTH + SIDE_PANEL_WIDTH, 0))

    for row in board:
        for candy in row:
            candy.draw(screen)

    display_score(screen, score, moves)
    pygame.display.update()

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    draw()
    clock.tick(30)

pygame.quit()
