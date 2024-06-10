from pygame.sprite import Sprite
from pygame.image import load as load_img
from pygame.transform import scale as change_scale

from setting import Setting

class Background(Sprite):
    
    def __init__(self, image_name : str, size : tuple, setting : Setting, address = ".png", position = None, index = -1, scale_to = None) -> None:
        """The init method of class Background

        Args:
            image_name (str): The name (excluding the address and the path) of the background
            size (tuple): The size of the background, which is the size of the screen
            address (str, optional): The address of the background. Defaults to ".png"
        """
        self.default_position = (setting["screen_size"][0]//2, setting["screen_size"][1]//2)
        
        if position is None:
            position = self.default_position
        elif not type(position[0]) is int or not type(position[1]) is int:
            position = (int(position[0]),int(position[1]))
        
        if scale_to is None:
            scale_to = setting["pressed_scale"]
        
        super().__init__()
        self.image_name = image_name
        self.size = size
        self.setting = setting
        self.address = address
        self.position = position
        self.index = index
        self.change_background(image_name, size, address)
        if index is -1:
            print("background initialized")
    
    def change_background(self, image_name : str, size : tuple, address = ".png") -> None:
        """This method changes the background image of the sprite

        Args:
            image_name (str): The name (excluding the address and the path) of the background
            size (tuple): The size of the background, which is the size of the screen
            address (str, optional): The address of the background. Defaults to ".png"
        """
        self.image = load_img("images/backgrounds/"+image_name+address)
        self.image = change_scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        if self.index is -1:
            print("background changed")
    
    def update(self):
        if self.position == self.default_position and self.image_name != self.setting["main_screen_bgi"]:
            self.change_background(self.setting["main_screen_bgi"], self.size, self.address)
            self.image_name = self.setting["main_screen_bgi"]
        elif self.position != self.default_position and self.image_name != self.setting["bgi_lst"][self.index]:
            self.change_background(self.setting["bgi_lst"][self.index], self.size, self.address)
            self.image_name = self.setting["bgi_lst"][self.index]
    
    def press(self, scale_to : int) -> None:
            """This method changes the scale_to variable of the object, which changes the image of the button

            Args:
                scale_to (int): The scale which the button is going to reach, original scale is 100
            """
            self.pressed = True
            self.scale_to = scale_to
            self.decrease_scale = True
    
    @staticmethod
    def run_code_if_button_pressed(start = 0, stop = 1, step = 2, sprites = None, \
                                    scale = 80, pos = (0,0), code = "", ret_spr = False, *args, **kwargs) -> list[bool, Sprite, int]:
        """This static method checks does the pressed position have sprite

        Args:
            start (int, optional): The start index of the sprites list. Defaults to 0.
            stop (int, optional): The stop index of the sprites list. Defaults to 1.
            step (int, optional): The step value of the sprites list. Defaults to 2.
            sprites (list, optional): The sprites list. Defaults to None.
            pos (tuple, optional): The position of the mouse when pressed. Defaults to (0,0).
            code (str, optional): Lines of codes which are going to be executed after a sprite is clicked. 
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