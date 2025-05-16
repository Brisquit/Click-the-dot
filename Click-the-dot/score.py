import os

class Scores:

    def __init__(self, filename="highscore.txt"):
        self.filename = filename
        self.score = 0
        self.last_score = 0
        self.highscore = 0
        self.highscore = self.load_highscore()
        
    def scoring(self):
        self.score = self.score + 1
        if self.score >= 1:
            self.last_score = self.score
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
            
    def save_highscore(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.highscore))

    def load_highscore(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return int(file.read())
                except ValueError:
                    return 0
        return 0
