from dataclasses import dataclass


IN_DIR = '../input/type2'
OUT_DIR = '../output/type2'

REGEX = '.*_(\d{3})\.png'
EXT = '.png'

FRAME_WIDTH = 128
FRAME_HEIGHT = 128

ROWS = 2
COLUMNS = 4
FRAMES = 6
DIRECTIONS = 8

FORMULA = {
    'attack':	[0,	 3,	7,	10,	14,	17],
    'block':	[0,	 3,	6,	9,	12,	15],
    'death':	[0,	 2,	3,	5,	6,	8],
    'got-hit':	[0,	 2,	5,	7,	10,	12],
    'idle':	    [0,	 3,	6,	9,	12,	15],
    'jump':	    [0,	 3,	6,	9,	12,	15],
    'run':	    [0,	 3,	6,	10,	13,	16],
    'walk':	    [0,	 3,	6,	8,	11,	14]
}


@dataclass
class Size:
    w: int
    h: int

@dataclass
class Sprite:
    index: int
    name: str
    path: str
    size: Size

@dataclass
class Action:
    name: str
    frames: int
    sprites: list[list[Sprite]]

@dataclass
class Actor:
    name: str
    count: int
    actions: list[Action]

@dataclass
class Assets:
    count: int
    actions: list[Action]