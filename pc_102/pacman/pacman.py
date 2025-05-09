#!/usr/bin/env python3

import pygame as pg

### Representation of levels and ghosts
import level
import ghost
import random

### some convenient color names
green  = pg.Color('#00FF00')
black  = pg.Color('black')
yellow = pg.Color('yellow')

from enum import Enum

class PacmanMode(Enum):
    ALIVE = 0
    DEAD = 1
    STANDARD_FREQUENCY = 200
    FAST_FREQUENCY = 100

class Pacman:
    def __init__(self, level_info : level.Level) -> None:
        self.level : level.Level = level_info    # the "level" is the current board
        self.score : int = 0                     # the score the Pac-Man has achieved
        self.pos : tuple[int,int] = (0, 0)       # the cell coordinates of the Pac-Man
        self.time_since_last_move : int = 0           # time since the last move
        self.crt_mode = "standard"
        self.speed_timer = 0
        ### The above are dummy values; the real values come from
        ### the following .reset() function
        self.reset()

    def reset(self) -> None:
        """Set the default values for the starting state of the Pac-Man."""
        (pr, pc, pw, ph) = self.level.pit
        self.pos  = (pr + ph, pc + pw // 2)
        self.score = 0
        # maybe set other variables/attributes?

    def project_pos(self) -> tuple[int,int]:
        return (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    def update(self, millis : int, ghosts : list[ghost.Ghost]) -> None:
        """Update the Pac-Man's state.

        millis: number of milliseconds that have elapsed since the last
                time update() was called
        ghosts: a list of all the ghost entities on the level. The Pac-Man
                should **not** modify the ghost entities, but is allowed
                to retrieve information about the ghosts"""
        # TODO
        self.speed_timer += millis
        if self.crt_mode == "fast" and self.speed_timer > 15000:
            self.crt_mode = "standard"
            self.speed_timer = 0
        if self.time_since_last_move < 200 and not (self.crt_mode == "fast" and self.time_since_last_move > 100): 
            self.time_since_last_move += millis
            return
        self.time_since_last_move = 0

        # nbh = self.level.neighbors(self.pos)
        # self.pos = random.choice(nbh)

        if not self.level.can_enter(self.project_pos()):
            self.direction = (0, 0)
            return
        self.pos = self.project_pos()

        if self.level.cells[self.pos[0]][self.pos[1]] == level.Cell.PILL:
            self.score += 1
            self.level.cells[self.pos[0]][self.pos[1]] = level.Cell.EMPTY
        elif self.level.cells[self.pos[0]][self.pos[1]] == level.Cell.POWERPILL:
            self.score += 10
            self.level.cells[self.pos[0]][self.pos[1]] = level.Cell.EMPTY
            self.crt_mode = "fast"
            self.speed_timer = 0

    def process_event(self, event : pg.event.Event) -> None:
        """Make the Pac-Man respond to the event, if relevant. It should
        only respond to the movement keys (WASD or the arrow keys)."""
        # TODO
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.direction = (-1, 0)
            elif event.key == pg.K_DOWN:
                self.direction = (1, 0)
            elif event.key == pg.K_LEFT:
                self.direction = (0, -1)
            elif event.key == pg.K_RIGHT:
                self.direction = (0, 1)
        elif event.type == pg.KEYUP:
            
            self.direction = (0, 0)
            

    def render(self, window : pg.surface.Surface) -> None:
        """Draw the Pac-Man on the given window"""
        # scale params
        cw = window.get_width() // (self.level.width + 2)
        ch = window.get_height() // (self.level.height + 2)
        y = int((self.pos[0] + 1) * ch)
        x = int((self.pos[1] + 1) * cw)

        ## body, a yellow circle
        pg.draw.circle(window, yellow, (x + cw//2, y + ch//2), cw * 2 // 5)
        ## mouth, a black filled wedge
        pg.draw.polygon(window, black, [(x + cw//2, y + ch//2), (x + cw, y), (x + cw, y + ch)])
