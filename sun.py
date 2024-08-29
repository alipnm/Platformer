import pygame
class Sun:
    def __init__(self, Topleft : tuple):
        self.image = pygame.image.load('assets/sun.png')
        self.rect = self.image.get_rect(topleft=Topleft)
    def draw(self, screen : pygame.Surface):
        screen.blit(self.image, self.rect)