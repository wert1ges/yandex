import sys
import requests
import pygame
import os

spn = [0.5, 0.5]
coords = [30.7, 30.8]

server = "http://static-maps.yandex.ru/1.x/"
parametrs = {
    'll': str(coords[0]) + ',' + str(coords[1]),
    'spn': str(spn[0]) + ',' + str(spn[1]),
    'l': 'map'}

response = requests.get(server, params=parametrs)
with open('map.png', 'wb') as f:
    f.write(response.content)
bg = pygame.image.load('map.png')
os.remove('map.png')
pygame.init()
screen = pygame.display.set_mode((600, 500))
run = True
now = 0
while run:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()