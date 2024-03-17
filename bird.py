from settings import *

class Bird(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game.bird_group)

        self.images =  [pg.image.load('sprites/bluebird-upflap.png').convert_alpha(),
                        pg.image.load('sprites/bluebird-midflap.png').convert_alpha(),
                        pg.image.load('sprites/bluebird-downflap.png').convert_alpha()]
        
        self.image_index = 0
        self.image = self.images[self.image_index]

        self.rect = self.image.get_rect()
        self.rect[0] = WIDTH / 6
        self.rect[1] = HEIGHT / 2

        self.velocity = 0

    def update(self):
        self.image_index = (self.image_index + 1 ) % 3
        self.image = self.images[self.image_index]

        self.velocity += GRAVITY
        if self.velocity > MAX_VELOCITY:
            self.velocity = MAX_VELOCITY

        self.rect[1] += int(self.velocity)

        self.image = pg.transform.rotate(self.image, self.velocity * -2)

    def jump(self):
        self.velocity = -JUMP_SPEED