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

    for i in range(ACTORS):

        actor_name = f'{ACTOR_PRE}{i}'
        actor_path = f'{IN_DIR}/{actor_name}'

        if not os.path.exists(actor_path):
            continue

        if not os.path.isdir(actor_path):
            continue

        actions = check_actions(i, actor_path)

        actor: Actor = Actor(i, actor_name, len(actions), actions, 0)
        actor.frames = total_frames(actor)

        actors.append(actor)
    
    return actors


def check_actions(actor_id: int, actor_path: str) -> list[list[Action]]:

    actions: list[list[Action]] = [
        [None for i in range(ACTIONS)],
        [None for i in range(ACTIONS)]
        ]

    for b in range(2):
        for i in range(ACTIONS):

            n = f'{i:x}'

            action_name = f'{ACTION_PRE}{b}{actor_id}{n}'
            action_path = f'{actor_path}/{action_name}{EXT}'

            if not os.path.exists(action_path):
                continue

            if not os.path.isfile(action_path):
                continue

            frames = check_frames(action_path)

            if frames <= 0:
                continue

            action: Action = Action(n, action_name, action_path, frames)
            actions[b][i] = action
    
    return actions


def check_frames(action_path: str) -> int:

    image = Image.open(action_path)
    w, h = image.size

    if h != FRAME_HEIGHT * DIRECTIONS:
        print(f'error height: {h}\t{action_path}')
        return 0

    if w % FRAME_WIDTH != 0:
        print(f'error width: {w}\t{action_path}')
        return 0

    frames = int( w / FRAME_WIDTH )

    return frames

def total_frames(actor: Actor) -> int:
    total = 0
    for d in range(2):
        for i in FORMULA[d]:
            total += actor.actions[d][i].frames

    return total


def print_counts(assets: Assets):

    error: str = ''

    print(f'actors: {assets.count}')

    print(f'A ', end='')
    for b in range(2):
        for i in range(ACTIONS):
            print(f'{b}{i:x} ', end='')
    print(' T')

    for actor in assets.actors:
        print(f'{actor.index} ', end='')

        for b in range(2):
            for i in range(ACTIONS):
                action = actor.actions[b][i]
                if action:
                    print(f'{action.frames:2} ', end='')
                else:
                    print(' 0 ', end='')

        print(f'{actor.frames:2}')

def main():

    print('check action files...')

    assets = check_assets();

    print_counts(assets);

    print('done!')


if __name__ == '__main__':
    main()