# 0 = Nothing
# 1 = Dirt
# 2 = Grass
# 3 = Lava
# 4 = Enemy
# 5 = Coin
# 6 = Hidden grass
# 7 = Hidden coin
# Every tiles side
from lava import Lava, pygame
from enemy import Enemy
from coin import Coin
from hidden_classes.hidden_grass import HiddenGrass
from hidden_classes.hidden_coin import HiddenCoin
from hidden_classes.hidden_blob import HiddenBlob
from door import Door
class World:
    def __init__(self, world_data : list, blob_group : pygame.sprite.Group, lava_group : pygame.sprite.Group, coin_group : pygame.sprite.Group, hidden_grass_group : pygame.sprite.Group, hidden_coin_group : pygame.sprite.Group, door_group : pygame.sprite.Group, hidden_blob_group : pygame.sprite.Group):
        self.dirt_picture = pygame.image.load("assets/dirt.png")
        self.grass_picture = pygame.image.load("assets/grass.png")
        self.lava_picture = pygame.image.load("assets/lava.png")
        self.tiles = []
        self.backgroundimage = pygame.image.load('assets/sky.png')
        self.backgroundimage = pygame.transform.scale(self.backgroundimage, (1000, 700))
        for row in range(len(world_data)):
            for column in range(len(world_data[row])):
                if world_data[row][column] == 1:
                    image = pygame.transform.scale(self.dirt_picture, (50, 50))
                    image_rect = image.get_rect(topleft=(column * 50, row * 50))
                    self.tiles.append((image, image_rect))
                if world_data[row][column] == 2:
                    image = pygame.transform.scale(self.grass_picture, (50, 50))
                    image_rect = image.get_rect(topleft=(column * 50, row * 50))
                    self.tiles.append((image, image_rect))
                if world_data[row][column] == 3:
                    Lava((column * 50, row * 50), lava_group)
                if world_data[row][column] == 4:
                    Enemy((column * 50, row * 50 + 15), blob_group)
                if world_data[row][column] == 5:
                    Coin((column * 50, row * 50), coin_group)
                if world_data[row][column] == 6:
                    HiddenGrass((column * 50, row * 50), "grass", hidden_grass_group)
                if world_data[row][column] == 7:
                    HiddenCoin((column * 50, row * 50), hidden_coin_group)
                if world_data[row][column] == 8:
                    Door((column * 50, row * 50), door_group)
                if world_data[row][column] == 9:
                    HiddenBlob((column * 50, row * 50 + 15), hidden_blob_group)
                if world_data[row][column] == 10:
                    HiddenGrass((column * 50, row * 50), "dirt", hidden_grass_group)
    def draw(self, screen : pygame.Surface):
        screen.blit(self.backgroundimage, (0,0))
        for tile in self.tiles:
            screen.blit(tile[0], tile[1])