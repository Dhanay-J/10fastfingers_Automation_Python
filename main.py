from pynput.keyboard import Listener
import random  # Uncomment line 67 & 66 to use this module
import sys
import pyautogui
import time
import os
from PIL import Image

EXIT = False
n = 0
FirstRUN = True
FOLDER = ".\\Screenshot"
if not os.path.exists(FOLDER):
    print("screenshot folder created.")


def screen_capture():
    global FirstRUN, n
    if FirstRUN:
        time.sleep(3)
    FirstRUN = False
    im = pyautogui.screenshot()
    filename = '\\' + f'img{n}.png'
    im.save(FOLDER + filename)
    cropper()
    img2text()
    out_txt_typer()
    n += 1


def cropper(file=f'.\\Screenshot\\img{n}.png', out=f'.\\Screenshot\\img{n}_ocr.png'):
    img = Image.open(file)
    # For Competition Use : box = (330, 280, 1350, 400)
    # For Test Use : box = (330, 320, 1500, 450)
    img_cropped = img.crop(box=(320, 280, 1350, 400))
    img_cropped.save(out)


def img2text():
    os.chdir('Screenshot')
    os.system(f'tesseract.exe .\\img{n}_ocr.png out quiet')
    os.chdir('..')


def op(key):
    global EXIT
    key_press = None
    try:
        key_press = key.name
    except:
        pass
    if key_press == 'shift_r':
        print('Exit')
        EXIT = True
        sys.exit()


def out_txt_typer(file='Screenshot/out.txt', t=0.2):
    # Change t to adjust time delay of typing 
    global EXIT
    # time.sleep(3)
    pyautogui.press('backspace', 50)
    txt = ''
    with open(file, 'r') as f:
        txt = f.readline().strip()
        # if n % 2 == 0:
        #     t = random.randint(0, 30) / 100.0
        pyautogui.write(txt, t)
    print(txt + ' ')
    pyautogui.write(' ')
    if not EXIT:
        screen_capture()


with Listener(on_press=op) as listener:
    screen_capture()
    listener.join()
sys.exit()


# ########## CLICK INSIDE THIS COMMENT BELOW BEFORE EXECUTION TO AVOID CODE DAMAGE ##################

'''
___________________________________________________________________________________________________
___________________________________________________________________________________________________
___________________________________________________________________________________________________
___________________________________________________________________________________________________
___________________________________________________________________________________________________
___________________________________________________________________________________________________

'''

