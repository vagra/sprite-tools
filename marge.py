import glob
import os
import re
import shutil

from pathlib import Path
from collections import namedtuple
from dataclasses import dataclass

from PIL import Image, ImageFile, ImageGrab, ImageDraw

from common import *
from check import check_assets


def marge_sprites(actor: Actor):

    print(f'marge sprites of actor {actor.name}')

    sheet = Image.new("RGBA", (OUT_WIDTH, OUT_HEIGHT), (0, 0, 0, 0))

    action = 0
    for row in range(ROWS):
        for col in range(COLUMNS):
            for direction in range(DIRECTIONS):
                frames = FORMULA[actor.actions[action].name]
                print("frames: ", frames)
                frame = 0
                for index in frames:
                    shadow_path = actor.actions[action].shadows[direction].frames[index].path
                    sprite_path = actor.actions[action].sprites[direction].frames[index].path

                    # print(shadow_path)
                    # print(sprite_path)

                    shadow = Image.open(shadow_path)
                    sprite = Image.open(sprite_path)

                    shadow = shadow.resize((SCALE_WIDTH, SCALE_HEIGHT), Image.Resampling.NEAREST)
                    sprite = sprite.resize((SCALE_WIDTH, SCALE_HEIGHT), Image.Resampling.NEAREST)
                    
                    x = SCALE_WIDTH * ( FRAMES * col + frame )
                    y = SCALE_WIDTH * ( DIRECTIONS * row + direction )

                    print(x, y, sprite_path)

                    sheet.paste(shadow, (x, y))
                    sheet.paste(sprite, (x, y))

                    frame += 1

            action += 1
        
    sheet.save(f'{OUT_DIR}/{actor.name}{EXT}')


def main():

    print('marge sprites to sprite sheets')

    assets = check_assets();

    for actor in assets.actors:
        marge_sprites(actor)

    print('done!')


if __name__ == '__main__':
    main()

