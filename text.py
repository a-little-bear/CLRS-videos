from pygame.sprite import Sprite
from pygame.font import Font
from pygame.transform import scale as change_scale


class Text(Sprite):
    def __init__(self, message : str, center : tuple[int,int], font_name, color, ratio, size = 30, /) -> None:
        """The init method of the class Text

        Args:
            message (str): The message of the text
            center (tuple[int,int]): The center of the text
            font_name (_type_): The name of the font of the text
            color (_type_): The color of the text
            ratio (_type_): The ratio of the text
            size (int, optional): The size of the text. Defaults to 30.
        """
        size = int(size)
        
        super().__init__()
        
        self.ratio = ratio
        self.size = size
        self.normal_size = self.size
        self.color = color
        
        self.font_name = font_name
        self.font = Font("fonts/"+font_name+".ttf", self.size)
        self.text = message
        self.image = self.font.render(self.text, 1, self.color)
        self.image = change_scale(self.image, self.ratio)
        
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.x -= 60 * ratio[0]
        self.rect.y -= 30 * ratio[1]
        self.topleft = self.rect.topleft
        
        self.scale = 100
        self.scale_to = 100
        self.decrease_scale = False
        
    def set_text(self, message : str):
        """Change the text.

        Args:
            message (str): The message replacing the original one.
        """        
        self.text = message
    
    def set_color(self, color : tuple) -> None:
        """Set the color of the text

        Args:
            color (tuple): The rgb tuple of the new color
        """
        self.color = color
    
    def get_text(self):
        """Get the message of the text"""
        return self.text
    
    def press(self, scale_to : int) -> None:
        """Press the text as a button

        Args:
            scale_to (int): The scale value which the text is going to reach, original at 100
        """
        self.scale_to = scale_to
        self.decrease_scale = True
        
    def update(self):
        """The update method of the class Text."""        
        
        
        if self.scale == self.scale_to and not self.scale == 100:
            self.decrease_scale = False
            self.scale_to = 100
        elif self.scale > self.scale_to and self.decrease_scale:
            self.scale -= 5
            self.size = self.normal_size * self.scale / 100
        elif not self.scale == 100 and not self.decrease_scale:
            self.scale += 5
            self.size = self.normal_size * self.scale / 100
        
        self.font = Font("fonts/"+self.font_name+".ttf", int(self.size))
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
