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


'''
과제 해야 한다
지금은 하기가 싫다
내일도 과제가 있다
내일도 하기가 싫을 것 같다
5/30 아이디어톤
8/18-19 헤커톤
어떻게 보면 이렇게 쾌적한 삶을 살 수 있다는 것에 감사하다
백엔드

혼자 집에서 쉬고 싶은 날, 챙겨야 할 사람 천지, 내가 제일 제일 소중하고 중요하다
돈을 최대한 아끼자, 잠 음식 정복, 상남자
아무 것도 안한다면
남는 게 없다면
오히려 좋다, 즐거운 이야기, 아깝다 시간이

진짜 악한 사람
다행인 것 같다
피곤함이 있다, 비가 올 것 같음
해야할 일이 있다

잠 조금 자고 밥먹고 출발하자, 정리를 하자

'''
