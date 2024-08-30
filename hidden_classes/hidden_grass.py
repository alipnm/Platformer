import pygame
from pygame.sprite import Sprite
class HiddenGrass(Sprite):
    def __init__(self, topleft : tuple, grass_or_dirt : str, group : pygame.sprite.Group):
        super().__init__()
        if grass_or_dirt == "grass":
            self.image = pygame.image.load("assets/grass.png")
        elif grass_or_dirt == "dirt":
            self.image = pygame.image.load("assets/dirt.png")
        else:
            self.image = pygame.image.load("assets/grass.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=topleft)
        group.add(self)