from dataclasses import dataclass


IN_DIR = '../input/type1'
OUT_DIR = '../output/type1'

SHADOWS_DIR = '_shadows'
SHADOW = 'shadow'

REGEX = '.*_(\d)(\d+)\.png'
EXT = '.png'

FRAME_WIDTH = 299
FRAME_HEIGHT = 240

SCALE_WIDTH = 100
SCALE_HEIGHT = 80

ROWS = 2
COLUMNS = 4
FRAMES = 6
DIRECTIONS = 8

OUT_WIDTH = SCALE_WIDTH * FRAMES * COLUMNS
OUT_HEIGHT = SCALE_HEIGHT * DIRECTIONS * ROWS

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
class Box:
    l: int = 0
    t: int = 0
    r: int = 0
    b: int = 0

@dataclass
class Frame:
    index: int
    name: str
    path: str
    box: Box

@dataclass
class Direction:
    index: int
    count: int
    frames: list[Frame]

@dataclass
class Action:
    name: str
    count: int
    sprites: list[Direction]
    shadows: list[Direction]

@dataclass
class Actor:
    name: str
    count: int
    actions: list[Action]

@dataclass
class Assets:
    count: int
    actors: list[Actor]