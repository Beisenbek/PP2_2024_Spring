from msvcrt import getch

while True:
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 13: #Enter
        print('enter!')
    elif key == 80: #Down arrow
        print('down!')
    elif key == 72: #Up arrow
        print('up!')