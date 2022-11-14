import pygame
import sys
from text import draw_text
from pygame.math import Vector2
from button import Button1,Button2
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
Play_button = Button1('Play',210,50,(305,270),3)
Score_button = Button1('Score',210,50,(305,390),3)
Exit_button = Button1('Exit',210,50,(305,515),3)
Enter_button = Button2('Enter',100,20,(530,200),2)
Back_button = Button1('Back',210,50,(310,600),3)

#define font
N_font =  pygame.font.Font('Font/PoetsenOne-Regular.ttf',20)
T_font =  pygame.font.Font('Font/PoetsenOne-Regular.ttf',70)
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf',25)
P_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf',15)

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
    #define player input
    player_text = ''
    #create rectangle
    input_rect = pygame.Rect(402,200,100,20)

    action = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()  
            # input the text  
            
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_BACKSPACE and event.key != pygame.K_ESCAPE:
                    player_text = player_text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    run =False
                    sys.exit()         
                else: 
                    player_text += event.unicode  
            
        win.blit(bg_main,(0,0))
        #Enter name button
        if player_text !='':
            if Enter_button.draw(win):
                action = True
                if action == True :
                    with open('programe/score.txt','a') as file:
                        file.write(player_text+ ':')
                    action != action
        #play button 
        if Play_button.draw(win):
            if player_text !='':
                action = True
                if action ==True:
                    game() 
                    action != action 
        #score button        
        if Score_button.draw(win):
            action = True
            if action == True  :
                score_page()
                action != action 
        #Exit button       
        if Exit_button.draw(win):
            action = True
            if action ==True:
                run = False
                action != action 
                sys.exit()
                
        draw_text('The Snake',T_font,text_col,win,235,100)
        draw_text('Pornthep Thammawong no.65010682',N_font,text_col,win,20,10)
        draw_text('Enter Name: '+ ' '+player_text,P_font,text_col,win,315,200)
        pygame.draw.rect(win,(255,255,255),input_rect,2)
        clock.tick(fps)
        pygame.display.update()  
    

 #save top5 player 

def top5_score():
    scores = []
    with open('programe/score.txt','r') as file:
        for line in file:
            name,score = line.split(':')
            score = int(score)
            scores.append((name,score))
    scores.sort(key = lambda s: s[1], reverse=True)

    with open('programe/top5player.txt','w') as f:
        for name,score in scores[:5]:
            f.write(name+':'+str(score)+'\n')
            print((name,score))
          
#show top 5 score            
def showtop5_score():
    with open('programe/top5player.txt','r') as file:
            for n,line in enumerate(file):
                text = game_font.render(str(n+1)+"."+line[:-1],True,(255,255,255))
                text_rect = text.get_rect()
                text_rect.centerx = (screen_size//2) +20
                text_rect.centery = n*70 + 210
                win.blit(text,text_rect)

#score page
def score_page():
    run =True
    action = False
    top5_score()
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
        draw_text('Top 5 player score',T_font,text_col,win,100,100)
        showtop5_score()
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
                
        win.fill((175, 215, 70))
        main_game.draw_elements(cell_number,cell_size,win,apple,game_font)
        clock.tick(fps)
        pygame.display.update()  


#main function
if __name__ == '__main__':         
    main_menu()