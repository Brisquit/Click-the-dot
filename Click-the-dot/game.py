import sys
import random
import pygame

from native_resolution import width, height
from circle import Start, Circle, Reverse
from score import Score
from timer import Timer

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Click the dot')
        self.font = pygame.font.Font(None, 30)
        self.score = Score()
        self.timer = Timer()
        self.type = 0
        self.create_start_circle()
         
    def create_start_circle(self):
        self.circle = Start(self)

    def run(self):
        while True:
            self.events()
            self.screen.fill('black')
            if self.timer.time_left == 0:
                self.screen.fill('black')
            if self.type == -2:
                self.time_ran_out_text()
                self.score.score = 0
                self.timer.reset()
            if self.type == -1:
                self.loss_text()
                self.score.score = 0
                self.timer.reset()

            if self.type == 0:
                start_text= self.font.render(f'Click on me to begin :D', True, "white")                
                self.screen.blit(start_text, (width/2-100, height/2-100))
                self.circle.draw("white")

            if self.type == 1:
                self.circle.draw("green")

            if self.type == 2:    
                self.circle.draw("blue")

            score_text = self.font.render(f'Score: {self.score.score}', True, "white")  
            self.screen.blit(score_text, (50, 50))

            time_text = self.font.render(f'Time left: {self.timer.time_left}', True, "white")  
            self.screen.blit(time_text, (50, 80))
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or  event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    self.type = 0
                    self.timer.reset()
                    self.score.score = 0
                    self.circle = Start(self)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.circle.collision():
                        if self.timer.time_left == 30 and not self.timer.on:
                             self.timer.start()
                        self.type = random.randint(1,2)
                        if self.score.score < 5:
                            self.type = 1
                        self.score.scoring()
                        if self.type == -1 or self.type == -2:
                            self.circle.circle_pos(width/2, height/2)
                        current_pos = self.circle.circle_pos
                        if self.type == 1:
                            self.circle = Circle(self, current_pos)
                        if self.type == 2:
                            self.circle = Reverse(self, current_pos)
                        if self.type == 0:
                            self.circle = Start(self, current_pos)
                        self.circle.randomize_pos()           
                    else:
                        self.type = - 1
                
    def loss_text(self):
        loss_text = self.font.render('Sorry, you missed. Better luck next time', True, "white")                
        self.screen.blit(loss_text, (width/2-200, height/2-100))

        loss_text = self.font.render(f'Score: {self.score.last_score}' , True, "white")                
        self.screen.blit(loss_text, (width/2-200, height/2+30-100))

        loss_text = self.font.render(f'HighScore: {self.score.highscore}', True, "white")                
        self.screen.blit(loss_text, (width/2-200, height/2+60-100))
        
        loss_text = self.font.render('Press "R" to restart or "Q" to quit', True, "white")                
        self.screen.blit(loss_text, (width/2-200, height/2+90-100))

    def time_ran_out_text(self):
        time_text = self.font.render('Time ran out', True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2-100))
        
        time_text = self.font.render(f'Score: {self.score.last_score}' , True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2+30-100))
        
        time_text = self.font.render(f'HighScore: {self.score.highscore}', True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2+60-100))
        
        time_text = self.font.render('Press "R" to restart or "Q" to quit', True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2+90-100))
        
                            
