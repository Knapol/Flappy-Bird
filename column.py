from settings import *

class Column(pg.sprite.Sprite):
    def __init__(self, game, xpos, height, inverted):
        super().__init__(game.col_group)
        self.image = pg.image.load('sprites/pipe-green.png')
        self.image = pg.transform.scale(self.image, (COL_WIDTH, COL_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect[1] = height - COL_HEIGHT
        else:
            self.rect[1] = HEIGHT - height

        self.enter = False
        self.exit = False
        self.passed = False
        self.inverted = inverted
        self.game = game

    def update(self):
        self.rect[0] -= GAME_SPEED

        if not self.inverted:
            if self.game.bird.rect[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if self.game.bird.rect[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                self.game.score.update_score()
            