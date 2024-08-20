import pyautogui as gui
import keyboard
from PIL import Image, ImageGrab
import time

def get_pixel(image, x, y):
    px = image.load()
    return px[x, y]

def start():
    x, y, width, height = 0, 102, 1920, 872
    jumping_time = 0
    last_jumping_time = 0
    current_jumping_time = 0
    last_interval_time = 0
    y_search_for_bird = 460

    time.sleep(3) 

    while True:
        t1 = time.time()
        if keyboard.is_pressed('q'): 
            break

        sct_img = gui.screenshot(region=(x, y, width, height))
        sct_img.save("dino.jpg")  

        
        bg_color = get_pixel(sct_img, 100, 100)

start()   
