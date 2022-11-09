import pygame,sys
from snake import SNAKE
from button import Button
from text import draw_text

def game_over():
    win = pygame.display.set_mode(((40*20),(40*20)))
    font_over = pygame.font.Font('Font/PoetsenOne-Regular.ttf',70)
    font_score = pygame.font.Font('Font/PoetsenOne-Regular.ttf',50)
    Exit_button = Button('Exit',210,50,(310,600),3)
     
    run = True
    snake =SNAKE()
               
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            win.fill((255,100,0))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    sys.exit() 
                          
                #event button 
            if Exit_button.draw(win):
                    run = False
                    sys.exit() 
                          
            
            draw_text('Game Over',font_over,(255,255,255),win,240,250)  
            draw_text
            pygame.display.update()     