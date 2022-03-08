import pygame as pg
import PIL

class Tile(pg.sprite.Sprite):
    def __init__(self, size, pos, tex):
        super().__init__()
        self.pos = pos
        self.size = size
        self.tex = tex
        self.set_texture(tex)
    
    def set_texture(self, new_tex):
        self.tex = new_tex
        self.image = pg.image.load(new_tex).convert_alpha()
        pg.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def set_pos(self, new_pos):
        self.pos = new_pos
        self.rect.topleft = new_pos