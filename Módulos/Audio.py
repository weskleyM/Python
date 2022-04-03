import pygame

pygame.init()
pygame.mixer.music.load('alarm.mp3')
pygame.mixer.music.play()
pygame.event.wait()
