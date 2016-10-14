import png
import world
import argparse


class Main:

    def __init__(self):
        self.w = 512
        self.h = 512
        self.pixels = None
        self.base = 0


    def main(self):
        self.parse_args()
        self.create_pixels()
        self.save_image()


    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-b", "--base", help="base for the noise function", type=int, default=0)
        parser.add_argument("-x", "--width", help="width of the world map", type=int, default=512)
        parser.add_argument("-y", "--height", help="height of the world map", type=int, default=512)
        args = parser.parse_args()
        self.base = args.base
        self.w = args.width
        self.h = args.height


    def create_pixels(self):
        """
        Create the pixel array that can be saved as a png. The pixels
        are computed from a `world` generator; see `world` module.
        """
        self.pixels = []
        world_generator = world.world1(self.w, self.h, self.base)
        try:
            for vertical in range(self.h):
                row = []
                for horizontal in range(self.w):
                    value = next(world_generator) * 255
                    row.append( [value, value, value] )
                self.pixels.append(row)

        except StopIteration:
            pass


    def save_image(self, filename="world.png"):
        image = png.from_array(self.pixels, 'RGB')
        image.save(filename)


if __name__ == '__main__':
    Main().main()
