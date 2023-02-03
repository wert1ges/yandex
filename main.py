import sys
import requests
import pygame
import os

def ch_spn(up):
    global spn
    if up:
        spn = [spn[0] * 2, spn[1] * 2]
    else:
        spn = [spn[0] / 2, spn[1] / 2]

spn = [0.5, 0.5]
coords = [30.7, 30.8]

def sh_map():
    global bg
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
sh_map()
screen = pygame.display.set_mode((600, 450))
run = True
now = 0
while run:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN:
                ch_spn(False)
                sh_map()
            elif event.key == pygame.K_PAGEUP:
                ch_spn(True)
                sh_map()
    pygame.display.flip()
pygame.quit()