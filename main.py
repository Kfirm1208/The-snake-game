import pygame
import sys
from text import draw_text
from pygame.math import Vector2
from button import Button
from gamemain import Game_main


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

#window setting
cell_size = 40
cell_number = 20
screen_size = cell_size * cell_number
win = pygame.display.set_mode((screen_size,screen_size))
icon = pygame.image.load('Graphic/icon.png').convert_alpha()
img_main = pygame.image.load('Graphic/background_snake_game.jpg')
bg_main = pygame.transform.scale(img_main,(screen_size,screen_size))
pygame.display.set_caption('The Snake')
pygame.display.set_icon(icon)

#button setting
Play_button = Button('Play',210,50,(305,270),3)
Score_button = Button('Score',210,50,(305,390),3)
Exit_button = Button('Exit',210,50,(305,515),3)
Back_button = Button('Back',210,50,(310,600),3)

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
        

# main menu 
def main_menu():
    run = True
    action = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()     
        win.blit(bg_main,(0,0))
        
        # button Click
        if Play_button.draw(win):
            action = True
            if action ==True:
                game()
                action != action 
        if Score_button.draw(win):
            action = True
            if action == True  :
                score_page()
                action != action 
        if Exit_button.draw(win):
            action = True
            if action ==True:
                run = False
                action != action 
                sys.exit()
                
        draw_text('The Snake',T_font,text_col,win,235,100)
        draw_text('Pornthep Thammawong no.65010682',N_font,text_col,win,20,10)
        clock.tick(fps)
        pygame.display.update()  
        
#open score              
def open_score():
    with open('score.txt','r') as file:
        file.readlines()
        
#score page
def score_page():
    run =True
    action = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            win.blit(bg_main,(0,0))    
            if Back_button.draw(win):
                action =True
                if action ==True:
                    main_menu() 
                    action != action   
        draw_text('Score',T_font,text_col,win,330,100)
        draw_text(open_score(),N_font,text_col,win,340,100)       
        clock.tick(fps)     
        pygame.display.update()

#game   
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


#main function
if __name__ == '__main__':           
    main_menu()