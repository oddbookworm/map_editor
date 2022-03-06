import pygame as pg
import pygame_gui as pg_g

class MainWindow:
    def __init__(self, size):
        self.screen = pg.display.set_mode(size)
        
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
