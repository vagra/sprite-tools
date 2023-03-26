import glob
import os
import re

from pathlib import Path
from PIL import Image, ImageFile, ImageGrab, ImageDraw

from config import *


def check_assets() -> Assets:

    actors = check_actors()

    assets = Assets(len(actors), actors)

    return assets


def check_actors() -> list[Actor]:

    actors: list[Actor] = []
    frames: int = FRAMES * ACTIONS

    for i in range(ACTORS):

        actor_name = f'{ACTOR_PRE}{i}{ACTOR_FIX}'
        actor_path = f'{IN_DIR}/{actor_name}{EXT}'
        print(actor_path)

        if not os.path.exists(actor_path):
            continue

        if not os.path.isfile(actor_path):
            continue

        actor: Actor = Actor(i, actor_name, actor_path, frames)

        actors.append(actor)
    
    return actors


def print_counts(assets: Assets):

    error: str = ''

    print(f'actors: {assets.count}')

    for actor in assets.actors:
        print(f'{actor.index}  ', end='')
        print(f'{actor.name}  ', end='')
        print(f'{actor.path}')

def main():

    print('check action files...')

    assets = check_assets();

    print_counts(assets);

    print('done!')


if __name__ == '__main__':
    main()