"""
Author: Joseph Siu
  
Date: Jun. 15, 2022
  
Description: This program is a tutorial based on the book "Introduction to Algorithms (3rd & 4th edition)" 
             Mathematical Background chapter is also based on Khan Academy's lessons
             And visual animations are made based on the lib "manim (community version)" by 3b1b

Need to install copy and cv2 libs to run the program, also need manim lib to run the manim codes
"""



#import pygame, which is the structure of the window
import pygame as pg

#import cv2, which allows the program to display video on the screen, but does not support audio
import cv2

#import random for background random and welcome print
from random import sample, randint as rand

#import and inisialize setting and color objects
from setting import Setting
setting = ...
from colors import Colors
colors = ...

#import classes from same folder's .py files
from stack import Stack
from button import Button
from background import Background
from text import Text
from cursor import Cursor

#deepcopy for cv2
from copy import deepcopy


def get_main_screen_sprites() -> list[Button]:
    """
    This function returns the main screen sprites list

    Args:
        setting (Setting): The setting object of class Setting
        colors (Colors): The colors object of class Colors

    Returns:
        list[Button]: A list which contains only Button objects
    """ 
    
    main_screen_sprites = []
    main_screen_sprites_texts = ["Lessons", "Setting", "About", "Exit"]
    
    for i in range (4):
        main_screen_sprites.append(Button.get_sprites_list("orange_rectangle_button", \
                ((1366/8)*(2*i+1)*setting.get_screen_ratio()[0], \
                (768/6*5)*setting.get_screen_ratio()[1]), \
                setting.get_screen_ratio(), main_screen_sprites_texts[i], \
                ((1366/8)*(2*i+1)*setting.get_screen_ratio()[0], \
                (768/6*5)*setting.get_screen_ratio()[1]), \
                setting["font"], colors.get_RGB_tuple("black"), 50 * setting.get_screen_ratio()[0]))
        
    return main_screen_sprites


def setting_screen_sprites_texts_setup():
    for i in range(6, 12):
        setting_screen_sprites_texts[i] = setting["bgi_lst"][i-6]

setting_screen_sprites_texts = [
    "Screen",
    "Background",
    "Font",
    
    "800x650",
    "1366x768",
    "1600x900",
    
    "","","","","","",
    
    "DancingScript",
    "Caveat",
    "ShadowsIntoLight",
    "DancingScript-VariableFont_wght",
    "Caveat-VariableFont_wght",
    "ShadowsIntoLight-Regular",
    
    "random",
    "reset",
    "return",
]

