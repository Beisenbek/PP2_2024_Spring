from colorama import Fore, Back, Style
import os 

path = os.getcwd() 
#path = "../week3"

with os.scandir(path) as it:
    for entry in it:
        if(entry.is_dir()):
            print(Fore.WHITE + entry.name)

with os.scandir(path) as it:
    for entry in it:
        if(not entry.is_dir()):
            print(Fore.YELLOW + entry.name)

print(Style.RESET_ALL)