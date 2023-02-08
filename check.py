import glob
import os
import re

from pathlib import Path
from PIL import Image, ImageFile, ImageGrab, ImageDraw

from common import *


def check_assets() -> Assets:

    actors = check_actors()

    assets = Assets(len(actors), actors)

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


def check_actions(actor: str) -> list[Action]:

    actions: list[Action] = []

    action_dirs = glob.glob(f'{IN_DIR}/{actor}/*')

    for action_dir in action_dirs:

        if not os.path.isdir(action_dir):
            continue

        dirname = Path(action_dir).name

        sprites = check_sprites(actor, dirname)
        shadows = check_shadows(actor, dirname)

        action: Action = Action(dirname, len(sprites), sprites, shadows)
        actions.append(action)
    
    return actions


def check_sprites(actor: str, action: str) -> list[Direction]:

    sprites: list[Direction] = []

    for i in range(8):

        pattern = f'{IN_DIR}/{actor}/{action}/*_{i}*{EXT}'

        frames = check_frames(actor, action, pattern)
        
        sprite: Direction = Direction(i, len(frames), frames)

        sprites.append(sprite)
    
    return sprites


def check_shadows(actor: str, action: str) -> list[Direction]:

    shadows: list[Direction] = []

    for i in range(8):
    
        pattern = f'{IN_DIR}/{actor}/{action}/{SHADOWS_DIR}/*_{i}*{EXT}'

        frames = check_frames(actor, action, pattern)

        shadow: Direction = Direction(i, len(frames), frames)

        shadows.append(shadow)
    
    return shadows


def check_frames(actor: str, action: str, pattern: str) -> list[Frame]:

    frames: list[Frame] = []

    images = glob.glob(pattern)

    for image in images:

        if not os.path.isfile(image):
            continue

        filename = Path(image).name

        numbers = re.search(REGEX, filename)

        if not numbers:
            continue

        index = int(numbers.group(2))

        box = check_bbox(image)
        frame = Frame(index, filename, image, box)

        frames.append(frame)

    return frames


def check_bbox(path: str) -> Box:

    image = Image.open(path)
    l, t, r, b = image.getbbox()

    return Box(l, t, r, b)


def print_counts(assets: Assets):

    error: str = ''

    print(f'actors: {assets.count}')

    for actor in assets.actors:
        print(f'{actor.name} actions: {actor.count}')
        
        for action in actor.actions:
            print(f'\t{actor.name} {action.name} sprites:')

            for i in range(8):

                if action.sprites[i].count != action.shadows[i].count:
                    error = 'not equal!'
                else:
                    error = ''
                
                print(f'\t{i}\t{action.sprites[i].count}\t{action.shadows[i].count}\t{error}')


def check_mcbbox(assets: Assets):

    print(f'check min common bounding box...')

    box: Box = Box(FRAME_WIDTH/2, FRAME_HEIGHT/2, FRAME_WIDTH/2, FRAME_HEIGHT/2)

    for actor in assets.actors:
        for action in actor.actions:
            for direction in action.sprites:
                for frame in direction.frames:
                    change = False
                    if frame.box.l < box.l:
                        box.l = frame.box.l
                        change = True
                    if frame.box.t < box.t:
                        box.t = frame.box.t
                        change = True
                    if frame.box.r > box.r:
                        box.r = frame.box.r
                        change = True
                    if frame.box.b > box.b:
                        box.b = frame.box.b
                        change = True
                    
                    if change:
                        print(f'{box}\t{frame.box}\t{frame.path}')
    
    print(f'min common bounding box: {box}')


def main():

    print('check sprite files...')

    assets = check_assets();

    print_counts(assets);

    check_mcbbox(assets);

    print('done!')


if __name__ == '__main__':
    main()