def get_setting_screen_sprites() -> list[Text, Button]:
    """
    This function returns the setting screen sprites list

    Args:
        setting (Setting): The setting object of class Setting
        colors (Colors): The colors object of class Colors

    Returns:
        list[Button]: A list which contains Text and Button objects
    """
    setting_screen_sprites = []
    setting_screen_sprites_positions = [
        (100 * setting.get_screen_ratio()[0], (768-160)/5 * setting.get_screen_ratio()[1]),
        (100 * setting.get_screen_ratio()[0], (768-160)/5*2 * setting.get_screen_ratio()[1]),
        (100 * setting.get_screen_ratio()[0], (768-160)/5*4 * setting.get_screen_ratio()[1]),
        
        (400 * setting.get_screen_ratio()[0], (768-160)/5 * setting.get_screen_ratio()[1]),
        (700 * setting.get_screen_ratio()[0], (768-160)/5 * setting.get_screen_ratio()[1]),
        (1000 * setting.get_screen_ratio()[0], (768-160)/5 * setting.get_screen_ratio()[1]),
        
        (500 * setting.get_screen_ratio()[0], (768-160)/5*2 * setting.get_screen_ratio()[1]),
        (800 * setting.get_screen_ratio()[0], (768-160)/5*2 * setting.get_screen_ratio()[1]),
        (1100 * setting.get_screen_ratio()[0], (768-160)/5*2 * setting.get_screen_ratio()[1]),
        (500 * setting.get_screen_ratio()[0], (768-160)/5*3 * setting.get_screen_ratio()[1]),
        (800 * setting.get_screen_ratio()[0], (768-160)/5*3 * setting.get_screen_ratio()[1]),
        (1100 * setting.get_screen_ratio()[0], (768-160)/5*3 * setting.get_screen_ratio()[1]),
        
        (400 * setting.get_screen_ratio()[0], (768-160)/5*4 * setting.get_screen_ratio()[1]),
        (750 * setting.get_screen_ratio()[0], (768-160)/5*4 * setting.get_screen_ratio()[1]),
        (1000 * setting.get_screen_ratio()[0], (768-160)/5*4 * setting.get_screen_ratio()[1]),
        (),(),(),
        
        (950 * setting.get_screen_ratio()[0], (768+80)/5*4 * setting.get_screen_ratio()[1]),
        (1150 * setting.get_screen_ratio()[0], (768+80)/5*4 * setting.get_screen_ratio()[1]),
        (1275 * setting.get_screen_ratio()[0], (768+80)/5*4 * setting.get_screen_ratio()[1]),
    ]
    
    
    
    for i in range(3):
        setting_screen_sprites.append(\
            Text(setting_screen_sprites_texts[i], 
                setting_screen_sprites_positions[i], 
                setting["font"], colors.get_RGB_tuple("green"), 
                setting.get_screen_ratio(), 80 * setting.get_screen_ratio()[0]))
        
    for i in range(3,6):
        setting_screen_sprites.append(\
            Button.get_text_button(setting_screen_sprites_texts[i], 
                setting_screen_sprites_positions[i], setting["font"], 
                colors.get_RGB_tuple("green"), setting.get_screen_ratio(), 60 * setting.get_screen_ratio()[0]))
        if str(setting["screen_size"][0])+"x"+str(setting["screen_size"][1]) == setting_screen_sprites[i].get_text():
            setting_screen_sprites[i].set_color(colors.get_RGB_tuple("cyan"))
        
    for i in range(6, 12):
        setting_screen_sprites.append(
            Background(setting_screen_sprites_texts[i], 
                        (200*setting.get_screen_ratio()[0], 100*setting.get_screen_ratio()[1]),
                        setting=setting, 
                        position=(setting_screen_sprites_positions[i][0],
                                  setting_screen_sprites_positions[i][1]),
                        index=i-6))
        
    for i in range(12, 15):
        setting_screen_sprites.append(
            Button.get_text_button(setting_screen_sprites_texts[i], 
                setting_screen_sprites_positions[i], setting_screen_sprites_texts[i+3], 
                colors.get_RGB_tuple("green"), setting.get_screen_ratio(), 60 * setting.get_screen_ratio()[0]))
        if setting["font"] == setting_screen_sprites_texts[i+3]:
            setting_screen_sprites[i].set_color(colors.get_RGB_tuple("cyan"))
            
    setting_screen_sprites.append(
        Button.get_picture_button(setting_screen_sprites_texts[18], 
            setting_screen_sprites_positions[18], (setting.get_screen_ratio()[0],setting.get_screen_ratio()[1])))
    
    for i in range(19, 21):
        setting_screen_sprites.append(
            Button.get_picture_button(setting_screen_sprites_texts[i], 
                setting_screen_sprites_positions[i], (setting.get_screen_ratio()[0]*0.5,setting.get_screen_ratio()[1])))
        
        
        
    return setting_screen_sprites



