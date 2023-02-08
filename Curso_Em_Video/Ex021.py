# Faça um programa em Python que abra e reproduza o audio de um arquivo Mp3.

import pygame
pygame.init()
pygame.mixer.music.load('Nasac - Dona Morte (prod. Psych).mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()