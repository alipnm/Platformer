from world import World, pygame
from levels.level_one import level_one_data, HIGHST_SCORE_UGAN_LEVELONE
from levels.level_two import level_two_data, HIGHST_SCORE_UGAN_LEVELTWO
from levels.level_three import level_three_data, HIGHST_SCORE_UGAN_LEVELTHREE
from levels.level_four import level_four_data, HIGHST_SCORE_UGAN_LEVELFOR
from levels.level_five import level_five_data, HIGHST_SCORE_UGAN_LEVELFIVE
from levels.level_six import level_six_data, HIGHST_SCORE_UGAN_LEVELSX
from levels.level_seven import level_seven_data, HIGHST_SCORE_UGAN_LEVELSEVN
from player import Player
from button import Button
from sun import Sun
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
lava_group = pygame.sprite.Group()
blob_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
hidden_grass_group = pygame.sprite.Group()
hidden_coin_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
hidden_blob_group = pygame.sprite.Group()
world = World(level_one_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
sun = Sun((50, 60))
score = 0
level = 1
lives = 3
game_font = pygame.font.Font("assets/Game Font.otf", 20)
start_button_image = pygame.image.load("assets/start_btn.png")
start_button = Button(start_button_image, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (100, 50))
pygame.mixer.music.load("assets/music.wav")
pygame.mixer.music.play(-1)
for blob in blob_group:
    blob.permission_to_move = False
for coin in coin_group:
    coin.permission_to_move = False
running = True
while running:
    running = not start_button.check_click()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                running = False
    world.draw(screen)
    lava_group.draw(screen)
    blob_group.update()
    blob_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    door_group.draw(screen)
    sun.draw(screen)
    start_button.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
for blob in blob_group:
    blob.permission_to_move = True
for coin in coin_group:
    coin.permission_to_move = True
player = Player()
restart_button_image = pygame.image.load("assets/restart_btn.png")
exit_button_image = pygame.image.load("assets/exit_btn.png")
score_text = game_font.render(f"Score:{score}", True, (250,12,0))
score_rect = score_text.get_rect(right=SCREEN_WIDTH - 10, centery=20)
lives_text = game_font.render(f"Live:{lives}", True, (250,12,0))
lives_rect = lives_text.get_rect(left=10, centery=20)
restart_button = Button(restart_button_image, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (110, 50))
exit_button = Button(exit_button_image, SCREEN_WIDTH / 2, 25, (100, 50))
game_over_sound = pygame.mixer.Sound("assets/game_over.wav")
game_over_played = False
def game_over():
    global score, game_over_played, level
    hidden_grass_group.empty()
    hidden_coin_group.empty()
    hidden_blob_group.empty()
    restart_button.draw(screen)
    if not game_over_played:
        game_over_sound.play()
        game_over_played = True
    score = 0
    level = 1
    for blob in blob_group:
        blob.permission_to_move = False
    for coin in coin_group:
        coin.permission_to_move = False
    for door in door_group:
        door.permission_to_move = False
    if restart_button.check_click():
        player.reset()
        blob_group.empty()
        coin_group.empty()
        door_group.empty()
        lava_group.empty()
        world.__init__(level_one_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
        for blob in blob_group:
            blob.permission_to_move = True
        for coin in coin_group:
            coin.permission_to_move = True
        for door in door_group:
            door.permission_to_move = True
        game_over_played = False
def win():
    global score, level, lives
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((255,255,255))
        screen.blit(pygame.image.load("assets/sky.png"), (0,0))
        final_point_text = game_font.render(f"Final point:{score + lives}/127", True, (255,255,255))
        final_point_rect = final_point_text.get_rect(centerx=SCREEN_WIDTH / 2, top=0)
        score_text = game_font.render(f"Score:{score}/124", True, (250,12,0))
        score_rect = score_text.get_rect(right=SCREEN_WIDTH - 10, centery=20)
        win_text = game_font.render("You win this game!", True, (85,204,0))
        win_rect = win_text.get_rect(centerx=SCREEN_WIDTH / 2, top=final_point_rect.bottom + 20)
        lives_text = game_font.render(f"Live:{lives}/3", True, (250,12,0))
        screen.blit(win_text, win_rect)
        screen.blit(final_point_text, final_point_rect)
        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)
        restart_button.draw(screen)
        if restart_button.check_click():
            world.__init__(level_one_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            score = 0
            level = 1
            lives = 3
            player.reset()
            break
        pygame.display.update()
        clock.tick(FPS)
running = True
while running:
    running = not exit_button.check_click()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if player.next_level:
        level += 1
        player.next_level = False
        hidden_grass_group.empty()
        hidden_coin_group.empty()
        hidden_blob_group.empty()
        blob_group.empty()
        coin_group.empty()
        door_group.empty()
        lava_group.empty()
        if level == 2:
            world.__init__(level_two_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            player.reset()
        elif level == 3:
            world.__init__(level_three_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            player.reset()
        elif level == 4:
            world.__init__(level_four_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            player.reset()
        elif level == 5:
            world.__init__(level_five_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            player.reset()
        elif level == 6:
            world.__init__(level_six_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            player.reset()
        elif level == 7:
            world.__init__(level_seven_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            player.reset()
        else:
            win()
    world.draw(screen)
    lava_group.draw(screen)
    player.draw(screen)
    if player.is_alive:
        score, lives = player.move(score, lives, world.tiles, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
        if player.should_reset:
            player.should_reset = False
            player.reset()
            hidden_grass_group.empty()
            hidden_coin_group.empty()
            hidden_blob_group.empty()
            blob_group.empty()
            coin_group.empty()
            door_group.empty()
            lava_group.empty()
            if level == 1:
                if score >= HIGHST_SCORE_UGAN_LEVELONE:
                    score -= HIGHST_SCORE_UGAN_LEVELONE
                else:
                    score = 0
            elif level == 2:
                if score >= HIGHST_SCORE_UGAN_LEVELTWO:
                    score -= HIGHST_SCORE_UGAN_LEVELTWO
                else:
                    score = 0
            elif level == 3:
                if score >= HIGHST_SCORE_UGAN_LEVELTHREE:
                    score -= HIGHST_SCORE_UGAN_LEVELTHREE
                else:
                    score = 0
            elif level == 4:
                if score >= HIGHST_SCORE_UGAN_LEVELFOR:
                    score -= HIGHST_SCORE_UGAN_LEVELFOR
                else:
                    score = 0
            elif level == 5:
                if score >= HIGHST_SCORE_UGAN_LEVELFIVE:
                    score -= HIGHST_SCORE_UGAN_LEVELFIVE
                else:
                    score = 0
            elif level == 6:
                if score >= HIGHST_SCORE_UGAN_LEVELSX:
                    score -= HIGHST_SCORE_UGAN_LEVELSX
                else:
                    score = 0
            elif level == 7:
                if score >= HIGHST_SCORE_UGAN_LEVELSEVN:
                    score -= HIGHST_SCORE_UGAN_LEVELSEVN
                else:
                    score = 0
            if level == 1:
                world.__init__(level_one_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            elif level == 2:
                world.__init__(level_two_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            elif level == 3:
                world.__init__(level_three_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            elif level == 4:
                world.__init__(level_four_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            elif level == 5:
                world.__init__(level_five_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            elif level == 6:
                world.__init__(level_six_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
            elif level == 7:
                world.__init__(level_seven_data, blob_group, lava_group, coin_group, hidden_grass_group, hidden_coin_group, door_group, hidden_blob_group)
        if player.should_game_over:
            player.should_game_over = False
            lives = 3
            game_over()
    else:
        game_over()
    score_text = game_font.render(f"Score:{score}", True, (250,12,0))
    score_rect.right = SCREEN_WIDTH - 30
    score_rect.centery = 20
    lives_text = game_font.render(f"Live:{lives}", True, (250,12,0))
    blob_group.update()
    blob_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    if player.draw_hidden_grass:
        hidden_grass_group.draw(screen)
    if player.draw_hidden_coin:
        hidden_coin_group.update()
        hidden_coin_group.draw(screen)
    if player.draw_hidden_blob:
        hidden_blob_group.update()
        hidden_blob_group.draw(screen)
    door_group.update()
    door_group.draw(screen)
    exit_button.draw(screen)
    sun.draw(screen)
    screen.blit(score_text, score_rect)
    screen.blit(lives_text, lives_rect)
    pygame.display.update()
    clock.tick(FPS)