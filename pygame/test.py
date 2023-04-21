import pygame
import sys
from degrees_to_velocity import degrees_to_velocity
from random import randint

pygame.init()

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

score_left = pygame.font.Font(None, 60)
score_right = pygame.font.Font(None, 60)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('a')

player_1_width = 20
player_1_height = 70
player_1_x = 50
player_1_y = screen_height // 2 - player_1_height // 2
score_p_1 = 0
player_1_speed = 10
player_1 = pygame.Rect(
    (player_1_x, player_1_y, player_1_width, player_1_height)
)

player_2_width = 20
player_2_height = 70
player_2_x = screen_width - player_1_x - player_2_width
player_2_y = screen_height // 2 - player_1_height // 2
score_p_2 = 0
player_2_speed = 10
player_2 = pygame.Rect(
    (player_2_x, player_2_y, player_2_width, player_2_height)
)

ball_color = (WHITE)
ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
velocity = degrees_to_velocity(45, 10)
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]
ball = pygame.Rect((ball_x, ball_y, ball_width, ball_height))


def ball_to_center():
    ball.x = ball_x
    ball.y = ball_y
    if randint(0, 1) == 0:
        velocity = degrees_to_velocity(randint(45, 135), 10)
    else:
        velocity = degrees_to_velocity(randint(215, 305), 10)


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
        player_1.y -= player_1_speed
    if keys[pygame.K_s]:
        if player_1.y > screen_height - player_1_height:
            player_1.y = screen_height - player_1_height
        player_1.y += player_1_speed
    if keys[pygame.K_UP]:
        if player_2.y < 0:
            player_2.y = 0
        player_2.y -= player_2_speed
    if keys[pygame.K_DOWN]:
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height
        player_2.y += player_2_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.x < 0:
        score_p_2 += 1
        print(score_p_1)
        print(score_p_2)
        ball_to_center()
    if ball.x > screen_width - ball_width:
        score_p_1 += 1
        print(score_p_1)
        print(score_p_2)
        ball_to_center()
    if ball.y < 0:
        ball_speed_y *= -1
    if ball.y > screen_height - ball_height:
        ball_speed_y *= -1
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_1)
    pygame.draw.rect(screen, WHITE, player_2)
    pygame.draw.rect(screen, WHITE, ball)
    score_left_img = score_left.render(str(score_p_1), True, WHITE)
    score_right_img = score_left.render(str(score_p_2), True, WHITE)
    screen.blit(score_left_img, (screen_width * 0.25, 10))
    screen.blit(score_right_img, (screen_width * 0.75, 10))
    pygame.draw.line(
        screen,
        WHITE,
        [screen_width // 2, 0],
        [screen_width // 2, screen_height],
        1
    )
    pygame.display.flip()

    clock.tick(FPS)
