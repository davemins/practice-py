import pygame
import random

# 게임 화면 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# 공 이미지 크기
BALL_WIDTH = 50
BALL_HEIGHT = 50

# 공 초기 위치
BALL_START_X = SCREEN_WIDTH // 2 - BALL_WIDTH // 2
BALL_START_Y = SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2

# 공 이동 속도
BALL_SPEED_X = 1
BALL_SPEED_Y = 1

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# 이미지와 사운드 로드
ball_img = pygame.image.load("ball.png")
hit_sound = pygame.mixer.Sound("hit.wav")

# 공 객체 생성
ball_rect = pygame.Rect(BALL_START_X, BALL_START_Y, BALL_WIDTH, BALL_HEIGHT)

# 무한 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 배경색으로 화면 채우기
    screen.fill(WHITE)

    # 공 이동 처리
    ball_rect.move_ip(BALL_SPEED_X, BALL_SPEED_Y)

    # 벽 충돌 검사
    if ball_rect.left < 0 or ball_rect.right > SCREEN_WIDTH:
        BALL_SPEED_X *= -1
    if ball_rect.top < 0 or ball_rect.bottom > SCREEN_HEIGHT:
        BALL_SPEED_Y *= -1

    # 화면에 공 출력
    screen.blit(ball_img, ball_rect)

    # 공과 마우스 충돌 검사
    mouse_pos = pygame.mouse.get_pos()
    if ball_rect.collidepoint(mouse_pos):
        BALL_SPEED_X *= -1
        BALL_SPEED_Y *= -1
        hit_sound.play()

    # 화면 업데이트
    pygame.display.update()