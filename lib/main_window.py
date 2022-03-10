import pygame as pg
import pygame_gui as pg_g
import pygame_menu as pg_m
from os import path
try:
    from tile import Tile
    from tile_loader import SpriteSheetReader
except ModuleNotFoundError:
    from .tile import Tile
    from .tile_loader import SpriteSheetReader

class MainWindow:
    def __init__(self, size):
        self.screen = pg.display.set_mode(size, pg.RESIZABLE)
        self.tile_select_width = 116
        
        self.manager = pg_g.UIManager(size)

        self.buttons = {}

    def add_button(self, relative_rect, text, function = lambda: None):
        button = pg_g.elements.UIButton(relative_rect = relative_rect,
                                        text = text, manager = self.manager,
                                        tool_tip_text = text)
        self.buttons.update({button: function})

    def handle_gui_event(self, event):
        if event.type == pg_g.UI_BUTTON_PRESSED:
            self.buttons[event.ui_element]()
        
        self.manager.process_events(event)

    def draw_lines(self):
        white = pg.Color(255, 255, 255)
        line_1 = [(self.tile_select_width, 0), 
                    (self.tile_select_width, self.screen.get_size()[1])]
        pg.draw.line(self.screen, white, line_1[0], line_1[1])

    def draw_tiles(self):
        tiles = []
        size = 32
        gap = 5

        width, height = (size * 3 + gap * 4, size * 10 + gap * 11)
        self.tile_surf = pg.Surface((width, height))
        for tile in tiles:
            self.tile_surf.blit(tile.image, tile.rect)

    def draw_test_tiles(self):
        tiles = []
        size = 32
        gap = 5
        for i in range(0, 3):
            for j in range(0, 10):
                tile = pg.Surface((size, size))
                tile.fill(pg.Color('#FFFFFF'))
                tile_rect = tile.get_rect()
                x = gap + i * (size + gap)
                y = gap + j * (size + gap)
                tile_rect.topleft = (x, y)
                tiles.append((tile, tile_rect))

        for tile in tiles:
            self.screen.blit(tile[0], tile[1])

    def test_menu(self):
        self.menu = pg_m.Menu("Test", 400, 300)
        self.menu.add.text_input('Name : ', default = 'Player')
        self.menu.add.selector('Difficulty : ', [('Hard', 1), ('Easy', 2)])
        self.menu.add.button('Play', lambda : print('test'))
        self.menu.add.button('Quit', pg_m.events.EXIT)

    def load_tiles(self, tileset, og_size, tile_size):
        gap = 5
        
        parent_dir = path.abspath(path.join(path.dirname(__file__), ".."))
        reader = SpriteSheetReader(''.join([parent_dir, tileset]), og_size)
        width, height = reader.get_ss_dims()

        cols = 3
        if width * height % 3:
            rows = (width * height) % 3
        else:
            rows = ((width * height) // 3) + 1
        
        width, height = (tile_size * cols + gap * (cols + 1),
                        tile_size * rows + gap * (rows + 1))
        self.tile_surf = pg.Surface((width, height))
        self.tile_surf_rect = self.tile_surf.get_rect()
        self.tile_surf_rect.topleft = (0, 0)

        size = (tile_size, tile_size)
        self.tiles = []

        i = 0
        for row in range(height):
            for col in range(width):
                tile = reader.get_tile((col, row))
                tile = reader.load_pygame(tile)
                if tile is not None:
                    col_drawn = i % 3
                    row_drawn = (i - i % 3) // 3
                    x = col_drawn * tile_size + (col_drawn + 1) * gap
                    y = row_drawn * tile_size + (row_drawn + 1) * gap
                    pos = (x, y)
                    new_tile = Tile(size, pos, tile)
                    self.tiles.append(new_tile)
                    i += 1

    def draw_tiles(self):
        self.tile_surf.fill((0, 0, 0, 0))
        for tile in self.tiles:
            self.tile_surf.blit(tile.image, tile.rect)
        self.screen.blit(self.tile_surf, self.tile_surf_rect)