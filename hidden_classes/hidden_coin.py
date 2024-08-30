import pygame
from pygame.sprite import Sprite
class HiddenCoin(Sprite):
    def __init__(self, topleft : tuple, hidden_coin_group : pygame.sprite.Group):
        super().__init__()
        self.image = pygame.image.load("assets/coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=topleft)
        self.counter = 1
        self.direction = 1
        self.counter_delay = pygame.time.get_ticks()
        hidden_coin_group.add(self)
    def animation(self):
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