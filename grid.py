import random

import pygame
from vec2 import Vec2

class Grid:
    def __init__(self):
        self.pos_frac = Vec2(0.1, 0.1)
        self.size = Vec2(16, 16)
        # self.map = []
        # for _ in range(self.size.y):
        #     row = []
        #     for _ in range(self.size.x):
        #         row.append(random.choice((True, False)))
        #     self.map.append(row)
        self.map = [
            [True, True, True, True, True, True, True, True],
            [True, False, False, False, False, False, False, True],
            [True, False, True, True, False, True, False, True],
            [False, False, True, True, False, False, False, False],
            [True, False, False, False, True, True, False, True],
            [True, False, True, False, True, True, False, True],
            [True, False, False, False, False, False, False, True],
            [True, True, True, True, True, True, True, True],
        ]
        self.size = Vec2(len(self.map), len(self.map[0]))

    def draw(self, graphics):
        tl = graphics.screen_dims * self.pos_frac
        br = graphics.screen_dims * (Vec2(1.0, 1.0) - self.pos_frac)
        width, height = br.x - tl.x, br.y - tl.y
        rect = (tl.x, tl.y, width, height)
        pygame.draw.rect(graphics.screen, (255, 0, 0), rect, 2)

        #   draw a box at every cell that is true
        start = tl.clone()
        cursor = tl.clone()
        box_size = Vec2(width, height) / self.size
        box_size = box_size.as_ints()
        for iy in range(self.size.y):
            for ix in range(self.size.x):
                rect = (cursor.x, cursor.y, box_size.x, box_size.y)
                if self.map[iy][ix]:
                    pygame.draw.rect(graphics.screen, (0, 0, 255), rect)
                cursor.x += box_size.x
            cursor.x = start.x
            cursor.y += box_size.y

        #   draw a box around the whole grid