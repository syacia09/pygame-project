# sprites.py
import pygame
import random
from config import CANDY_COLORS, CANDY_SIZE, CANDY_WIDTH, CANDY_HEIGHT

class Candy:
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.color = random.choice(CANDY_COLORS)
        image_name = f'{self.color}.png'
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.smoothscale(self.image, CANDY_SIZE)
        self.rect = self.image.get_rect()
        self.rect.left = col_num * CANDY_WIDTH + 100  # Shift right to account for side panel
        self.rect.top = row_num * CANDY_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def snap(self):
        self.rect.top = self.row_num * CANDY_HEIGHT
        self.rect.left = self.col_num * CANDY_WIDTH + 100
