from dataclasses import dataclass


IN_DIR = '../input/type5'
OUT_DIR = '../output/type5'

ACTOR_PRE = 'hero'
EXT = '.png'

FRAME_WIDTH = 128
FRAME_HEIGHT = 128

ACTORS = 8
ACTIONS = 12
DIRECTIONS = 8

FORMULA = [
    (0, 6),
    (1, 5),
    (2, 4),
    (3, 3),
    (4, 2),
    (5, 1),
    (6, 0),
    (7, 7)
]


@dataclass
class Actor:
    index: int
    name: str
    path: str
    frames: int

@dataclass
class Assets:
    count: int
    actors: list[Actor]