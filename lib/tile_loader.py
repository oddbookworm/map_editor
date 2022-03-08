from asyncore import read
from PIL import Image
import os
try:
    from tile import Tile
except ModuleNotFoundError:
    from .tile import Tile

class SpriteSheetReader:
    def __init__(self, filename, tile_size):
        self.spritesheet = Image.open(filename)
        self.tile_size = tile_size
        self.margin = 0

    def get_tile(self, pos):
        pos_x = self.tile_size * pos[0] + self.margin * (pos[0] + 1)
        pos_y = self.tile_size * pos[1] + self.margin * (pos[1] + 1)

        box = (pos_x, pos_y, pos_x + self.tile_size, pos_y + self.tile_size)
        return self.spritesheet.crop(box)

if __name__ == "__main__":
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    reader = SpriteSheetReader(''.join([parent_dir, "\\assets\\RPG Nature Tileset.png"]),
                                32)

    # tile1 = reader.get_tile((0, 0))
    # print(type(tile1))

    tile2 = reader.get_tile((1, 0))
    tile2.show()