from pygame.sprite import Sprite
from pygame.image import load as load_img

class Cursor(Sprite):
    #init method of the class Cursor
    def __init__(self, pg, name = "normal.cur"):
        super().__init__()
        
        self.pg = pg
        self.name = name
        self.image = load_img("images/cursors/"+name)
        self.rect = self.image.get_rect()
    
    #The update method overriding Sprite super class
    def update(self):
        self.rect.center = self.pg.mouse.get_pos()
    
    #change cursor picture
    def set_pic(self, name):
        if self.name != name:
            self.name = name
            self.image = load_img("images/cursors/"+name)