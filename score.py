from settings import *

class Score:
    def __init__(self, screen):
        self.score = 0
        self.screen = screen

        self.images = [pg.image.load(f'sprites/{i}.png').convert_alpha() for i in range(10)]

    def draw(self):
        length = self.get_length()
        tmp_score = self.score
        for i in range(length):
            self.screen.blit(self.images[tmp_score % 10], (5 * (length-1) //2 + WIDTH // 2 + length * SCORE_IMAGE_WIDTH // 2 - SCORE_IMAGE_WIDTH * (i+1) - 5 * i, 50))
            tmp_score //= 10

    def get_length(self):
        cnt = 1
        tmp_score = self.score
        while tmp_score > 9:
            tmp_score //= 10
            cnt += 1
        return cnt
    
    def update_score(self):
        self.score += 1