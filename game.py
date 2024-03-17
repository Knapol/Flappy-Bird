from settings import *
from column import Column
from ground import Ground
from bird import Bird
from score import Score
import random

class Game:
    def __init__(self, app):
        self.app = app
        self.col_group = pg.sprite.Group()
        self.ground_group = pg.sprite.Group()
        self.bird_group = pg.sprite.GroupSingle()
        
        for i in range(2):
            Ground(self, GROUND_WIDTH * i)

        for i in range(2):
            self.get_random_col(WIDTH * i + 800)

        self.bird = Bird(self)

        self.score = Score(self.app.screen)

    def update(self):
        self.col_group.update()
        self.ground_group.update()

        if self.is_off_screen(self.ground_group.sprites()[0]):
            self.ground_group.remove(self.ground_group.sprites()[0])
            
            Ground(self, GROUND_WIDTH - GAME_SPEED)
        
        if self.is_off_screen(self.col_group.sprites()[0]):
            self.col_group.remove(self.col_group.sprites()[0])
            self.col_group.remove(self.col_group.sprites()[0])

            self.get_random_col(WIDTH*2)
        
        self.bird_group.update()

        self.detect_collision()

    def draw(self):
        self.col_group.draw(self.app.screen)
        self.ground_group.draw(self.app.screen)
        self.bird_group.draw(self.app.screen)
        self.score.draw()

    def is_off_screen(self, sprite):
        return sprite.rect[0] < -sprite.rect[2]
    
    def get_random_col(self, xpos):
        size = random.randint(100, 300)
        Column(self, xpos, size, True)
        Column(self, xpos, HEIGHT - size - COL_GAP, False)

    def bird_jump(self):
        self.bird.jump()

    def detect_collision(self):
        collision_columns = pg.sprite.spritecollide(self.bird_group.sprite, self.col_group, False)
        collision_ground = pg.sprite.spritecollide(self.bird_group.sprite, self.ground_group, False)

        if collision_columns or collision_ground:
            self.app.screen.blit(GAME_OVER, (((WIDTH - GAME_OVER.get_width()) // 2, (HEIGHT - GAME_OVER.get_height()) // 2)))
            self.app.running = False
            pg.display.flip()

    