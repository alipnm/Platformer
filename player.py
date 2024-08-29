# Directions:
# left = -1
# right = 1
from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.image_number_list_index = 0
        for i in range(1, 5):
            self.IMG = pygame.image.load(f"assets/guy{i}.png")
            self.right_images.append(self.IMG)
            self.IMG = pygame.transform.flip(self.IMG, True, False)
            self.left_images.append(self.IMG)
        self.image = self.right_images[self.image_number_list_index]
        self.rect = pygame.rect.Rect(100, 250, ((self.IMG.get_width()) * 0.6) + 10, self.IMG.get_height())
        self.mask = pygame.mask.from_surface(self.image)
        self.last_update = pygame.time.get_ticks()
        self.moving_status = False
        self.direction = 1
        self.yvel = 0
        self.jumped = False
        self.is_alive = True
        self.draw_hidden_grass = False
        self.draw_hidden_coin = False
        self.draw_hidden_blob = False
        self.next_level = False
        self.should_reset = False
        self.should_game_over = False
        self.game_start_now = True
        self.not_move_delay = pygame.time.get_ticks()
        self.ghost_image = pygame.image.load("assets/ghost.png")
        self.point_sound = pygame.mixer.Sound("assets/coin.wav")
        self.jump_sound = pygame.mixer.Sound("assets/jump.wav")
    def reset(self):
        self.image_number_list_index = 0
        self.image = self.right_images[self.image_number_list_index]
        self.rect = pygame.rect.Rect(100, 250, (self.IMG.get_width()) * 0.6, self.IMG.get_height())
        self.mask = pygame.mask.from_surface(self.image)
        self.last_update = pygame.time.get_ticks()
        self.moving_status = False
        self.direction = 1
        self.yvel = 0
        self.jumped = False
        self.is_alive = True
        self.draw_hidden_grass = False
        self.draw_hidden_coin = False
        self.draw_hidden_blob = False
        self.next_level = False
        self.should_reset = False
        self.should_game_over = False
        self.game_start_now = True
        self.not_move_delay = pygame.time.get_ticks()
    def move(self, score : int, lives : int, screen_tiles : list, enemy_group : pygame.sprite.Group, lava_group : pygame.sprite.Group, coin_group : pygame.sprite.Group, hidden_grass_group : pygame.sprite.Group, hidden_coin_group : pygame.sprite.Group, door_group : pygame.sprite.Group, hidden_blob_group : pygame.sprite.Group) -> int:
        dx = 0
        dy = 0
        if self.game_start_now and (pygame.time.get_ticks() - self.not_move_delay) > 250:
            self.game_start_now = False
        if not self.game_start_now:
            keys = pygame.key.get_pressed()
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] or not keys[pygame.K_UP]:
                self.moving_status = False
            if keys[pygame.K_LEFT]:
                self.moving_status = True
                self.direction = -1
                dx -= 5
            if keys[pygame.K_RIGHT]:
                self.moving_status = True
                self.direction = 1
                dx += 5
            if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self.jumped:
                self.yvel = -18
                self.jumped = True
                self.jump_sound.play()
        dy += self.yvel
        self.yvel += 1
        for lava in lava_group:
            if pygame.sprite.collide_mask(self, lava):
                lives -= 1
                self.should_reset = True
                if lives <= 0:
                    self.should_reset = False
                    self.is_alive = False
                    self.should_game_over = True
                break
        for tile in screen_tiles:
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                if self.yvel > 0:
                    dy = tile[1].top - self.rect.bottom
                    self.jumped = False
                else:
                    dy = tile[1].bottom - self.rect.top
                self.yvel = 0
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.size[0], self.rect.size[1]):
                dx = 0
        for blob in enemy_group:
            if pygame.sprite.collide_mask(self, blob):
                if self.yvel > 1:
                    blob.kill()
                    self.point_sound.play()
                    score += 1
                else:
                    lives -= 1
                    if lives <= 0:
                        self.is_alive = False
                        self.should_game_over = True
                    else:
                        self.should_reset = True
        for coin in coin_group:
            if pygame.sprite.collide_mask(self, coin):
                coin.kill()
                self.point_sound.play()
                score += 1
        for hidden_grass in hidden_grass_group:
            if hidden_grass.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                self.draw_hidden_grass = True
                self.draw_hidden_coin = True
                self.draw_hidden_blob = True
                if self.yvel > 0:
                    dy = hidden_grass.rect.top - self.rect.bottom
                    self.jumped = False
                else:
                    dy = hidden_grass.rect.bottom - self.rect.top
                self.yvel = 0
            if hidden_grass.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.size[0], self.rect.size[1]):
                dx = 0
        for hidden_coin in hidden_coin_group:
            if self.draw_hidden_coin:
                if pygame.sprite.collide_mask(self, hidden_coin):
                    hidden_coin.kill()
                    self.point_sound.play()
                    score += 1
        for door in door_group:
            if pygame.sprite.collide_mask(self, door):
                self.next_level = True
        for hidden_blob in hidden_blob_group:
            if self.draw_hidden_blob:
                if pygame.sprite.collide_mask(self, hidden_blob):
                    if self.yvel > 1:
                        hidden_blob.kill()
                        self.point_sound.play()
                        score += 1
                    else:
                        lives -= 1
                        if lives <= 0:
                            self.is_alive = False
                            self.should_game_over = True
                        else:
                            self.should_reset = True
        if self.rect.right + dx >= 1000:
            dx = 1000 - self.rect.right
        if self.rect.left + dx <= 0:
            dx = 0 - self.rect.left
        self.rect.x += dx
        self.rect.y += dy
        return score, lives
    def animation(self):
        if pygame.time.get_ticks() - self.last_update > 100:
            self.last_update = pygame.time.get_ticks()
            self.image_number_list_index += 1
            if self.image_number_list_index >= len(self.right_images) or not self.moving_status:
                self.image_number_list_index = 0
        if self.direction == 1:
            self.image = self.right_images[self.image_number_list_index]
        elif self.direction == -1:
            self.image = self.left_images[self.image_number_list_index]
    def draw(self, screen):
        if not self.is_alive:
            self.image = self.ghost_image
        screen.blit(self.image, (self.rect.topleft[0] - 10, self.rect.topleft[1]))
        self.mask = pygame.mask.from_surface(self.image)
        # showing mask:
        # pygame.draw.lines(self.image, (255,0,0), True, self.mask.outline())
        # showing rect
        # pygame.draw.rect(screen, (255,0,0), self.rect, 1)
        self.animation()