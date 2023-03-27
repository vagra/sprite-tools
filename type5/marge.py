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
    out_height = FRAME_HEIGHT * DIRECTIONS

    src = Image.open(actor.path)
    dst = Image.new("RGBA", (out_width, out_height), (0, 0, 0, 0))

    for t in FORMULA:
        s = t[0]
        d = t[1]

        for i in range(actor.frames):
            x = i * FRAME_WIDTH
            
            sy = s * FRAME_HEIGHT
            dy = d * FRAME_HEIGHT

            src_box = ( x, sy, x + FRAME_WIDTH, sy + FRAME_HEIGHT)
            dst_box = ( x, dy, x + FRAME_WIDTH, dy + FRAME_HEIGHT)

            frame = src.crop(src_box)
            dst.paste(frame, dst_box, frame)
        
    dst.save(f'{OUT_DIR}/{actor.name}{EXT}')


def main():

    print('marge actions to sprite sheets')

    assets = check_assets();

    for actor in assets.actors:
        marge_actions(actor)

    print('done!')


if __name__ == '__main__':
    main()

