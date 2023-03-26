from dataclasses import dataclass


IN_DIR = '../input/type4'
OUT_DIR = '../output/type4'

ACTOR_PRE = 'actor-'
ACTOR_FIX = '-0'
EXT = '.png'

SHADOW_PATH = f'{IN_DIR}/shadow.png'
SHADOW_OFFX = 30
SHADOW_OFFY = 80

FRAME_WIDTH = 100
FRAME_HEIGHT = 100

FRAMES = 3

ACTORS = 17
ACTIONS = 3
DIRECTIONS = 8

FORMULA = [
    ((0,0), (0,0)),
    ((0,1), (0,6)),
    ((0,2), (0,2)),
    ((0,3), (0,4)),
    ((1,0), (0,7)),
    ((1,1), (0,1)),
    ((1,2), (0,5)),
    ((1,3), (0,3)),
    ((2,0), (1,0)),
    ((2,1), (1,6)),
    ((2,2), (1,2)),
    ((2,3), (1,4)),
    ((3,0), (1,7)),
    ((3,1), (1,1)),
    ((3,2), (1,5)),
    ((3,3), (1,3)),
    ((0,4), (2,0)),
    ((0,5), (2,6)),
    ((0,6), (2,2)),
    ((0,7), (2,4)),
    ((1,4), (2,7)),
    ((1,5), (2,1)),
    ((1,6), (2,5)),
    ((1,7), (2,3)),
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