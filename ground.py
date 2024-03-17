from settings import *

class Ground(pg.sprite.Sprite):
    def __init__(self, game, xpos):
        super().__init__(game.ground_group)

        self.image = pg.image.load('sprites/base.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (GROUND_WIDTH, HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = HEIGHT - GROUND_HEIGHT
    
    def update(self):
        self.rect[0] -= GAME_SPEED