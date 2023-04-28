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

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode(
    (screen_width, screen_height),
    pygame.FULLSCREEN
)
pygame.display.set_caption('a')


def players_to_center():
    player_1.y = screen_height // 2 - player_1_height // 2
    player_2.y = screen_height // 2 - player_2_height // 2
    player_1.x = screen_width * 0.1
    player_2.x = screen_width * 0.9 - player_2_width


player_1_width = 20
player_1_height = 70
score_p_1 = 0
player_1_speed = 10
player_1 = pygame.Rect(
    (0, 0, player_1_width, player_1_height)
)

player_2_width = 20
player_2_height = 70
score_p_2 = 0
player_2_speed = 10
player_2 = pygame.Rect(
    (0, 0, player_2_width, player_2_height)
)

players_to_center()


def ball_to_center():
    ball.x = screen_width // 2 - ball_width
    ball.y = screen_height // 2 - ball_height


def rotate_ball() -> tuple:
    if randint(0, 1) == 0:
        direction = randint(225, 315)
    else:
        direction = randint(45, 135)
    velocity = degrees_to_velocity(direction, 10)
    return velocity


ball_color = (WHITE)
ball_width = 10
ball_height = 10
ball = pygame.Rect((0, 0, ball_width, ball_height))
ball_to_center()
velocity = rotate_ball()
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]

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
    '''
    if keys[pygame.K_UP]:
        if player_2.y < 0:
            player_2.y = 0
        player_2.y -= player_2_speed
    if keys[pygame.K_DOWN]:
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height
        player_2.y += player_2_speed
    '''

    if ball.centery < player_2.centery:
        player_2.y -= player_2_speed
    if ball.centery > player_2.centery:
        player_2.y += player_2_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.x < 0:
        score_p_2 += 1
        ball_to_center()
        players_to_center()
        pygame.time.delay(1500)
        velocity = rotate_ball()
        ball_speed_x = velocity[0]
        ball_speed_y = velocity[1]
    if ball.x > screen_width - ball_width:
        score_p_1 += 1
        ball_to_center()
        players_to_center()
        pygame.time.delay(1500)
        velocity = rotate_ball()
        ball_speed_x = velocity[0]
        ball_speed_y = velocity[1]
    if ball.y < 0:
        ball_speed_y *= -1
    if ball.y > screen_height - ball_height:
        ball_speed_y *= -1
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        ball.x += ball_speed_x
        ball.y += ball_speed_y

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
