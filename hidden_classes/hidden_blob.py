from typing import Any
import pygame
from pygame.sprite import Sprite
class HiddenBlob(Sprite):
    def __init__(self, topleft : tuple, hidden_blob_group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load("assets/blob.png")
        self.rect = self.image.get_rect(topleft=topleft)
        self.counter = 0
        self.direction = 1
        hidden_blob_group.add(self)
    def animation(self):
        self.counter += 1
        if self.counter >= 50:
            self.direction *= -1
            self.counter *= -1
        self.rect.x += self.direction
    def update(self):
        self.animation()