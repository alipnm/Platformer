import pygame
class Button:
    def __init__(self, image : pygame.image, centerx : int, centery : int, button_size : tuple):
        self.image = image
        self.image = pygame.transform.scale(self.image, button_size)
        self.rect = self.image.get_rect(center=(centerx, centery))
    def draw(self, screen : pygame.Surface):
        screen.blit(self.image, self.rect)
    def check_click(self):
        result = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                result = True
        return result