# statistics.py
import pygame
from config import WINDOW_WIDTH, BOARD_HEIGHT

def display_score(screen, score, moves):
    font = pygame.font.SysFont('monoface', 18)
    score_text = font.render(f'Score = {score}', True, (0, 0, 0))
    moves_text = font.render(f'Moves = {moves}', True, (0, 0, 0))
    
    screen.blit(score_text, (WINDOW_WIDTH // 4, BOARD_HEIGHT + 5))
    screen.blit(moves_text, (3 * WINDOW_WIDTH // 4, BOARD_HEIGHT + 5))
