import math
import random
import pygame

from native_resolution import width, height

class Start:

    def __init__(self, game, pos=((width/2, height/2))):
        self.game = game
        self.color = ""
        self.circle_pos = pos

    def draw(self, color):
         pygame.draw.circle(self.game.screen, color, self.circle_pos, width/30)

    def collision(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if math.sqrt((mouse_pos[0] - self.circle_pos[0])**2 + (mouse_pos[1] - self.circle_pos[1])**2) <= width/30:
            return True
        return False
    
    def randomize_pos(self):
        pass

class Circle(Start):

    def randomize_pos(self):
        x, y = self.circle_pos
        x = x - 150 + random.randint(0, 300)
        if x >= width:
            x = x - 300
        elif x <= 50:
            x = x + 300
        y = y - 150 + random.randint(0, 300)
        if y >= height-50:
            y = y - 300
        elif y <=50:
            y = y + 300
        self.circle_pos = (x, y)  

class Reverse(Start):

    def randomize_pos(self):
        x, y = self.circle_pos
        x = abs(width - x)
        y = abs(height - y)
        self.circle_pos = (x, y)