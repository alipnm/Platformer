from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, topLeft : tuple, blob_group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load('assets/blob.png')
        self.rect = self.image.get_rect(topleft=topLeft)
        self.direction = 1
        self.counter = 0
        self.permission_to_move = True
        blob_group.add(self)
    def update(self):
        if self.permission_to_move:
            self.counter += 1
            if self.counter >= 50:
                self.direction *= -1
                self.counter *= -1
            self.rect.x += self.direction