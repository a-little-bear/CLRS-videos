import ast
from typing import Any

class Setting():

    setting = {}
    
    def __init__(self) -> None:
        """The init method of the class Setting"""
        self.read_setting()        
        print("settings initialized")
        self.set("switch_window", False)
        self.set("next_window", "main_screen")
        self.set("play_vid", False)
        self.set("pause", False)

    def read_setting(self) -> int:
        """This method read the setting from the setting.dat file,
            Returns 0 when error, 1 when success"""
        try:
            with open("data/setting.dat", "r") as inp:
                self.setting = ast.literal_eval(inp.read())
        except Exception as e:
            print(e)
            return 0
        finally:
            print("finish reading setting")
            return 1

    def write_setting(self) -> int:
        """This method write the setting to the setting.dat file,
            Return 0 whe error, 1 when success"""
        self.set("switch_window", False)
        self.set("next_window", "main_screen")
        try:
            with open("data/setting.dat", "w") as outp:
                outp.write(str(self.setting))
                outp.close()
        except Exception as e:
            print(e)
            return 0
        finally:
            print("finish writing setting")
            return 1
            
    
    def set(self, key : str, value : Any) -> int:
        """This method set the value of the key in setting dictionary

        Args:
            key (str): The name of the key
            value (Any): The value of the key

        Raises:
            Exception: raise Exception when key not found

        Returns:
            int: returns 0 when error occurs when writing settings to the file setting.dat
                 returns 1 after successly writing settings
        """
        if key in self.setting:
            self.setting[key] = value
            #self.write_setting()
        else:
            raise Exception("KeyNotFoundError")
        
        try:
            with open("data/setting.dat", "w") as outp:
                outp.write(str(self.setting))
                outp.close()
        except Exception as e:
            print(e)
            return 0
        finally:
            return 1
    
    def get(self, key : str) -> Any:
        """This method get the value by passing the key

        Args:
            key (str): The name of the key in setting dictionary

        Raises:
            Exception: Raise Exception("KeyNotFoundError") when key not found

        Returns:
            Any: The value of the key
        """
        if key in self.setting:
            return self.setting.get(key)
        else:
            raise Exception("KeyNotFoundError")
    
    def get_screen_ratio(self) -> tuple:
        """This method gets the ratio of the screen, base value is 1366x768"""
        return (self.setting["screen_size"][0] / 1366 , \
            self.setting["screen_size"][1] / 768)
    
    def to_default(self) -> None:
        """This method changes the setting file setting.dat to default file default_setting.dat"""
        try:
            with open("data/default_setting.dat", "r") as inp:
                with open("data/setting.dat", "w") as outp:
                    outp.write(inp.read())
        except Exception as e:
            print(e)
        finally:
            print("setting changed to default")
    
    def __getitem__(self, key):
        """overrided method, obj[key] same as obj.get(key)"""
        return self.get(key)
    
    def __setitem__(self, key, value):
        """overrided method, obj[key] = value same as obj.set(key)"""
        return self.set(key, value)
    
    def __dir__(self):
        """overrided method, obj[] returns the setting dictionary"""
        return self.setting