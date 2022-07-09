import pygame

from vec2 import Vec2
from graphics import Graphics
from entity import Entity
from grid import Grid

################   ENGINE STATE  ################
graphics = Graphics()
clock = pygame.time.Clock()

################   GAME STATE  ################
grid = Grid()
entities = []

################   DO GAME  ################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                pygame.quit()
                quit()
            elif event.key == pygame.K_SPACE:
                points = []
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

    ########   update   ########
    pygame.display.set_caption(f'speedrun-pacman - {int(clock.get_fps())}fps')
    dt = clock.tick(60)*.001

    ########   draw   ########
    graphics.window.fill((60,50,60))
    graphics.screen = pygame.Surface(graphics.screen_dims.as_tuple(), pygame.SRCALPHA)

    ####    draw grid
    grid.draw(graphics)
    ####    draw entities
    for entity in entities:
        entity.draw(graphics)
    ####    draw any effects or particles
    ####    draw menu things or score

    graphics.window.blit(pygame.transform.scale(graphics.screen, graphics.window_size.as_tuple()),(0, 0))
    pygame.display.flip()
