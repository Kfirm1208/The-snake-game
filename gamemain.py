import pygame
from game_over import game_over
import snake,fruit


class Game_main: 
    def __init__(self,size_number):
        self.snake = snake.SNAKE()
        self.fruit = fruit.FRUIT(size_number)
        self.score = 0

    def update(self,size_number):
    
        self.snake.snake_move()
        self.check_collision(size_number)
        self.check_fail(size_number)
        

    def draw_elements(self,size_number,size,surface,apple,font):
        self.draw_grass(size_number,size,surface)
        self.fruit.draw_fruit(size,surface,apple)
        self.snake.draw_snake(size,surface)
        self.draw_score(font,size,size_number,apple,surface)
       
    def check_collision(self,size_number):
        if self.fruit.pos == self.snake.body[0]:
            # reposition fruit
            self.fruit.randomize(size_number)
            # add another block to snake
            self.snake.add_block()
            # add sound
            self.snake.play_crunch_sound()
            # fruit not spawn in snake
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize(size_number)
                    
    def check_fail(self,size_number):
        # check if snake hits screen
        if not 0 <= self.snake.body[0].x < size_number or not 0 <= self.snake.body[0].y < size_number:
            self.gameover()             
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
               self.gameover()
               
    def gameover(self):
        score =self.score
        self.record_score()
        game_over(score)
              
    def draw_grass(self,size_number,size,surface):
        grass_color = (167,209,61)
        
        for row in range(size_number):
            if row %2 ==0 :
                for col in range(size_number):
                    if col%2 == 0 :
                        grass_rect = pygame.Rect(col * size,row * size,size,size)
                        pygame.draw.rect(surface,grass_color,grass_rect)
    
            else: 
                for col in range(size_number):
                    if col%2 != 0 :
                        grass_rect = pygame.Rect(col * size,row * size,size,size)
                        pygame.draw.rect(surface,grass_color,grass_rect)
    
    def draw_score(self,font,size,size_number,apple,surface):
        score_text = str(len(self.snake.body) - 3 )                 
        score_surface = font.render(score_text,True,(56,74,12))  
        score_x = int(size * size_number -60)
        score_y = int(size * size_number -40) 
        score_rect = score_surface.get_rect(center = (score_x,score_y))           
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width +
                            apple_rect.width+6,apple_rect.height)
        self.score = int(score_text)        
        pygame.draw.rect(surface,(167,209,61),bg_rect)
        surface.blit(score_surface,score_rect)
        surface.blit(apple,apple_rect)                 
        pygame.draw.rect(surface,(56,74,12),bg_rect,2)
    
    
    def record_score(self):
        if self.score >= 0:
            try:
                with open('score.txt','a') as file:
                    file.write(str(self.score) + "\n")
            except Exception as e:
                print(e)        
    
        