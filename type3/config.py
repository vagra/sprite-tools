from dataclasses import dataclass


IN_DIR = '../input/type3'
OUT_DIR = '../output/type3'

ACTOR_PRE = 'hero'
ACTION_PRE = 'ch00'
EXT = '.png'

FRAME_WIDTH = 128
FRAME_HEIGHT = 128

FRAMES = 64

ACTORS = 8
ACTIONS = 12
DIRECTIONS = 8

FORMULA = [
    [0, 1, 3, 4, 5],
    [0, 1, 2, 3, 4, 5, 6]
]

@dataclass
class Action:
    index: str
    name: str
    path: str
    frames: int

@dataclass
class Actor:
    index: int
    name: str
    count: int
    actions: list[list[Action]]
    frames: int

@dataclass
class Assets:
    count: int
    actors: list[Actor]