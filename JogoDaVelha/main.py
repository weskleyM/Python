import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)

tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Velha')
tela.fill(BG_COLOR)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
