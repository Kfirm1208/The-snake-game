import pygame
import sys
import button

#window setting
pygame.init()
cell_size = 40
cell_number = 20
win_size = cell_size * cell_number
win = pygame.display.set_mode((win_size,win_size))
icon = pygame.image.load('Graphic/icon.png').convert_alpha()
pygame.display.set_caption('The Snake')
pygame.display.set_icon(icon)

#define background home page
img_main = pygame.image.load('Graphic/background_snake_game.jpg')
bg_main = pygame.transform.scale(img_main,(win_size,win_size))

clock = pygame.time.Clock()
fps = 144
game_play = False
run =True 

#define fonts
N_font =  pygame.font.Font('Font/PoetsenOne-Regular.ttf',20)
T_font =  pygame.font.Font('Font/PoetsenOne-Regular.ttf',70)

#define colors
text_col = (255,255,255)

#define button 
Play_button = button.Button('Play',210,50,(310,250),3)
Score_button = button.Button('Score',210,50,(310,380),3)
Exit_button = button.Button('Exit',210,50,(310,520),3)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    win.blit(img,(x,y))

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
            
    win.blit(bg_main,(0,0))
    if Play_button.draw(win):
        game_play = True
        if game_play ==True:
            print('Play')
    if Score_button.draw(win):
        print('Score')
    if Exit_button.draw(win):
        run = False
        sys.exit()
    draw_text('The Snake',T_font,text_col,240,100)
    draw_text('no.65010682',N_font,text_col,20,10)
    clock.tick(fps)
    pygame.display.update()
    