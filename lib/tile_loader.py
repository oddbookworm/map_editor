from asyncore import read
from PIL import Image
import os
import pygame
import numpy
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

    def get_ss_dims(self):
        size = self.spritesheet.size
        width = size[0] // self.tile_size
        height = size[1] // self.tile_size
        return (width, height)

    # def load_pygame(self, tile):
    #     data = numpy.asarray(tile)
    #     return pygame.surfarray.make_surface(data[:][:])

    def load_pygame(self, tile):
        is_transparent = False

        extrema = tile.getextrema()
        max_red = extrema[0][1]
        max_green = extrema[1][1]
        max_blue = extrema[2][1]

        if max_red == max_green == max_blue == 0:
            is_transparent = True

        if not is_transparent:
            data = tile.tobytes()
            return pygame.image.fromstring(data, tile.size, tile.mode)
        else:
            return None

if __name__ == "__main__":
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    reader = SpriteSheetReader(''.join([parent_dir, "\\assets\\RPG Nature Tileset.png"]),
                                32)

    print(reader.get_ss_dims())

    tile_size = 128

    top = reader.get_tile((19, 8))
    bottom = reader.get_tile((0, 1))

    pygame.init()
    screen = pygame.display.set_mode((512, 512))

    top = reader.load_pygame(top)
    bottom = reader.load_pygame(bottom)
    tree_top = Tile((tile_size, tile_size), (tile_size, tile_size), top)
    tree_bottom = Tile((tile_size, tile_size), (tile_size, 2 * tile_size), bottom)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 0, 0, 0))
        screen.blit(tree_top.image, tree_top.rect)
        screen.blit(tree_bottom.image, tree_bottom.rect)
        pygame.display.flip()


    