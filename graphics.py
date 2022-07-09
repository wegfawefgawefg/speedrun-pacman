import pygame
from vec2 import Vec2

class Graphics:
    def __init__(self):
        self.screen_dims = Vec2(256,256)
        self.scale = 2
        self.window_size = self.screen_dims * self.scale
        self.ratio =  self.screen_dims / self.window_size
        pygame.init()
        self.screen = pygame.Surface(self.screen_dims.as_tuple())
        self.window = pygame.display.set_mode(self.window_size.as_tuple())

    def window_to_screen(self, p):
        return p * self.ratio