import pygame
from pygame.sprite import Sprite
class Lava(Sprite):
    def __init__(self, topleft : tuple, group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load("assets/lava.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=topleft)
        group.add(self)