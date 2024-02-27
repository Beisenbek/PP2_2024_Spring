from colorama import Fore, Back, Style
import os 

path = os.getcwd() 
activeItemIndex = 1
currentItemIndex = 0

with os.scandir(path) as it:
    for entry in it:
        if(entry.is_dir()):
            if activeItemIndex == currentItemIndex:
                print(Back.GREEN + entry.name, end = '')
            else:
                print(Back.BLACK + entry.name, end = '')
            currentItemIndex = currentItemIndex + 1
            print(Back.BLACK + '')

with os.scandir(path) as it:
    for entry in it:
        if(not entry.is_dir()):
            if activeItemIndex == currentItemIndex:
                print(Back.GREEN + entry.name, end = '')
            else:
                print(Back.BLACK + entry.name, end = '')
            currentItemIndex = currentItemIndex + 1
            print(Back.BLACK + '')

print(Style.RESET_ALL)