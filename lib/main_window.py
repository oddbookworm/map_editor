import pygame as pg
import pygame_gui as pg_g
import pygame_menu as pg_m

try:
    from tile import Tile
except ModuleNotFoundError:
    from .tile import Tile

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
