"""
# DO NOT EDIT THIS FILE #
"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg

pg.init()
try:
    pg.mixer.init()
except:
    print('Failed to initialize mixer')

from .game_object import GameObject
from .input_manager import InputManager
from .physic_sprite import PhysicSprite
from .sound_manager import SoundManager
from .sprite import Sprite
from .world import World
from .transform import Transform
from .vec2 import Vec2


class TitoEngine:
    def __init__(self, win_title: str = 'Tito Engine Game', win_resolution: tuple[int, int] = (1080, 720), colour_fill: tuple[int, int, int] = (255, 255, 255), fps: int = 60):
        pg.display.set_caption(win_title)

        self.WIN = pg.display.set_mode(win_resolution)
        self.CLOCK = pg.time.Clock()
        self.FPS = fps
        self.COLOUR_FILL = colour_fill

        self.initialized = True
        print('Tito Engine Initialized Successfully')

    def run(self, game_objects: list[GameObject] = []):
        self.world = World(self.WIN, game_objects)

        running = True
        firstTick = False

        # Main Loop
        while running:
            # First tick
            if firstTick == False:
                firstTick = True

            # Updating window
            DELTA_TIME = self.CLOCK.tick(self.FPS)/1000.0
            self.WIN.fill(self.COLOUR_FILL)

            self.world.update()

            # Close Window when 'X' pressed
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    running = False
                    return 0

            pg.display.update()
