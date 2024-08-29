import pygame
from pygame.sprite import Sprite
class Coin(Sprite):
    def __init__(self, topleft_tuple : tuple, coin_group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load("assets/coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=topleft_tuple)
        self.counter = 1
        self.direction = 1
        self.counter_delay = pygame.time.get_ticks()
        self.permission_to_move = True
        coin_group.add(self)
    def animation(self):
        if self.permission_to_move:
            dx = 0
            if pygame.time.get_ticks() - self.counter_delay > 100:
                self.counter_delay = pygame.time.get_ticks()
                self.counter += 1
                if self.counter >= 10:
                    self.counter *= -1
                    self.direction *= -1
                dx = self.direction
            self.rect.x += dx
    def update(self):
        self.animation()