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

    shadow = Image.open(SHADOW_PATH)

    for t in FORMULA:
        s = t[0]
        d = t[1]

        for i in range(3):
            sx = (s[0] * FRAMES + i) * FRAME_WIDTH
            sy = s[1] * FRAME_HEIGHT
            src_box = ( sx, sy, sx + FRAME_WIDTH, sy + FRAME_HEIGHT)

            dx = (d[0] * FRAMES + i) * FRAME_WIDTH
            dy = d[1] * FRAME_HEIGHT
            dst_box = ( dx, dy, dx + FRAME_WIDTH, dy + FRAME_HEIGHT)

            wx = dx + SHADOW_OFFX
            wy = dy + SHADOW_OFFY

            dst.paste(shadow, (wx, wy), shadow)

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

