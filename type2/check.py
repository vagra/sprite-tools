import glob
import os
import re

from pathlib import Path
from PIL import Image, ImageFile, ImageGrab, ImageDraw

from config import *


def check_assets() -> Assets:

    actions = check_actions()

    assets = Assets(len(actions), actions)

    return assets


def check_actors() -> list[Actor]:

    actors: list[Actor] = []

    actor_dirs = glob.glob(f'{IN_DIR}/*')

    for actor_dir in actor_dirs:

        if not os.path.isdir(actor_dir):
            continue

        dirname = Path(actor_dir).name

        actions = check_actions(dirname)

        actor: Actor = Actor(dirname, len(actions), actions)
        actors.append(actor)
    
    return actors


def check_actions() -> list[Action]:

    actions: list[Action] = []

    action_dirs = glob.glob(f'{IN_DIR}/*')

    for action_dir in action_dirs:

        if not os.path.isdir(action_dir):
            continue

        dirname = Path(action_dir).name

        sprites = check_sprites(dirname)

        if len(sprites) != DIRECTIONS:
            continue

        action: Action = Action(dirname, len(sprites[0]), sprites)
        actions.append(action)
    
    return actions


def check_sprites(action: str) -> list[list[Sprite]]:

    sprites: list[list[Sprite]] = [[] for i in range(DIRECTIONS)]

    n = 0
    while True:
        n += 1

        path = f'{IN_DIR}/{action}/{action}_{n:03}{EXT}'

        if not os.path.exists(path):
            break

        if not os.path.isfile(path):
            continue

        direction = n % DIRECTIONS - 1
        index = int(n / 8)
        filename = Path(path).name
        size = check_size(path)
        sprite = Sprite(index, filename, path, size)

        sprites[direction].append(sprite)
    
    count = 0
    for i in range(DIRECTIONS):
        if len(sprites[i]) == 0:
            return []
        
        if count == 0:
            count = len(sprites[i])
            continue

        if count != len(sprites[i]):
            return []
    
    return sprites


def check_size(path: str) -> Size:

    image = Image.open(path)
    w, h = image.size

    return Size(w, h)


def print_counts(assets: Assets):

    error: str = ''

    print(f'actors: {assets.count}')

    for action in assets.actions:
        print(f'{action.name} sprites:')

        for i in range(8):
            print(f'  {i}  {action.frames}')


def check_maxsize(assets: Assets):

    print(f'check max size of sprites...')

    size: Size = Size(0, 0)

    for action in assets.actions:
        for i in range(DIRECTIONS):
            for frame in action.sprites[i]:
                change = False
                if frame.size.w > size.w:
                    size.w = frame.size.w
                    change = True
                if frame.size.h > size.h:
                    size.h = frame.size.h
                    change = True
                
                if change:
                    print(f'{size}\t{frame.size}\t{frame.path}')
    
    print(f'max size of sprites: {size}')


def main():

    print('check sprite files...')

    assets = check_assets();

    print_counts(assets);

    check_maxsize(assets);

    print('done!')


if __name__ == '__main__':
    main()