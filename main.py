import pygame
import sys
import math
import random
import threading
import time
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
[width, height]= screensize

color = ""

class Start:

    def __init__(self, game, pos=((width/2, height/2))):
        self.game = game
        self.color = color
        self.circle_pos = pos

    def draw(self, color):
         pygame.draw.circle(self.game.screen, color, self.circle_pos, width/30)
         pass

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



class Scores:

    score = 0
    last_score = 0
    highscore = 0

    def __init__(self):
        self.score = 0
        self.last_score = 0
        self.highscore = 0
        
    def scoring(self):
        self.score = self.score + 1
        if self.score >= 1:
            self.last_score = self.score
        if self.score > self.highscore:
            self.highscore = self.score



class Timer:
    def __init__(self):
        self.time_left = 30
        self.on = False
        self.thread = None
        
    def countdown(self):
        while self.time_left > 0 and self.on:
            time.sleep(1)
            self.time_left -= 1

    def start(self):
        if not self.on:
            self.on = True
            self.time_left = 30
            self.thread = threading.Thread(target=self.countdown)
            self.thread.start()

    def stop(self):
        self.on = False
        self.thread = None

    def reset(self):
        self.stop()
        self.time_left = 30 



class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Click the dot')
        self.font = pygame.font.Font(None, 30)
        self.score = Scores()

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
                self.type = - 2 
                self.screen.fill('black')
            if self.type == -2:
                self.circle.draw("gray35")
                self.time_ran_out_text()
                self.score.score = 0
                self.timer.reset()
            if self.type == -1:
                self.circle.draw("gray35")
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
        
        loss_text = self.font.render('Click the gray circle to restart', True, "white")                
        self.screen.blit(loss_text, (width/2-200, height/2+90-100))

    def time_ran_out_text(self):
        time_text = self.font.render('Time ran out', True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2-100))
        
        time_text = self.font.render(f'Score: {self.score.last_score}' , True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2+30-100))
        
        time_text = self.font.render(f'HighScore: {self.score.highscore}', True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2+60-100))
        
        time_text = self.font.render('Click the gray circle to restart', True, "white")                
        self.screen.blit(time_text, (width/2-200, height/2+90-100))
        
                            
if __name__ == "__main__":
    game = Game()
    game.run()