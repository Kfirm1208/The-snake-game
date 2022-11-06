import pygame 
import random
from pygame import Vector2

class FRUIT:
    def __init__(self,number_size):
        self.randomize(number_size)

    def draw_fruit(self,size,surface,apple):
        fruit_rect = pygame.Rect(
            (self.pos.x*size), (self.pos.y*size), size, size)
        surface.blit(apple, fruit_rect)

    def randomize(self,number_size):
        self.x = random.randint(0, number_size - 2)
        self.y = random.randint(0, number_size - 2)
        self.pos = Vector2(self.x, self.y)