import pygame as pg
import PIL

class Tile(pg.sprite.Sprite):
    def __init__(self, size, pos, tex):
        super().__init__()
        self.pos = pos
        self.base_pos = pos
        self.size = size
        self.tex = tex
        self.set_texture(tex)
        self.darkened = False
    
    def set_texture(self, new_tex):
        if isinstance(new_tex, str):
            self.tex = new_tex
            self.base_image = pg.image.load(new_tex).convert_alpha()
        elif isinstance(new_tex, pg.Surface):
            self.base_image = new_tex.convert_alpha()
        else:
            print(type(new_tex))

        if self.size != self.base_image.get_size():
            self.image = pg.Surface(self.size).convert_alpha()
            pg.transform.scale(self.base_image, self.size, self.image)
        else:
            self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def set_pos(self, new_pos):
        self.pos = new_pos
        self.rect.topleft = new_pos

    def darken(self):
        if not self.darkened:
            self.dark = pg.Surface(self.size).convert_alpha()
            self.dark.fill((0, 0, 0, 25))
            self.old_image = self.image.copy()
            self.image.blit(self.dark, (0, 0))
            self.darkened = True

    def brighten(self): # need to tweak
        try:
            self.image = self.old_image
            self.darkened = False
        except AttributeError:
            pass
