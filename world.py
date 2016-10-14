from noise import pnoise2
from math import log

def generate_noise_map(w, h, divider, octaves=1, persistence=0.5, base=0):
    """
    A generator for numerous single noise values. Values are yieled as arranged inside rows.
    When a row ends, the next value will be on the next row, and so on.
    Values are -1...+1 as per the noise function.
    """
    for vertical in range(h):
        for horizontal in range(w):
            value = pnoise2(horizontal / divider,
                            vertical / divider,
                            octaves=octaves,
                            persistence=persistence,
                            base=base)
            yield value


def world1(w, h, base=0):
    """
    An example of creating a world with noise layers.

    Stuff to note:

     - We yield a single value. This is stupid. We should actually yield several 'world layers'
       i.e. things like typography, trees, swamps, resources, etc...
       These layers could be then used to generate proper texture images or game logic
       calculations instead of generating a stupid greyscale image.

    """
    plates = generate_noise_map(w, h, w/3, 1, base=base)
    hills = generate_noise_map(w, h, w/5, 2, 0.44, base=base)
    trees = generate_noise_map(w, h, w/8, 3, 0.76, base=base)
    speckle = generate_noise_map(w, h, w/150, octaves=2, persistence=0.1, base=base)

    for vertical in range(h):
        for horizontal in range(w):
            """Now the fun custom parts begin. These will be differnet per world type"""
            base_value = next(plates)
            value = base_value + next(hills) / 2.2
            speckle_value = next(speckle) / 4

            if base_value < 0.144 and base_value > -0.2:
                value += speckle_value

            tree_value = next(trees)
            if (tree_value > 0):
                value += tree_value

            if value > 1:
                value = 1

            if value < -1:
                value = -1

            value = (value + 1) / 2

            yield value

