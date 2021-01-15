import pygame

pygame.init()

sc_w = 960 #화면 가로 크기
sc_h = 540 #화면 세로 크기
sc = pygame.display.set_mode((sc_w, sc_h))

pygame.display.set_caption("untitled") #게임 제목 

bg = pygame.image.load("D:/바탕화면/game/background.png") #배경 불러오기

char = pygame.image.load("D:/바탕화면/game/char.png")#캐릭터 불러오기

char_size = char.get_rect().size  #캐릭터의 크기를 구함 
bg_size = bg.get_rect().size    #배경의 크기를 구함

char_width = char_size[0]  #캐릭터 x축 크기를 구함 
char_height = char_size[1]  #캐릭터 y축 크기를 구함

bg_width = bg_size[0]   #배경의 x축 크기를 구함
bg_height = bg_size[1]  #배경의 y축 크기를 구함

char_x_pos = sc_w / 2 - char_width/2 #캐릭터 위치 x축으로는 중앙
char_y_pos = sc_h - char_height   #캐릭터 위치 Y축으로는 맨 아래

bg_char = -bg_width /2 + sc_w /2 #배경의 시작 생성위치
char_bg_x_pos = 0

char_speed = 1 #캐릭터의 속도
a = 0
 
run = True #게임이 진행중인지 확인하는 변수
while run:

    sc.blit(bg, (bg_char,0)) #배경 적용

    bg_char += char_bg_x_pos #캐릭터 x축 움직임 구현

    sc.blit(char, (char_x_pos, char_y_pos)) #캐릭터 적용

    pygame.display.update() #화면 유지

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: #캐릭터 좌우 움직임
                char_bg_x_pos -= char_speed
            elif event.key == pygame.K_a: #캐릭터 좌우 움직임
                char_bg_x_pos += char_speed
            elif event.key == pygame.K_SPACE: #점프 (미구현)
                pass

            elif event.key == pygame.K_ESCAPE:#esc키를 눌렀을 때 프로그램이 종료되도록 하는 코드
                run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: #키가 눌리지 않을 때는 좌우로 움직이지 않게하는 코드
                char_bg_x_pos += char_speed
            elif event.key == pygame.K_a:
                char_bg_x_pos -= char_speed
                
        if bg_char > 0:   #캐릭터가 일정거리 이상 이동하지 못하도록 하는 문장
            char_bg_x_pos = 0
            bg_char = 0
        if bg_char < -5000: #캐릭터가 일정거리 이상 이동하지 못하도록 하는 문장
            char_bg_x_pos = 0
            bg_char = -5000
        


        if event.type == pygame.QUIT: #창 닫기를 했을 때 프로그램이 종료되도록 하는 코드
            run = False
    
pygame.quit() #게임 종료