def get_about_screen_sprites() -> list[Button, Text]:
    """
    This function returns the about screen sprites list

    Args:
        setting (Setting): The setting object of class Setting
        colors (Colors): The colors object of class Colors

    Returns:
        list[Button]: A list which contains Text and Button objects
    """
    about_screen_sprites_texts = """
About    
This program's tutorials are based on the book
"Introduction to Algorithms (3rd & 4th edition)" 

Mathematical Background chapter is also based on
Khan Academy's lessons

And visual animations are made based on the lib
"manim (community version)" by 3b1b

Press Exit to return to the previous window
Press Space to pause or start the video
Use Left and Right arrows to change the video time

Joseph Siu""".splitlines()
    
    about_screen_sprites = []
    
    about_screen_sprites.append(Button.get_picture_button("yellow_lined_paper", \
                                (setting["screen_size"][0]/2, setting["screen_size"][1]/2), \
                                (3.5 * setting.get_screen_ratio()[0], 7.5 * setting.get_screen_ratio()[1])))
    for i in range(len(about_screen_sprites_texts)): 
        about_screen_sprites.append(Text(about_screen_sprites_texts[i], (about_screen_sprites[0].get_rect().left + 150 * setting.get_screen_ratio()[0], 
                                        (i+1)*35*setting.get_screen_ratio()[1]), \
                                        setting["font"], colors.get_RGB_tuple("black"), setting.get_screen_ratio(), 30*setting.get_screen_ratio()[0]))
    about_screen_sprites.append(Button.get_picture_button("return", (1275 * setting.get_screen_ratio()[0], (768+80)/5*4 * setting.get_screen_ratio()[1]), \
                                (setting.get_screen_ratio()[0]*0.5,setting.get_screen_ratio()[1])))
    
    return about_screen_sprites



lessons_screen_sprites_texts = []

def get_lessons_screen_sprites() -> list[Button]:
    """
    This function returns the about screen sprites list

    Args:
        setting (Setting): The setting object of class Setting
        colors (Colors): The colors object of class Colors

    Returns:
        list[Button]: A list which contains only Button objects
    """
    for i in range(1, 9):
        lessons_screen_sprites_texts.append(setting["lesson_"+str(i)])
    lessons_screen_sprites_texts.append("Return")
    
    
    
    lessons_screen_sprites = []
    lessons_screen_sprites_positions = [
        ((1366/4) * setting.get_screen_ratio()[0], (768-160)/5 * setting.get_screen_ratio()[1]),
        ((1366/4) * setting.get_screen_ratio()[0], (768-160)/5*2 * setting.get_screen_ratio()[1]),
        ((1366/4) * setting.get_screen_ratio()[0], (768-160)/5*3 * setting.get_screen_ratio()[1]),
        ((1366/4) * setting.get_screen_ratio()[0], (768-160)/5*4 * setting.get_screen_ratio()[1]),
        
        ((1366/4*3) * setting.get_screen_ratio()[0], (768-160)/5 * setting.get_screen_ratio()[1]),
        ((1366/4*3) * setting.get_screen_ratio()[0], (768-160)/5*2 * setting.get_screen_ratio()[1]),
        ((1366/4*3) * setting.get_screen_ratio()[0], (768-160)/5*3 * setting.get_screen_ratio()[1]),
        ((1366/4*3) * setting.get_screen_ratio()[0], (768-160)/5*4 * setting.get_screen_ratio()[1]),
        
        (1275 * setting.get_screen_ratio()[0], (768+80)/5*4 * setting.get_screen_ratio()[1]),
    ]
    
    
    
    for i in range (8):
        lessons_screen_sprites.append(Button.get_sprites_list("orange_rectangle_button", \
                lessons_screen_sprites_positions[i], \
                (setting.get_screen_ratio()[0]*2.5,setting.get_screen_ratio()[1]), lessons_screen_sprites_texts[i], \
                (lessons_screen_sprites_positions[i][0]-63*setting.get_screen_ratio()[0], \
                lessons_screen_sprites_positions[i][1]+15*setting.get_screen_ratio()[0]), \
                setting["font"], colors.get_RGB_tuple("black"), 28 * setting.get_screen_ratio()[0]))
    lessons_screen_sprites.append(Button.get_picture_button(lessons_screen_sprites_texts[8], \
            lessons_screen_sprites_positions[8], (setting.get_screen_ratio()[0]*0.5,setting.get_screen_ratio()[1])))
    
    
    
    return lessons_screen_sprites



