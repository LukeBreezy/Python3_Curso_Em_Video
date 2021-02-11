import pygame
num = int(input('Digite: '))

musica = ["Juice", "Let's Smoke"]

pygame.mixer.init()
pygame.mixer.music.load(musica[num-1]+".mp3")
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
