import pygame as pg

vec = pg.Vector2

WIDTH = 400
HEIGHT = 600
GAME_RES = (WIDTH, HEIGHT)

GROUND_HEIGHT = 100
GROUND_WIDTH = 2 * WIDTH

COL_WIDTH = 80
COL_HEIGHT = 500

MIN_COL_SIZE = 100
MAX_COL_SIZE = 300
COL_GAP = 150

GRAVITY = 0.5
JUMP_SPEED = 9
MAX_VELOCITY = 8

FPS = 60
GAME_SPEED = 2

BACKGROUND = pg.transform.scale(pg.image.load('sprites/background-day.png'), (WIDTH, HEIGHT))
GAME_OVER = pg.image.load('sprites/gameover.png')

SCORE_IMAGE_WIDTH = 24