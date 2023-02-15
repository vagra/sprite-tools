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


def marge_sprites(action: Action):

    print(f'marge sprites of action {action.name}')

    out_width = FRAME_WIDTH * action.frames

    sheet = Image.new("RGBA", (out_width, FRAME_HEIGHT * DIRECTIONS), (0, 0, 0, 0))

    for i in range(DIRECTIONS):
        for j in range(action.frames):
            sprite = action.sprites[i][j]
            frame = Image.open(sprite.path)
            
            offx = int((FRAME_WIDTH - sprite.size.w) / 2)
            offy = int((FRAME_HEIGHT - sprite.size.h) / 2)

            x = FRAME_WIDTH * j + offx
            y = FRAME_HEIGHT * i + offy

            sheet.paste(frame, (x, y), frame)
        
    sheet.save(f'{OUT_DIR}/{action.name}{EXT}')


def main():

    print('marge sprites to sprite sheets')

    assets = check_assets();

    for action in assets.actions:
        marge_sprites(action)

    print('done!')


if __name__ == '__main__':
    main()

