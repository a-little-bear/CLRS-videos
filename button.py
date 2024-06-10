from pygame.sprite import Sprite
from pygame.image import load as load_img
from pygame.transform import scale as change_scale
from pygame import Rect
from text import Text

class Button():
    class Button(Sprite):
        def __init__(self, pic_name : str, center : tuple, ratio : tuple) -> None:
            """The init method of the class Button

            Args:
                pic_name (str): The name of the picture of the button
                center (tuple): The center position of the button
                ratio (tuple): The ratio of the button to its original size
            """
            super().__init__()
            
            self.ratio = ratio
            self.pic_name = pic_name
            
            self.scale = 100
            self.scale_to = 100
            self.decrease_scale = False
            
            self.image = load_img("images/" + self.pic_name + ".png")
            #self.image.set_colorkey(color_key)
            self.image = change_scale(self.image, \
                (200*self.ratio[0], 100*self.ratio[1]))
            self.normal_image = self.image
            
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.width = self.rect.width
            self.height = self.rect.height
            
            self.pressed = False
            self.activated = False
        
        def get_rect(self) -> Rect:
            """This method gets the rect of the image of the object

            Returns:
                Rect: Returns the rect of the image of the object
            """
            return self.rect
        
        def press(self, scale_to : int) -> None:
            """This method changes the scale_to variable of the object, which changes the image of the button

            Args:
                scale_to (int): The scale which the button is going to reach, original scale is 100
            """
            self.pressed = True
            self.scale_to = scale_to
            self.decrease_scale = True
        
        def update(self):
            """The update function of Sprite's sub class Button"""
            if self.scale == self.scale_to and not self.scale == 100:
                self.decrease_scale = False
                self.scale_to = 100
            elif self.scale > self.scale_to and self.decrease_scale:
                self.scale -= 5
                self.image = change_scale(self.normal_image, \
                    (self.width*self.scale/100, self.height*self.scale/100))
            elif not self.scale == 100 and not self.decrease_scale:
                self.scale += 5
                self.image = change_scale(self.normal_image, \
                    (self.width*self.scale/100, self.height*self.scale/100))
            elif self.pressed:
                self.activated = True
                self.pressed = False
                
    @staticmethod
    def run_code_if_button_pressed(start = 0, stop = 1, step = 2, sprites = None, \
                                    scale = 80, pos = (0,0), code = "", ret_spr = False, *args, **kwargs) -> list[bool, Sprite, int]:
        """This static method check does the pressed position has sprite

        Args:
            start (int, optional): The start index of the sprites list. Defaults to 0.
            stop (int, optional): The stop index of the sprites list. Defaults to 1.
            step (int, optional): The step value of the sprites list. Defaults to 2.
            sprites (list, optional): The sprites list. Defaults to None.
            pos (tuple, optional): The position of the mouse when pressed. Defaults to (0,0).
            code (str, optional): Lines of codes which is going to be executed after a sprite is clicked. 
                                    All lines are seperated. Defaults to "".
            ret_spr (bool, optional): Directly return the sprite, True when returning. Defaults to False.

        Returns:
            list[bool, Sprite, int]: first value is a bool type value which tells is their a sprite pressed, 
                                    second value is the sprite which is being pressed (only one),
                                    third / last value is the position of this sprite in the sprites list.
        """
        
        if sprites is None:
            return False
        
        code = code.splitlines()
        
        for i in range(start, stop, step):
            button = sprites.sprites()[i]
            #If this botton contains text
            if step == 2:
                font = sprites.sprites()[i+1]
            if pos[0] > button.rect.left and \
                pos[0] < button.rect.right and \
                pos[1] > button.rect.top and \
                pos[1] < button.rect.bottom:
                    button.press(scale)
                    if ret_spr:
                        return [True, button, i]
                    #If this botton contains text
                    if step == 2:
                        font.press(scale)
                    for j in range(0, len(code)):
                        for key in kwargs.keys():
                            address = ". [ (".split()
                            for adr in address:
                                if key+adr in code[j]:
                                    code[j] = code[j].replace(key+adr, f"kwargs.get(\"{key}\"){adr}")
                        eval(code[j])
                    return [True, None, i]
        return [False, None, -1]
            
    @staticmethod
    def get_sprites_list(pic_name : str, center_pic : tuple, ratio : tuple, text = None, center_text = (0,0), font = None, font_color = (0,0,0), font_size = 30, /) -> list[Button, Text]:
        """his static method gets the picture and the text of the button

        Args:
            pic_name (str): The name of the picture of the button
            center_pic (tuple): The center position of the picutre
            ratio (tuple): The ratio of the button
            text (str, optional): The message of the text part, default with no text. Defaults to None.
            center_text (tuple, optional): The center position of the text. Defaults to (0,0).
            font (str, optional): The font name of the text. Defaults to None.
            font_color (tuple, optional): The color of the text in rgb tuple. Defaults to (0,0,0).
            font_size (int, optional): The size of the text. Defaults to 30.

        Returns:
            list[Button.Button, Text]: Returns a list contains two objects, Button.Button and Text
        """
        if text is None:
            text = ""
        if font is None:
            font = "None"
        return [Button.Button(pic_name, center_pic, ratio), \
            Text(text, center_text, font, font_color, ratio, font_size)]
    
    @staticmethod
    def get_text_button(text : str, center : tuple, font : str, font_color : tuple, ratio : tuple, font_size : int, /) -> Text:
        """This static method returns the Text object which is clickable as a button

        Args:
            text (str): The message of the text
            center (tuple): The center of the text
            font (str): The font name of the text
            font_color (tuple): The color of the text
            ratio (tuple): The ratio of the text
            font_size (int): The size of the text

        Returns:
            Text: Returns a clickable text object
        """
        return Text(text, center, font, font_color, ratio, font_size)
    
    @staticmethod
    def get_picture_button(pic_name : str, center : tuple, ratio : tuple, /) -> Button:
        """This static method returns the Button.Button object which is clikable and only containing the picture

        Args:
            pic_name (str): The name of the picture
            center (tuple): The center position of the picture
            ratio (tuple): The ratio of the picture

        Returns:
            Button.Button: Returns the picture as a button
        """
        return Button.Button(pic_name, center, ratio)
    