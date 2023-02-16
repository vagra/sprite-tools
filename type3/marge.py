import glob
import os
import re
import shutil

from pathlib import Path
from collections import namedtuple
from dataclasses import dataclass

from PIL import Image, ImageFile, ImageGrab, ImageDraw

from config import *
from check import check_assets


def marge_actions(actor: Actor):

    print(f'marge actions of actor {actor.name}')

    out_width = FRAME_WIDTH * actor.frames

    sheet = Image.new("RGBA", (out_width, FRAME_HEIGHT * DIRECTIONS), (0, 0, 0, 0))

    n = 0
    for b in range(2):
        for i in FORMULA[b]:
            action = actor.actions[b][i]
            frame = Image.open(action.path)

            x = FRAME_WIDTH * n
            y = 0

            sheet.paste(frame, (x, y), frame)

            n += action.frames
        
    sheet.save(f'{OUT_DIR}/{actor.name}{EXT}')


def main():

    print('marge actions to sprite sheets')

    assets = check_assets();

    for actor in assets.actors:
        marge_actions(actor)

    print('done!')


if __name__ == '__main__':
    main()

