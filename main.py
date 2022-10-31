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
img_main = pygame.image.load('Graphic/background_snake_game.jpg')
bg_main = pygame.transform.scale(img_main,(screen_size,screen_size))
pygame.display.set_caption('The Snake')
pygame.display.set_icon(icon)

#button setting
Play_button = Button('Play',210,50,(310,250),3)
Score_button = Button('Score',210,50,(310,380),3)
Exit_button = Button('Exit',210,50,(310,520),3)

#define font
N_font =  pygame.font.Font('Font/PoetsenOne-Regular.ttf',20)
T_font =  pygame.font.Font('Font/PoetsenOne-Regular.ttf',70)
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf',25)

#define color
text_col = (255,255,255)

#system setting
clock = pygame.time.Clock()
fps = 144                    

#game attribute
apple = pygame.image.load('Graphic/apple (1).png').convert_alpha()
main_game = Game_main(cell_number)
        
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 110)
        
#Draw text        
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    win.blit(img,(x,y))        
 
def main_menu():
    run = True
    game_play = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
        win.blit(bg_main,(0,0))
        if Play_button.draw(win):
            game_play = True
        if game_play ==True:
            game()
            game_play = False
        if Score_button.draw(win):
            print('Score')
        if Exit_button.draw(win):
            run = False
            sys.exit()
        draw_text('The Snake',T_font,text_col,240,100)
        draw_text('no.65010682',N_font,text_col,20,10)
        clock.tick(fps)
        pygame.display.update()        

def game():  
    run = True
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
                    main_menu()

        win.fill((175, 215, 70))
        main_game.draw_elements(cell_number,cell_size,win,apple,game_font)
        clock.tick(fps)
        pygame.display.update()  
            
main_menu()

    

