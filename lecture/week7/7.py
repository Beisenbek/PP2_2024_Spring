from msvcrt import getch
from colorama import Fore, Back, Style
import os 


class Layer:
    def __init__(self, path):
        self.activeItemIndex = 0
        self.path = path
        self.entries = []
        self.fill_entries()

    def fill_entries(self):
        with os.scandir(self.path) as it:
            for entry in it:
                if(entry.is_dir()):
                    self.entries.append(entry)

        with os.scandir(self.path) as it:
            for entry in it:
                if(not entry.is_dir()):
                    self.entries.append(entry)

    def step(self, dx):
        self.activeItemIndex += dx
        if(self.activeItemIndex < 0):
            self.activeItemIndex = len(self.entries) - 1
        elif(self.activeItemIndex >= len(self.entries)):
            self.activeItemIndex = 0
        

    def draw(self):
        currentItemIndex = 0

        for entry in self.entries:
            if self.activeItemIndex == currentItemIndex:
                print(Back.GREEN + entry.name, end = '')
            else:
                print(Back.BLACK + entry.name, end = '')

            currentItemIndex = currentItemIndex + 1
            print(Back.BLACK + '')


        print(Style.RESET_ALL)
    
    def open(self):
        entry = self.entries[self.activeItemIndex]
        if (entry.is_dir()):
            return entry.path
        return None

        


layers = [Layer('.')]

while True:
    os.system("cls")
    layers[-1].draw()
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 80: #Down arrow
        layers[-1].step(1)
    elif key == 72: #Up arrow
        layers[-1].step(-1)
    elif key == 13: #Enter
        child_path =  layers[-1].open()
        if(child_path != None):
            layers.append(Layer(child_path))
    elif key == 8: #Backspace
        layers.pop()
        
    