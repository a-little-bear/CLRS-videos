import ast

class Colors():
    
    # returns black as an undefined color
    UNDEFINED_RGB_TUPLE = (0, 0, 0) 
    
    def __init__(self) -> None:
        """The init method of the class Colors, read colors from the color dat file"""
        self.read_colors()

    def read_colors(self) -> None:
        """read colors from data/colors.dat and stores to the variable colors"""
        try:
            with open("data/colors.dat", "r") as inp:
                self.colors = ast.literal_eval(inp.read())
        except Exception as e:
            print(e)
        finally:
            print("finish reading colors")
    
    def get_RGB_tuple(self, name: str) -> tuple:
        """Get the RGB tuple using the name of the color

        Args:
            name (str): The name of the color

        Returns:
            tuple: The RGB tuple of the corresponding color
        """
        name = name.strip().title()
        if name in self.colors:
            return self.colors.get(name)
        else:
            return Colors.UNDEFINED_RGB_TUPLE
    
    def add_color(self, name : str, rgb_tuple : tuple) -> None:
        """Add a new color to the color dictionary

        Args:
            name (str): The name of the color
            rgb_tuple (tuple): The rgb tuple of the color
        """
        self.colors.update(name, rgb_tuple)

            
        

