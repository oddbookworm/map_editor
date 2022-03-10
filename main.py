from turtle import back
import pygame as pg
import pygame_gui as pg_g
from lib.main_window import MainWindow

def add_buttons(window):
    # button_rect = pg.Rect((350, 275), (100, 50))
    # text = 'Say Hello'
    # function = lambda: print('Hello World!')
    # window.add_button(button_rect, text, function)

    # window.test_menu()
    # button_rect = pg.Rect((350, 275), (100, 50))
    # text = 'Open Menu'
    # function = lambda: window.menu.mainloop(window.screen)
    # window.add_button(button_rect, text, function)

    pass

def main():
    bg_color = '#000000'
    pg.init()

    pg.display.set_caption('Temp')
    size = (800, 600)
    fps = 60

    clock = pg.time.Clock()

    window = MainWindow(size)
    add_buttons(window)
    
    background = pg.Surface(size)
    background.fill(pg.Color(bg_color))

    window.load_tiles("\\assets\\RPG Nature Tileset.png", 32, 32)

    while True:
        dt = clock.tick(fps) / 1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            if event.type == pg.MOUSEWHEEL:
                if window.tile_surf_rect.collidepoint(pg.mouse.get_pos()):
                    pos = window.tile_surf_rect.topleft
                    new_pos = new_pos = (pos[0], pos[1] + event.y * 32)
                    if new_pos[1] > 0:
                        new_pos = (new_pos[0], 0)
                    if new_pos[1] + window.tile_surf_rect.height < size[1]:
                        new_y = -(window.tile_surf_rect.height - size[1])
                        new_pos = (new_pos[0], new_y)
                    window.tile_surf_rect.topleft = new_pos
                    for tile in window.tiles:
                        pos = tile.base_pos
                        tile.set_pos((pos[0], pos[1] + new_pos[1]))

            window.handle_gui_event(event)

        for tile in window.tiles:

            if tile.rect.collidepoint(pg.mouse.get_pos()):
                tile.darken()
            elif tile.darkened:
                tile.brighten()
                    
        window.manager.update(dt)
        if background.get_size() != window.screen.get_size():
            background = pg.Surface(window.screen.get_size())
            background.fill(pg.Color(bg_color))

        window.screen.blit(background, (0, 0))
        window.manager.draw_ui(window.screen)
        window.draw_lines()
        window.draw_tiles()
        
        pg.display.flip()

if __name__ == "__main__":
    main()