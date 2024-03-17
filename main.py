import sys
from settings import *
from game import Game

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Flappy Bird') 
        self.screen = pg.display.set_mode(GAME_RES)
        self.clock = pg.time.Clock()

        self.game = Game(self)
        self.running = True

    def check_for_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.game.bird_jump()

    def update(self):
        self.game.update()

    def draw(self):
        self.screen.blit(BACKGROUND, (0, 0))
        self.game.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.check_for_events() 

            self.update()

            if self.running:
                self.draw()

            self.clock.tick(FPS)

if __name__ == '__main__':
    app = App()
    app.run()