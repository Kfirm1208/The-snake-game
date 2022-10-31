import pygame
import sys
from pygame.math import Vector2
from button import Button
from gamemain import Game_main

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

#window setting
cell_size = 40
cell_number = 20
screen_size = cell_size *cell_number
win = pygame.display.set_mode((screen_size,screen_size))
icon = pygame.image.load('Graphic/icon.png').convert_alpha()
pygame.display.set_caption('The Snake')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
apple = pygame.image.load('Graphic/apple (1).png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf',25)
Play_button = Button('Play',210,50,(310,250),3)
Score_button = Button('Score',210,50,(310,380),3)
Exit_button = Button('Exit',210,50,(310,520),3)
fps = 144                    
run =True

main_game = Game_main(cell_number)
        
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 110)
        
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update(cell_number)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_ESCAPE:
                run = False
                sys.exit()

    win.fill((175, 215, 70))
    main_game.draw_elements(cell_number,cell_size,win,apple,game_font)
    clock.tick(fps)
    pygame.display.update()

