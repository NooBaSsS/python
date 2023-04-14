import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('a')

player_1_width = 20
player_1_height = 70
player_1_x = 50
player_1_y = screen_height // 2 - player_1_height // 2
player_1 = pygame.Rect(
    (player_1_x, player_1_y, player_1_width, player_1_height)
)
player_2_width = 20
player_2_height = 70
player_2_x = screen_width - player_1_x - player_2_width
player_2_y = screen_height // 2 - player_1_height // 2
player_2 = pygame.Rect(
    (player_2_x, player_2_y, player_2_width, player_2_height)
)
ball_color = (WHITE)
ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
ball = pygame.Rect((ball_x, ball_y, ball_width, ball_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_1.y < 0:
            player_1.y = 0
        player_1.y -= 1
    if keys[pygame.K_s]:
        if player_1.y > screen_height - player_1_height:
            player_1.y = screen_height - player_1_height
        player_1.y += 1
    if keys[pygame.K_UP]:
        if player_2.y < 0:
            player_2.y = 0
        player_2.y -= 1
    if keys[pygame.K_DOWN]:
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height
        player_2.y += 1

    ball.x += 1
    ball.y += 1

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_1)
    pygame.draw.rect(screen, WHITE, player_2)
    pygame.draw.rect(screen, WHITE, ball)
    pygame.display.flip()
