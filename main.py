from turtle import back
import pygame as pg
import pygame_gui as pg_g
from lib.main_window import MainWindow

def add_buttons(window):
    # button_rect = pg.Rect((350, 275), (100, 50))
    # text = 'Say Hello'
    # function = lambda: print('Hello World!')
    # window.add_button(button_rect, text, function)

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

    while True:
        dt = clock.tick(fps) / 1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            window.handle_gui_event(event)
                    
        window.manager.update(dt)
        if background.get_size() != window.screen.get_size():
            background = pg.Surface(window.screen.get_size())
            background.fill(pg.Color(bg_color))

        window.screen.blit(background, (0, 0))
        window.manager.draw_ui(window.screen)
        window.draw_lines()
        window.draw_test_tiles()
        
        pg.display.flip()

if __name__ == "__main__":
    main()