def get_lesson_screen_sprites(lesson_num : int) -> list[Button]:
    """
    This function returns the specific lesson screen sprites list

    Args:
        setting (Setting): The setting object of class Setting
        colors (Colors): The colors object of class Colors
        lesson_num (int): The chapter number

    Returns:
        list[Button]: A list which contains only Button objects
    """
    lesson_screen_sprites = []
    lesson_screen_sprites_positions = [
        (325*setting.get_screen_ratio()[0]+setting["screen_size"][0]/2, setting["screen_size"][1]/2),
    ]
    
    
    
    sub_lesson_num = len(setting["lesson_"+str(lesson_num)+"_"])
    for i in range(1, sub_lesson_num+1):
        lesson_screen_sprites_positions.append((335 * setting.get_screen_ratio()[0], (50*i+(768-50*sub_lesson_num)/(sub_lesson_num+1)*i-30) * setting.get_screen_ratio()[1]))
    lesson_screen_sprites_positions.append((1275 * setting.get_screen_ratio()[0], (768+80)/5*4 * setting.get_screen_ratio()[1]))
    
    
    
    lesson_screen_sprites.append(Button.get_picture_button("yellow_lined_paper", \
                                lesson_screen_sprites_positions[0], \
                                (3.5 * setting.get_screen_ratio()[0], 7.5 * setting.get_screen_ratio()[1])))
    
    for i in range(1, sub_lesson_num+1):
        lesson_screen_sprites.append(Button.get_sprites_list(
                                        "orange_rectangle_button", \
                                        lesson_screen_sprites_positions[i], \
                                        (3*setting.get_screen_ratio()[0], \
                                            ((768-35*(sub_lesson_num-2))/(sub_lesson_num+4))/55*setting.get_screen_ratio()[1]), \
                                        setting["lesson_"+str(lesson_num)+"_"][i], \
                                        (lesson_screen_sprites_positions[i][0]-100*setting.get_screen_ratio()[0],lesson_screen_sprites_positions[i][1]), \
                                        setting["font"], colors.get_RGB_tuple("black"), 30*setting.get_screen_ratio()[0]))
        
    lesson_screen_sprites.append(Button.get_picture_button("return", lesson_screen_sprites_positions[-1], \
                                (setting.get_screen_ratio()[0]*0.5,setting.get_screen_ratio()[1])))
    
    
    
    return lesson_screen_sprites 





def set_next_window(*args, **kwargs):
    """
    This function sets next window to previous window
    
    Args:
        setting= (Setting): The setting object of class Setting
        windows= (Stack): The windows stack of the program
    """
    current = kwargs.get("windows").pop()
    kwargs.get("setting").set("next_window", kwargs.get("windows").top())
    kwargs.get("windows").push(current)



def restart():
    main()
    raise SystemExit



def main():
    
    print('''
            ___________________________________________________
            
            
            Starting the program "Introduction to Algorithms"

            This program's tutorials are based on the book
            "Introduction to Algorithms (3rd & 4th edition)" 
            
            Mathematical Background chapter is also based on
            Khan Academy's lessons

            And visual animations are made based on the lib
            "manim (community version)" by 3b1b

                                                    Joseph Siu
            ___________________________________________________
''')
    
    def hi():
        print("")
        print("Hello, User_"+str(rand(1, 99999999999)))
        print("")
    
    hi()
        
    
    #inisializing all modules, classes, and objects
    pg.init()
    pg.mouse.set_visible(False)
    global setting, colors
    setting = Setting()
    setting_screen_sprites_texts_setup()
    colors = Colors() 
    
    '''TODO: delete after tested'''
    #setting.to_default()
    #setting.read_setting()
    fps = 60
    
    

    #The entire frame of pygame
    frame = pg.display.set_mode(setting["screen_size"])
    pg.display.set_caption(setting["title"])
    pg.display.set_icon(pg.image.load("images/" + setting["icon"] + ".png"))
    #The main screen of pygame
    main_screen = pg.Surface(setting["screen_size"])
    #The stack of windows
    windows = Stack()
    #sprites list
    sprites = pg.sprite.OrderedUpdates()
    
    sprites_cursor = pg.sprite.OrderedUpdates()
    cursor = Cursor(pg=pg)
    sprites_cursor.add(cursor)
    
    
    #sprites lists of all windows
    background_sprite = Background(setting["main_screen_bgi"], setting["screen_size"], 
                                   setting, position=(setting["screen_size"][0]//2, setting["screen_size"][1]//2))
    main_screen_sprites = get_main_screen_sprites()
    setting_screen_sprites = get_setting_screen_sprites()
    about_screen_sprites = get_about_screen_sprites()
    lessons_screen_sprites = get_lessons_screen_sprites()
    lesson_screen_sprites_lst = []
    for i in range(1, setting["lesson_number"]+1):
        lesson_screen_sprites_lst.append(get_lesson_screen_sprites(i))
    
    
    
    #video properties
    vid, vid_size, vid_img_lst, vid_img_index, vid_move_fwd, vid_move_bwd = None, None, [], 0, 0, 0
    
    
    
    #add background and main screen sprites to the sprites list
    sprites.add(background_sprite)
    print("background added to sprites list")
    sprites.add(main_screen_sprites)
    print("main screen buttons added to sprites list")
    #push "main_screen" to the windows stack
    windows.push("main_screen")
    
    
    
    #main screen to the frame
    frame.blit(main_screen, (0,0))
    #The clock (FPS) of pygame
    clock = pg.time.Clock()
    #False when exiting
    keep_going = True
    
    
    
    #The main loop of the pygame window
    while keep_going:
        #change the framerate (FPS) to 60 (videos are 15 FPS)
        clock.tick(fps)
        
        
        
        #getting events from the window
        for event in pg.event.get():
            #when clicked the exit botton at top right
            if event.type == pg.QUIT:
                #terminate the loop
                keep_going = False
            
            
            
            #when event is a key down (keyboard or mouse)
            elif event.type == pg.KEYDOWN:
                match(event.key):
                    case pg.K_ESCAPE:
                        #stop the program if pressed exit at the main screen
                        if windows.top() == "main_screen":
                            keep_going = False
                        #go back to the previous window
                        else:    
                            set_next_window(setting=setting, windows=windows)
                            setting["switch_window"] = True
                    
                    case pg.K_SPACE:
                        #switch the pause boolean value if space pressed
                        setting.set("pause", not setting["pause"])
                    
                    case pg.K_LEFT:
                        #move video index if left arrow pressed
                        if setting["play_vid"]:
                            vid_img_index -= fps
                            if vid_img_index < 0:
                                vid_img_index = 0
                            else:
                                vid_move_bwd = fps
                                vid_move_fwd = 0
                    
                    case pg.K_RIGHT:
                        #move video index if right arrow pressed
                        if setting["play_vid"]:
                            vid_img_index += fps
                            if vid_img_index >= len(vid_img_lst):
                                vid_img_index = len(vid_img_lst) - 1
                            else:
                                vid_move_fwd = fps
                                vid_move_bwd = 0
            
            
            
            #if left mouse button clicking
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                #check the top window
                match(windows.top()):
                    case "main_screen":
                        #if one of the main screen buttons is pressed 
                        Button.run_code_if_button_pressed(1, 9, 2, sprites, setting["pressed_scale"], pg.mouse.get_pos(), 
                                                       """cursor.set_pic("text.cur")
                                                          setting.set("next_window", font.get_text().lower())""", setting=setting, cursor=cursor)
                    
                    case "lessons":
                        #if one of the chapter buttons is pressed
                        Button.run_code_if_button_pressed(1, 17, 2, sprites, setting["pressed_scale"], pg.mouse.get_pos(),
                                                        """cursor.set_pic("text.cur")
                                                        setting.set("next_window", font.get_text().lower())""", setting=setting, cursor=cursor)
                        #if return button is pressed
                        if Button.run_code_if_button_pressed(17, 18, 1, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""", True)[0]:
                            cursor.set_pic("text.cur")
                            sprites.sprites()[17].press(setting["pressed_scale"])
                            set_next_window(windows=windows, setting=setting)
                    
                    case "setting":
                        #if one of the screen size buttons is pressed, restart window
                        pressed, button, _ = Button.run_code_if_button_pressed(4, 7, 1, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""", True)
                        if pressed and button.get_text() != str(setting["screen_size"][0])+"x"+str(setting["screen_size"][1]):
                            match(button.get_text()):
                                case "800x650":
                                    setting.set("screen_size", (800, 650))
                                case "1366x768":
                                    setting.set("screen_size", (1366, 768))
                                case "1600x900":
                                    setting.set("screen_size", (1600, 900))
                            print("window size set to " + button.get_text())
                            restart()
                        
                        #if one of the background image buttons is pressed, change background sprite
                        Background.run_code_if_button_pressed(7, 13, 1, sprites, setting["pressed_scale"], 
                                                        pg.mouse.get_pos(), 
                                                        """setting.set("main_screen_bgi", setting["bgi_lst"][i-7])
                                                            print("bacground image set to " + setting["bgi_lst"][i-7])""", 
                                                        False, setting=setting, setting_screen_sprites_texts=setting_screen_sprites_texts, cursor=cursor)
                            
                        #if one of the font buttons is pressed, restart window
                        pressed, _, index = Button.run_code_if_button_pressed(13, 16, 1, sprites, setting["pressed_scale"], 
                                                        pg.mouse.get_pos(), """""", True)
                        if pressed and setting["font"] != setting_screen_sprites_texts[index+2]:
                            setting["font"] = setting_screen_sprites_texts[index+2]
                            print("font is set to " + setting_screen_sprites_texts[index+2])
                            restart()
                        
                        #if random button is pressed, change 6 background pictures to random
                        if Button.run_code_if_button_pressed(16, 17, 1, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""")[0]:
                            cursor.set_pic("text.cur")
                            sprites.sprites()[16].press(setting["pressed_scale"])
                        
                        #if reset button is pressed, set settings to default, and restart window
                        if Button.run_code_if_button_pressed(17, 18, 1, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""")[0]:
                            cursor.set_pic("text.cur")
                            sprites.sprites()[17].press(setting["pressed_scale"])
                            
                        #go to the previous window if return button is pressed
                        if Button.run_code_if_button_pressed(18, 19, 1, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""")[0]:
                            cursor.set_pic("text.cur")
                            sprites.sprites()[18].press(setting["pressed_scale"])
                            set_next_window(windows=windows, setting=setting)
                    
                    case "about":
                        #return to main screen if return button is pressed
                        if Button.run_code_if_button_pressed(len(sprites.sprites())-1, len(sprites.sprites()), 1, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""")[0]:
                            cursor.set_pic("text.cur")
                            set_next_window(windows=windows, setting=setting)
                    
                    case _:
                        #windows.top() only up to chapter (lesson_(1~8))
                        valid = False
                        for i in range(1, 9):
                            #if current window is a lesson
                            if windows.top() == setting["lesson_"+str(i)].lower():
                                valid = True
                                #if a sub lesson button is pressed
                                pressed, _, j = Button.run_code_if_button_pressed(2, len(sprites.sprites())-1, 2, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""", True)
                                if pressed:
                                    cursor.set_pic("precision.cur")
                                    setting.set("next_window", "lesson_"+str(i)+"_"+str(j//2))
                                    
                                #if return button is pressed
                                if Button.run_code_if_button_pressed(len(sprites.sprites())-1, len(sprites.sprites()), 1, sprites, setting["pressed_scale"], pg.mouse.get_pos(), """""")[0]:
                                    cursor.set_pic("text.cur")
                                    set_next_window(windows=windows, setting=setting)
                        if not valid:
                            raise Exception("incorrect next_window case")
        
        
        
        
        
        match(windows.top()):
            #if currently at main screen
            case "main_screen":
                #if one of the buttons is finished pressing and switch_window == True, set global switch window to True
                for i in range(1, 9, 2):
                    button = sprites.sprites()[i]
                    if button.activated:
                        setting["switch_window"] = True
                        button.activated = False
        
                #if button is finished animating and ready to switch window
                if setting["switch_window"]:
                    cursor.set_pic("normal.cur")
                    print("switching window from " + windows.top() \
                        + " to " + setting["next_window"])
                    match(setting["next_window"]):
                        case "lessons":
                            sprites.remove(main_screen_sprites)
                            windows.push("lessons")
                            sprites.add(lessons_screen_sprites)
                        case "setting":
                            sprites.remove(main_screen_sprites)
                            windows.push("setting")
                            sprites.add(setting_screen_sprites)
                        case "about":
                            sprites.remove(main_screen_sprites)
                            windows.push("about")
                            sprites.add(about_screen_sprites)
                        case "exit":
                            keep_going = False
                        case _:
                            raise Exception("incorrect next_window case")
                    setting.set("switch_window", False)
            
            
            
            #if currently at setting window
            case "setting":
                #if random button pressed
                if sprites.sprites()[-3].activated:
                    cursor.set_pic("normal.cur")
                    setting.set("bgi_lst",  sample([str(i) for i in range(1, setting["bgi_num"]+1)], 6))
                    print("backgrounds randomized")
                    sprites.sprites()[-3].activated = False
                #if reset button pressed
                if sprites.sprites()[-2].activated:
                    cursor.set_pic("normal.cur")
                    setting.to_default()
                    print("setting set to default")
                    restart()
                #if return button finished pressing
                if sprites.sprites()[-1].activated:
                    cursor.set_pic("normal.cur")
                    sprites.sprites()[-1].activated = False
                    setting["switch_window"] = True
                
                #if ready to switch window
                if setting["switch_window"]:
                    match(setting["next_window"]):
                        case "main_screen":
                            windows.pop()
                            setting["next_window"] = windows.top()
                            sprites.remove(setting_screen_sprites)
                            sprites.add(main_screen_sprites)
                        case _:
                            raise Exception("incorrect next_window case")
                    
                    print("window switched to " + setting["next_window"])
                    setting.set("switch_window", False)
            
            
            
            #if currently at abouto screen
            case "about":
                #if return button finished pressing
                if sprites.sprites()[-1].activated:
                    sprites.sprites()[-1].activated = False
                    setting["switch_window"] = True
                
                #if ready to switch window
                if setting["switch_window"]:
                    cursor.set_pic("normal.cur")
                    if setting["next_window"] == "main_screen":
                        windows.pop()
                        setting["next_window"] = windows.top()
                        sprites.remove(about_screen_sprites)
                        sprites.add(main_screen_sprites)
                    
                    print("window switched to " + setting["next_window"])
                    setting.set("switch_window", False)
            
            
            
            #if currently at selecting lesson / chapter screen
            case "lessons":
                #if one of the chapter buttons finished pressing
                for i in range(1, 16, 2):
                    button = sprites.sprites()[i]
                    if button.activated:
                        setting["switch_window"] = True
                        button.activated = False
                
                #if return button finished pressing
                rtrn = sprites.sprites()[17]
                if rtrn.activated:
                    setting["switch_window"] = True
                    rtrn.activated = False
                
                #if ready to switch window
                if setting["switch_window"]:
                    cursor.set_pic("normal.cur")
                    match(setting["next_window"]):
                        case "main_screen":
                            windows.pop()
                            setting["next_window"] = windows.top()
                            sprites.remove(lessons_screen_sprites)
                            sprites.add(main_screen_sprites)
                        
                        case _:
                            switched = False
                            for i in range(1, 9):
                                #if switching to a chapter screen
                                if setting["next_window"] == setting["lesson_"+str(i)].lower():
                                    switched = True
                                    windows.push(setting["next_window"])
                                    sprites.remove(lessons_screen_sprites)
                                    sprites.add(lesson_screen_sprites_lst[i-1])
                            
                            if not switched:
                                raise Exception("incorrect next_window case")
                    
                    print("window switched to " + setting["next_window"])
                    setting.set("switch_window", False)
            
            
            
            case _:
                valid = False
                for i in range(1, 9):
                    #if current window is this chapter screen
                    if windows.top() == setting["lesson_"+str(i)].lower():
                        valid = True
                        #if one sub lesson button finished pressing
                        for j in range(2, len(sprites.sprites())-1, 2):
                            button = sprites.sprites()[j]
                            if button.activated:
                                setting["switch_window"] = True
                                button.activated = False
                        
                        #if return finished pressing
                        rtrn = sprites.sprites()[-1]
                        if rtrn.activated:
                            setting["switch_window"] = True
                            rtrn.activated = False
                        
                        #if ready to swtich window
                        if setting["switch_window"]:
                            cursor.set_pic("normal.cur")
                            match(setting["next_window"]):
                                case "lessons":
                                    windows.pop()
                                    setting["next_window"] = windows.top()
                                    sprites.remove(lesson_screen_sprites_lst)
                                    sprites.add(lessons_screen_sprites)
                                    setting["play_vid"] = False
                                    setting["pause"] = False
                                
                                case _:
                                    for j in range(1, 10):
                                        #if next window is this sub lesson
                                        if setting["next_window"] == "lesson_"+str(i)+"_"+str(j):
                                            try:
                                                #play the video of this sub lesson
                                                vid = cv2.VideoCapture("videos/"+str(i)+"_"+str(j)+".mp4")
                                                found, vid_img = vid.read()
                                                #if their is no video, play the default Video_not_found.mp4 video
                                                if not found:
                                                    vid = cv2.VideoCapture("videos/Video_not_found.mp4")
                                                    found, vid_img = vid.read()
                                                
                                                #sizes of all frames of the video
                                                vid_size = (
                                                    int(852/10*8*setting.get_screen_ratio()[0]), 
                                                    int(480/10*8*setting.get_screen_ratio()[1])
                                                )
                                                vid_img = cv2.resize(vid_img, vid_size) 
                                                
                                                #read the entire video first, takes a while
                                                vid_img_index = 0
                                                vid_img_lst = []
                                                while found:
                                                    vid_img = cv2.resize(vid_img, vid_size)
                                                    vid_img_lst.append(vid_img)
                                                    found, vid_img = vid.read()
                                                
                                                #start playing video
                                                setting["play_vid"] = True
                                                setting["pause"] = False
                                                
                                            
                                            except FileNotFoundError:
                                                print(f"Video not found: videos/{i}_{j}.mp4")
                                                raise SystemExit
                            
                            print("window switched to " + setting["next_window"])
                            setting.set("switch_window", False)
                        
                if not valid:
                    raise Exception("incorrect next_window case")
        
        
        
        
        sprites.clear(frame, main_screen)
        sprites.update()
        sprites.draw(frame)
        
        
        
        #if playing video
        if setting["play_vid"]:
            img = deepcopy(vid_img_lst[vid_img_index])
            
            #if not pausing
            if not setting["pause"]:
                vid_img_index += 1
                
                #if video finished playing, restart the video (change the index)
                if len(vid_img_lst) == vid_img_index:
                    vid_img_index = 0
                    setting.set("pause", True)
                    cv2.putText(img, "Paused", (int(50*setting.get_screen_ratio()[0]), int(50*setting.get_screen_ratio()[0])), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            #if pausing
            else:
                #put paused text
                cv2.putText(img, "Paused", (int(50*setting.get_screen_ratio()[0]), int(50*setting.get_screen_ratio()[0])), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            
            #if left or right arrow pressed, show the direction text
            if(vid_move_fwd != 0):
                vid_move_fwd -= 1
                cv2.putText(img, "-> 1 second", (int(300*setting.get_screen_ratio()[0]), int(50*setting.get_screen_ratio()[0])), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            elif(vid_move_bwd != 0):
                vid_move_bwd -= 1
                cv2.putText(img, "<- 1 second", (int(300*setting.get_screen_ratio()[0]), int(50*setting.get_screen_ratio()[0])), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
                
            frame.blit(pg.image.frombuffer(img.tobytes(), vid_size, "BGR"), \
                        (int((1366/2-16)*setting.get_screen_ratio()[0]), \
                        150*setting.get_screen_ratio()[1]))
            
            
        
        
        sprites_cursor.update()
        sprites_cursor.draw(frame)
        
        
        
        pg.display.flip()
    
    
    
    
    
    pg.quit()
    print("pygame deconstructed")
    
    
    
    #write settings to the file
    setting.write_setting()
    print("setting wrote to file")
                 
                 
                 
                    

#entrance of the program
if __name__ == "__main__":
    main()
    
    #TYFUMP!
    print("Thank you for using my program! - Joseph Siu")